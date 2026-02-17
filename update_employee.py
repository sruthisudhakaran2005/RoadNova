#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("content-type:text/html\r\n\r\n")

import cgi
import cgitb
import os
import shutil
import pymysql
import html  # For escaping error messages safely

cgitb.enable()

# Config - Make sure these folders exist and are writable
UPLOAD_PHOTO_DIR = "uploads/photos/"
UPLOAD_IDPROOF_DIR = "uploads/idproofs/"

# Connect DB
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

form = cgi.FieldStorage()

try:
    id = form.getvalue("id")
    mechanic_id = form.getvalue("mechanic_id")
    full_name = form.getvalue("full_name")
    phone = form.getvalue("phone")
    email = form.getvalue("email")
    address = form.getvalue("address")
    specialization = form.getvalue("specialization")
    experience = form.getvalue("experience")
    dob = form.getvalue("dob")  # YYYY-MM-DD or None
    gender = form.getvalue("gender")

    # Fetch existing filenames so we don't lose them if no new file uploaded
    cur.execute("SELECT image, idproof, shop_id FROM mechanics WHERE mech_id = %s", (mechanic_id,))
    row = cur.fetchone()

    if not row:
        raise Exception("Mechanic not found.")

    old_profile_pic, old_id_proof, shop_id = row

    # Handle profile picture upload
    profile_pic_field = form["profile_pic"] if "profile_pic" in form else None
    if profile_pic_field is not None and getattr(profile_pic_field, 'filename', None):
        filename = os.path.basename(profile_pic_field.filename)
        filepath = os.path.join(UPLOAD_PHOTO_DIR, filename)

        # Save file
        with open(filepath, "wb") as f:
            shutil.copyfileobj(profile_pic_field.file, f)
        new_profile_pic = filename
    else:
        new_profile_pic = old_profile_pic

    # Handle ID proof upload
    id_proof_field = form["id_proof"] if "id_proof" in form else None
    if id_proof_field is not None and getattr(id_proof_field, 'filename', None):
        filename = os.path.basename(id_proof_field.filename)
        filepath = os.path.join(UPLOAD_IDPROOF_DIR, filename)

        with open(filepath, "wb") as f:
            shutil.copyfileobj(id_proof_field.file, f)
        new_id_proof = filename
    else:
        new_id_proof = old_id_proof

    # Update query
    update_sql = """
    UPDATE mechanics SET
      name=%s,
      phone=%s,
      mail=%s,
      address=%s,
      specialization=%s,
      experience=%s,
      dob=%s,
      gender=%s,
      image=%s,
      idproof=%s
    WHERE mech_id=%s
    """
    cur.execute(update_sql, (
        full_name,
        phone,
        email,
        address,
        specialization,
        experience,
        dob if dob else None,
        gender,
        new_profile_pic,
        new_id_proof,
        mechanic_id
    ))
    con.commit()

    print(f"""
    <html>
    <head>
        <meta http-equiv="refresh" content="2; url=view.py?id={shop_id}" />
    </head>
    <body>
    <h3 style="color:green; text-align:center; margin-top:50px;">Mechanic details updated successfully!</h3>
    </body>
    </html>
    """)

except Exception as e:
    print(f"<h3 style='color:red;'>Error: {html.escape(str(e))}</h3>")

finally:
    cur.close()
    con.close()
