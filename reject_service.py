#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type: text/html\r\n\r\n")

import pymysql
import cgi
import cgitb
import smtplib
from email.message import EmailMessage
import html

cgitb.enable()

# Get form data
form = cgi.FieldStorage()
request_id = form.getvalue("request_id")
status = form.getvalue("status")
shop_id = form.getvalue("shop_id")
email = form.getvalue("email")
note = form.getvalue("rejection_note")

try:
    request_id = int(request_id)
    shop_id = int(shop_id)
except (ValueError, TypeError):
    print("<h3>Invalid request or shop ID.</h3>")
    exit()

email = html.escape(email)

con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

# Check if 'note' is provided. If not, use a default message.
if note:
    message = note
else:
    message = "Your service request has been rejected due to unforeseen circumstances or scheduling conflicts."

q = """select * from service_requests where request_id=%s """
cur.execute(q, (request_id,))
res = cur.fetchall()
user_id = None
for i in res:
    user_id = i[1]

x = """select shop_name from mechanicshops where id=%s """
cur.execute(x, (shop_id,))
r = cur.fetchone()
shop_name = r[0] if r else "RoadNova Mechanic Shop"

if user_id is not None:
    notif_query = """
           INSERT INTO notifications(user_id, request_id, shop_name, message)
           VALUES (%s, %s, %s, %s)
       """
    cur.execute(notif_query, (user_id, request_id, shop_name, message))
    con.commit()

cur.execute("UPDATE service_requests SET status=%s WHERE request_id=%s", (status, request_id))
con.commit()

fromadd = 'sruthisudhakaran2005@gmail.com'
ppasswod = 'trng sjeu embt htce'
toadd = email
subject = "Your Service Request Has Been Rejected"
# Use the 'message' variable for the email body
body = f"""
Dear Customer,

We regret to inform you that your service request has been rejected.

Rejection Reason: {message}

You may submit a new request if needed, or contact support for more details.

Thank you for using RoadNova.

Best regards,
RoadNova Team
"""
msg = f"Subject:{subject}\n\n{body}"

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(fromadd, ppasswod)
    server.sendmail(fromadd, toadd, msg)
    server.quit()
except Exception as e:
    # Print a more informative error message to the browser
    print(f"An error occurred while sending the email: {e}")
    # You might want to log this error as well

print(f"""
<script>
  alert("service Request rejected and customer notified.");
  window.location.href = "pending.py?id={shop_id}";
</script>
""")

con.close()