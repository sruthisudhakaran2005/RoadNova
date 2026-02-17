#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')
print("Content-type: text/html\r\n\r\n")

import cgi, cgitb

cgitb.enable()

import pymysql
import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

form = cgi.FieldStorage()
email = form.getvalue("email")


print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Password Reset</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .navbar {
            background-color: #ffffff;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .navbar-brand {
            font-weight: bold;
            color: #ff4500;
        }

        .navbar-brand:hover {
            color: #c0392b;
        }

        .nav-link {
            color: #333;
            font-weight: 500;
        }

        .nav-link:hover {
            color: #007bff;
        }

        .container {
            max-width: 600px;
            margin-top: 100px;
            margin-left:350px;
            padding: 30px;
            background-color: white;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }
        .btn-primary {
            background-color: #ff5722;
            border-color: #ff5722;
        }
        .btn-primary:hover {
            background-color: #e64a19;
            border-color: #e64a19;
        }
        .alert {
            font-size: 1.1rem;
        }
    </style>
</head>
<body>
<nav class="navbar navbar-expand-lg fixed-top " >
      <div class="container-fluid">
        <a class="navbar-brand" href="home.py">
          <i class="fas fa-car-crash me-2"></i>RoadNova
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" href="home.py">Home</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
<div class="container">
""")

# Validate email in DB
cur.execute("SELECT * FROM mechanicshops WHERE owner_email=%s", (email,))
res = cur.fetchone()

if res:
    shop_name = res[10]
    # Generate new password
    new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))



    cur.execute("UPDATE mechanicshops SET password=%s WHERE owner_email=%s", (new_password, email))
    con.commit()

    from_email = 'sruthisudhakaran2005@gmail.com'
    app_password = 'trng sjeu embt htce'
    to_email = email

    subject = f"🔒 RoadNova Password Reset TO{shop_name}"
    body = f"""
    Dear Mechanic Shop Owner,

    You recently requested to reset your password.

    🔐 Your new temporary password is: {new_password}

    Please login and change it immediately for your security.

    Regards,  
    RoadNova Team
    """

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, app_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()

        print(f"""
        <div class="alert alert-success text-center" role="alert">
            ✅ Password reset successful! A new password has been sent to <strong>{email}</strong>.
        </div>
        """)
    except Exception as e:
        print(f"""
        <div class="alert alert-danger text-center" role="alert">
            ❌ Failed to send email. Please try again later.<br>
            Error: {str(e)}
        </div>
        """)
else:
    print(f"""
    <div class="alert alert-warning text-center" role="alert">
        ⚠️ The email <strong>{email}</strong> is not registered in our system.
    </div>
    """)


print("""
    <div class="text-center">
        <a href="forgot_shop_password.py" class="btn btn-primary mt-4">🔙 Go Back</a>
    </div>
</div>
</body>
</html>
""")


con.close()
