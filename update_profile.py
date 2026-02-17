#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type: text/html\r\n\r\n")
import pymysql, cgi

form = cgi.FieldStorage()
user_id = form.getvalue("user_id")
name = form.getvalue("name")
gender = form.getvalue("gender")
email = form.getvalue("email")
phone = form.getvalue("phone")
address = form.getvalue("address")
pincode = form.getvalue("pincode")

con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

cur.execute("""
    UPDATE users SET name=%s, gender=%s, email=%s, phone=%s, address=%s, pincode=%s 
    WHERE user_id=%s
""", (name, gender, email, phone, address, pincode, user_id))

con.commit()
con.close()

print(f"""
<script>
alert("profile updated successfully!");
window.location.href = "user_profile.py?user_id={user_id}"
</script>
""")
