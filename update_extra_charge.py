#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import cgi
import cgitb
import pymysql
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print("Content-Type: text/html; charset=utf-8\r\n\r\n")

cgitb.enable()

form = cgi.FieldStorage()
shop_id = form.getvalue("id")
request_id = form.getvalue('request_id')
extra_charge = form.getvalue('extra_charge')
extra_note = form.getvalue('extra_note')
email = form.getvalue("email")
name = form.getvalue("name")

con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

try:
    sql = "UPDATE service_requests SET extra_charge=%s, extra_charge_status='Pending' WHERE request_id=%s"
    cur.execute(sql, (extra_charge, request_id))

    # Get user_id
    cur.execute("SELECT user_id FROM service_requests WHERE request_id=%s", (request_id,))
    r = cur.fetchone()
    if r:
        user_id = r[0]
    else:
        raise Exception("User ID not found for request.")

    # Get shop_name
    cur.execute("SELECT shop_name FROM mechanicshops WHERE id=%s", (shop_id,))
    res = cur.fetchone()
    if res:
        shop_name = res[0]
    else:
        raise Exception("Shop name not found.")

    # Insert into notifications table
    if extra_note:
        notif_query = """
            INSERT INTO notifications(user_id, request_id, shop_name, message)
            VALUES (%s, %s, %s, %s)
        """
        cur.execute(notif_query, (user_id, request_id, shop_name, extra_note))

        # Email setup
        fromadd = 'sruthisudhakaran2005@gmail.com'
        ppassword = 'trng sjeu embt htce'  # App password (never hard-code in real apps)
        toadd = email
        subject = "Additional charge for your service from RoadNova"

        body = f"""Hello {name},

An additional charge of ₹{extra_charge} has been added to your service request for the following reason:

{extra_note}

Thank you for choosing our service.

Regards,  
RoadNova Support Team
"""

        # Create UTF-8 encoded email
        msg = MIMEMultipart()
        msg['From'] = fromadd
        msg['To'] = toadd
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        # Send email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(fromadd, ppassword)
        server.send_message(msg)
        server.quit()

    # Success response
    print(f"""<script>
        alert("Extra charge added! Mail sent successfully.");
        window.location.href = "current.py?id={shop_id}";
    </script>""")

except Exception as e:
    print("<h1>Error occurred:</h1>")
    print(f"<pre>{str(e)}</pre>")

finally:
    con.commit()
    con.close()
