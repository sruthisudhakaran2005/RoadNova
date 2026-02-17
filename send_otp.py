#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys
import cgi
import cgitb
import pymysql
import smtplib
from email.mime.text import MIMEText
import random
import os

# Enable CGI error tracing
cgitb.enable()

# Ensure proper encoding for stdout
sys.stdout.reconfigure(encoding='utf-8')
print("Content-Type: text/html\n")

# Get form data
form = cgi.FieldStorage()
email = form.getvalue("email")

if not email:
    print("""
    <script>
    alert("Email is required.");
    location.href="forgot_password.py";
    </script>
    """)
    sys.exit()

else:
    # Connect to database
    con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
    cur = con.cursor()

    # Parameterized query to check if email exists
    cur.execute("SELECT user_id, name FROM users WHERE email = %s", (email,))
    user = cur.fetchone()

    if user:
        user_id, name = user
        otp = str(random.randint(100000, 999999))

        # Email settings
        sender_email = "sruthisudhakaran2005@gmail.com"
        sender_password = "trng sjeu embt htce"  # Consider using env vars in production
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Prepare the email content
        subject = "Your OTP for Password Reset from RoadNova"
        body = f"""
        Hello {name},
        
        Your One-Time OTP for resetting your password is: {otp}
        
        This OTP is valid for 5 minutes. Do not share it with anyone.
        
        Regards,
        RoadNova Support
        """
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = email

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, msg.as_string())

        # Save OTP in the database
        cur.execute("UPDATE users SET otp = %s WHERE email = %s", (otp, email))
        con.commit()

        print(f"""
        <script>
        alert("OTP sent to your email!");
        location.href="verify_otp.py?email={email}";
        </script>
        """)
    else:
        print("""
        <script>
        alert("Email not found. Please check your email address.");
        location.href="forgot_password.py";
        </script>
        """)


con.commit()

