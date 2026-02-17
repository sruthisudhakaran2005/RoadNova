#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type: text/html\r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
form = cgi.FieldStorage()

user_id = form.getvalue("user_id")
current_password = form.getvalue("current_password")
new_password = form.getvalue("new_password")
confirm_password = form.getvalue("confirm_password")

con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

# Fetch current password from DB
cur.execute("SELECT password FROM users WHERE user_id=%s", (user_id,))
row = cur.fetchone()

error = None

if current_password != row[0]:
    print(f"""
    <script>
    alert("Current password is incorrect.");
     window.location.href = "user_profile.py?user_id={user_id}"
    </script>
    """)
elif current_password == new_password:
    print(f"""
       <script>
       alert("Current password and new password is same.");
        window.location.href = "user_profile.py?user_id={user_id}"
       </script>
       """)
elif new_password != confirm_password:
    print(f"""
    <script> alert("New password and confirm password do not match.");
     window.location.href = "user_profile.py?user_id={user_id}"
    </script>
    """)
else:
    # Update password in DB
    cur.execute("UPDATE users SET password=%s WHERE user_id=%s", (new_password, user_id))
    con.commit()
    print(f"""
       <script>
       alert("password changed successfully!");
       window.location.href = "user_profile.py?user_id={user_id}"
       </script>
       """)

con.close()



