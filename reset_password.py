#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
print("Content-Type: text/html\n")

import cgi
import cgitb
import pymysql
import html

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
form = cgi.FieldStorage()
email = form.getvalue("email")
newpass = form.getvalue("newpass")
confirmpass = form.getvalue("confirmpass")

escaped_email = html.escape(email or "")
message = ""
success = None
user_id = None

if email and newpass and confirmpass:
    if newpass != confirmpass:
        message = "Passwords do not match!"
        success = False
    else:
        try:

            con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
            cur = con.cursor()

            cur.execute("UPDATE users SET password=%s, otp=NULL WHERE email=%s", (newpass, email))
            con.commit()

            # Get user_id for redirect
            cur.execute("SELECT user_id FROM users WHERE email=%s", (email,))
            result = cur.fetchone()
            if result:
                user_id = result[0]

            message = "Password reset successful!"
            success = True
        except Exception as e:
            message = f"Error: {e}"
            success = False
        finally:
            if 'cur' in locals():
                cur.close()
            if 'con' in locals():
                con.close()




print(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Reset Password</title>
    <meta charset="utf-8">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
    .navbar-custom {{
        background-color: #ffffff;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        padding: 0.5rem 1rem;
        margin-bottom: 20px;
    }}
    .navbar-brand {{
        font-weight: 700;
        font-size: 1.5rem;
        color: #4a148c;
    }}
    
    .navbar-brand:hover {{
        color: #6a1b9a;
        text-decoration: none;
    }}
    .nav-link {{
        color: #4a148c;
        font-weight: 500;
    }}
    .nav-link:hover {{
        color: #6a1b9a;
    }}
        body {{
            background-color: #f8f9fa;
        }}
        .reset-container {{
            max-width: 450px;
            margin: 80px auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
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
        <div class="reset-container">
            <h3 class="text-center mb-4">Reset Your Password</h3>
""")

# Show result message
if success is not None:
    alert_class = "success" if success else "danger"
    print(f'<div class="alert alert-{alert_class} text-center" id="status-message">{message}</div>')

# Show form again only if not success
if success is not True:
    print(f"""
        <form method="post" action="reset_password.py">
            <input type="hidden" name="email" value="{escaped_email}">
            <div class="mb-3">
                <label class="form-label">New Password</label>
                <input type="password" class="form-control" name="newpass" required>
            </div>
            <div class="mb-3">
                <label class="form-label">Confirm Password</label>
                <input type="password" class="form-control" name="confirmpass" required>
            </div>
            <button type="submit" class="btn btn-success w-100">Reset Password</button>
        </form>
    """)

# JS redirect if success
redirect_script = ""
if success and user_id:
    redirect_script = f"""
        <script>
            document.addEventListener('DOMContentLoaded', function() {{
                const statusMessage = document.getElementById('status-message');
                if (statusMessage) {{
                    const message = statusMessage.textContent.trim();
                    const successMessage = "Password reset successful!";
                    if (message === successMessage) {{
                        setTimeout(() => {{
                            window.location.href = "user.py?user_id={user_id}";
                        }}, 3000);
                    }}
                }}
            }});
        </script>
    """

print(f"""
        </div>
    </div>
    {redirect_script}
</body>
</html>
""")
