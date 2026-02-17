#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type: text/html\r\n\r\n")

import pymysql
import cgi
import cgitb
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Enable error display
cgitb.enable()

# Database connection
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

# Get form data
form = cgi.FieldStorage()
request_id = form.getvalue("request_id")
status = form.getvalue("status")
shop_id = form.getvalue("shop_id")

# Fetch service request
cur.execute("SELECT * FROM service_requests WHERE request_id=%s", (request_id,))
res = cur.fetchall()
for i in res:
    issue = i[3]
    user_id = i[1]
    mech_id = i[6]

# Fetch shop name
cur.execute("SELECT shop_name FROM mechanicshops WHERE id=%s", (shop_id,))
r = cur.fetchone()
shop_name = r[0] if r else "Unknown Shop"

# Fetch mechanic name
cur.execute("SELECT name FROM mechanics WHERE mech_id=%s", (mech_id,))
result = cur.fetchone()
mech_name = result[0] if result else "Unknown Mechanic"

# Fetch user details
cur.execute("SELECT * FROM users WHERE user_id=%s", (user_id,))
user = cur.fetchall()
for i in user:
    user_name = i[1]
    email = i[3]

if request_id and status:
    # Update request status
    cur.execute(
        "UPDATE service_requests SET status=%s, completed_date=CURRENT_TIMESTAMP WHERE request_id=%s",
        (status, request_id)
    )
    con.commit()
    con.close()

    # Email setup
    fromadd = 'sruthisudhakaran2005@gmail.com'
    ppasswod = 'trng sjeu embt htce'  # ⚠️ Consider storing this securely!
    toadd = email
    subject = "Your service completed from RoadNova"

    body = f"""Hello {user_name},

Your service request has been completed. Below are the details:

• Issue: {issue}  
• Assigned Mechanic: {mech_name}  
• Shop: {shop_name}

Thank you for choosing our service.
Please take a moment to rate and review your experience with {shop_name}.

Regards,  
RoadNova Support Team
"""

    # Build email using MIME
    msg = MIMEMultipart()
    msg['From'] = fromadd
    msg['To'] = toadd
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(fromadd, ppasswod)
        server.sendmail(fromadd, toadd, msg.as_string())
        server.quit()

        print(f"""
        <html>
          <head>
            <script>
              alert("Request marked as completed! Mail sent successfully.");
              window.location.href = "current.py?id={shop_id}";
            </script>
          </head>
          <body></body>
        </html>
        """)
    except Exception as e:
        print(f"""
        <html>
          <head>
            <script>
              alert("Request updated but failed to send email: {str(e)}");
              window.location.href = "current.py?id={shop_id}";
            </script>
          </head>
          <body></body>
        </html>
        """)

else:
    print("""
    <html>
      <head>
        <script>
          alert("Missing request ID or status. Update failed.");
          window.history.back();
        </script>
      </head>
      <body></body>
    </html>
    """)
