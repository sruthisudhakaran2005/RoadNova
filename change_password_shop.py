#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe

import cgi, cgitb, pymysql

cgitb.enable()
print("Content-Type: text/html\r\n\r\n")

form = cgi.FieldStorage()
shop_id = form.getvalue("id")
current = form.getfirst("current_password", "")
new = form.getfirst("new_password", "")
confirm = form.getfirst("confirm_password", "")

con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

# Fetch current password from database
query = "SELECT password FROM mechanicshops WHERE id=%s"
cur.execute(query, (shop_id,))
res = cur.fetchone()

if res and current == res[0]:
    if current == new:
        # Same as current password
        print(f"""
        <html><body>
        <script>
            alert("Current password and new password are the same!");
            window.location.href = "owner.py?id={shop_id}";
        </script>
        </body></html>
        """)
    elif new != confirm:
        # New and confirm passwords don't match
        print(f"""
        <html><body>
        <script>
            alert("New password and confirm password do not match!");
            window.location.href = "owner.py?id={shop_id}";
        </script>
        </body></html>
        """)
    else:
        # Update password
        update_query = "UPDATE mechanicshops SET password=%s WHERE id=%s"
        cur.execute(update_query, (new, shop_id))
        con.commit()
        print(f"""
        <html><body>
        <script>
            alert("Password changed successfully!");
            window.location.href = "owner.py?id={shop_id}";
        </script>
        </body></html>
        """)
else:
    # Incorrect current password
    print(f"""
    <html><body>
    <script>
        alert("Current password is incorrect!");
        window.location.href = "owner.py?id={shop_id}";
    </script>
    </body></html>
    """)

cur.close()
con.close()
