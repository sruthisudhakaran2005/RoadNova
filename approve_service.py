#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-

import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Content-Type: text/html\r\n\r\n")

import pymysql
import cgi
import cgitb
import smtplib
from email.message import EmailMessage

cgitb.enable()

form = cgi.FieldStorage()

# Get form values safely and provide default values
request_id = form.getvalue("request_id")
status = form.getvalue("status")
shop_id = form.getvalue("shop_id")
email = form.getvalue("email")
mechanic_id = form.getvalue("mechanic_id")
service_id = form.getvalue("service_id")
manual_price = form.getvalue("manual_price")
# Provide a default value if the form field is empty or missing
notification_msg = form.getvalue("notification_message") or "Your service request has been approved."

# Connect to the database
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

# ---------------------- [1] Get email and user_id from request_id if email is missing -----------------------
if not email:
    cur.execute("""
        SELECT u.email, u.user_id 
        FROM service_requests r 
        JOIN users u ON r.user_id = u.user_id 
        WHERE r.request_id = %s
    """, (request_id,))
    user_data = cur.fetchone()
    if user_data:
        email, user_id = user_data
    else:
        print(f"<h3>Error: No user associated with request ID {request_id}</h3>")
        con.close()
        sys.exit()
else:
    # Email is provided, get user_id from email
    cur.execute("SELECT user_id FROM users WHERE email = %s", (email,))
    res = cur.fetchone()
    if res:
        user_id = res[0]
    else:
        print(f"<h3>Error: No user found with email '{email}'</h3>")
        con.close()
        sys.exit()

# ---------------------- [2] Get shop_name from shop_id -----------------------
cur.execute("SELECT * FROM mechanicshops WHERE id = %s", (shop_id,))
shop_row = cur.fetchone()

if shop_row:
    shop_name = shop_row[10]  # Assuming index 10 is correct
else:
    print(f"<h3>Error: No shop found with ID '{shop_id}'</h3>")
    con.close()
    sys.exit()

# ---------------------- [3] Insert notification -----------------------
notif_query = """
    INSERT INTO notifications(user_id, request_id, shop_name, message)
    VALUES (%s, %s, %s, %s)
"""
cur.execute(notif_query, (user_id, request_id, shop_name, notification_msg))
con.commit()

# ---------------------- [4] Get mechanic info -----------------------
cur.execute("SELECT name, phone FROM mechanics WHERE mech_id = %s", (mechanic_id,))
mech = cur.fetchone()
mech_name, mech_phone = mech if mech else ("Unknown", "N/A")

# ---------------------- [5] Get user name for email -----------------------
cur.execute("""
    SELECT u.name 
    FROM service_requests r 
    JOIN users u ON r.user_id = u.user_id 
    WHERE r.request_id = %s
""", (request_id,))
user_row = cur.fetchone()
user_name = user_row[0] if user_row else "Customer"

# ---------------------- [6] Handle price and service name -----------------------
if service_id:
    cur.execute("SELECT price, service_name FROM services WHERE service_id = %s", (service_id,))
    service_row = cur.fetchone()
    if service_row:
        price, service_name = service_row
    else:
        price, service_name = 0, "Unknown"
else:
    service_name = "Custom Service"
    price = float(manual_price) if manual_price else 0
    service_id = None

# ---------------------- [7] Update service request -----------------------
cur.execute("""
    UPDATE service_requests 
    SET status = %s, mech_id = %s, price = %s 
    WHERE request_id = %s
""", (status, mechanic_id, price, request_id))
con.commit()

# ---------------------- [8] Send email to user -----------------------
fromadd = 'sruthisudhakaran2005@gmail.com'
ppasswod = 'trng sjeu embt htce'
toadd = email.strip()

subject = f"Your Service Request Has Been Approved"
body = f"""Dear {user_name},

✅ Your service request has been approved.
🏪 Shop Name: {shop_name}
🧰 Assigned Mechanic: {mech_name}
📞 Contact: {mech_phone}

🛠️ Service: {service_name}
💰 Charge: ₹{price}

📩 Message from the Service Center:
{notification_msg}

Thank you for using RoadNova!
"""

msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = fromadd
msg['To'] = toadd
msg.set_content(body)

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(fromadd, ppasswod)
    server.send_message(msg)
    server.quit()

    print(f"""
    <script>
        alert("Request approved and mail sent!");
        window.location.href = "pending.py?id={shop_id}";
    </script>
    """)
except Exception as e:
    print(f"""
       <script>
           alert("there is an error while processing request!");
           window.location.href = "pending.py?id={shop_id}";
       </script>
       """)


con.close()
