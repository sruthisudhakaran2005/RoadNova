#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type: text/html\r\n\r\n")

import cgi
import pymysql
import os

# Connect to MySQL database
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

# Get form data
form = cgi.FieldStorage()

# Get values from form
id = form.getfirst("id")  # use getfirst to avoid list issues
name = form.getvalue("name")
dob = form.getvalue("dob")
gender = form.getvalue("gender")
email = form.getvalue("email")
phone = form.getvalue("phone")
address = form.getvalue("address")
shop_name = form.getvalue("shop_name")
shop_address = form.getvalue("shop_address")
operating_hours = form.getvalue("operating_hours")
submit = form.getvalue("submit")

# Default image filenames
fn = ""
simage = ""

if submit is not None:

    # Handle owner image upload
    if 'owner_Image' in form and form['owner_Image'].filename:
        Image = form['owner_Image']
        fn = os.path.basename(Image.filename)
        # Ensure images folder exists
        if not os.path.exists("images"):
            os.makedirs("images")
        with open("images/" + fn, "wb") as f:
            f.write(Image.file.read())
    else:
        # Get existing owner_image from DB
        cur.execute("SELECT owner_image FROM mechanicshops WHERE id=%s", (id,))
        result = cur.fetchone()
        if result:
            fn = result[0]

    # Handle shop image upload
    if 'shop_image' in form and form['shop_image'].filename:
        Shopi = form['shop_image']
        simage = os.path.basename(Shopi.filename)
        if not os.path.exists("images"):
            os.makedirs("images")
        with open("images/" + simage, "wb") as f:
            f.write(Shopi.file.read())
    else:
        # Get existing shop_image from DB
        cur.execute("SELECT shop_image FROM mechanicshops WHERE id=%s", (id,))
        result = cur.fetchone()
        if result:
            simage = result[0]

    # Prepare SQL update query
    q = """
        UPDATE mechanicshops 
        SET owner_name=%s, dob=%s, gender=%s, owner_email=%s, phone=%s, address=%s,
            shop_name=%s, shop_address=%s, operating_hours=%s, 
            owner_image=%s, shop_image=%s
        WHERE id=%s
    """
    params = (
        name, dob, gender, email, phone, address,
        shop_name, shop_address, operating_hours,
        fn, simage, id
    )

    # Execute the query safely
    try:
        cur.execute(q, params)
        con.commit()
    except Exception as e:
        print(f"<p><strong>Database Error:</strong> {e}</p>")

# Final HTML response with success alert and redirect
print(f"""
<html>
  <head>
    <script>
      alert("Profile updated successfully!");
      window.location.href = "owner.py?id={id}";
    </script>
  </head>
  <body></body>
</html>
""")
