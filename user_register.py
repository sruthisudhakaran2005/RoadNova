#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html\r\n\r\n")

import pymysql, cgi, cgitb
cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

form = cgi.FieldStorage()

# Check if this is a registration submission
if "name" in form:
    name = form.getvalue("name")
    gender = form.getvalue("gender")
    email = form.getvalue("email")
    phone = form.getvalue("phone")
    address = form.getvalue("address")
    pincode = form.getvalue("pincode")
    password = form.getvalue("password")
    confirmpass = form.getvalue("confirmpass")

    if password != confirmpass:
        print("<script>alert('Passwords do not match');</script>")
    else:
        try:
            query = "INSERT INTO users (name, gender, email, phone, address, pincode, password, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(query, (name, gender, email, phone, address, pincode, password, 'Registered'))
            con.commit()
            print("<script>alert('Registration successful');</script>")
        except Exception as e:
            print(f"<script>alert('Error: {str(e)}');</script>")