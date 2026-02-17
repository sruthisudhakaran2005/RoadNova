#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')
print("content-type:text/html \r\n\r\n")

import pymysql, cgi, cgitb

# Enable for debugging
cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

form = cgi.FieldStorage()
email = form.getvalue("email")
otp = form.getvalue("otp")

# Check if OTP is submitted
if otp:
    # Verify the OTP
    q = """
    SELECT email FROM users WHERE email="%s" AND otp="%s"
    """ % (email, otp)
    cur.execute(q)
    res = cur.fetchone()

    if res:
        print("""
        <script>
        alert("OTP verified successfully! You can now reset your password.");
        location.href="reset_password.py?email=%s"
        </script>
        """ % email)
    else:
        print("""
        <script>
        alert("Invalid or expired OTP. Please try again.");
        location.href="verify_otp.py?email=%s"
        </script>
        """ % email)
else:
    # Display the OTP form
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Verify OTP</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background-color: #f8f9fa;
            }
            .form-container {
                max-width: 450px;
                margin: 100px auto;
                padding: 30px;
                background-color: #ffffff;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            }
        </style>
    </head>
    <body>
    <nav class="navbar navbar-expand-lg fixed-top">
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
            <div class="form-container">
                <h2>Verify OTP</h2>
                <p class="text-center">An OTP has been sent to **%s**. Please enter it below.</p>
                <form action="verify_otp.py" method="post">
                    <input type="hidden" name="email" value="%s">
                    <div class="mb-3">
                        <label for="otp" class="form-label">Enter OTP</label>
                        <input type="text" class="form-control" id="otp" name="otp" required>
                    </div>
                    <button type="submit" class="btn btn-primary w-100">Verify OTP</button>
                </form>
            </div>
        </div>
    </body>
    </html>
    """ % (email, email))

cur.close()
con.close()