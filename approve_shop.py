#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')
print("Content-type: text/html\r\n\r\n")

import cgi, cgitb

cgitb.enable()

import pymysql
import smtplib



con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
form = cgi.FieldStorage()
shop_id = form.getvalue("shop_id")
password = form.getvalue("password")
q = """select * from mechanicshops where id='%s' """%(shop_id)
cur.execute(q)
res = cur.fetchall()
for i in res:
    email = i[17]
    name = i[1]
if password is not None:
    q = "UPDATE mechanicshops SET status=%s, password=%s WHERE id=%s"
    cur.execute(q, ('Approved', password, shop_id))

    con.commit()
    print("""
    <script>
    alert("mechanic shop approved");
    </script>
    """)
    fromadd = 'sruthisudhakaran2005@gmail.com'
    ppasswod = 'trng sjeu embt htce'
    toadd = email
    subject = "your registration request is approved from roadnova"
    body = "hello %s your password is %s" % (name, password)
    msg = """Subject:%s \n\n%s""" % (subject, body)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(fromadd, ppasswod)
    server.sendmail(fromadd, toadd, msg)
    server.quit()
    print("""
           <script>
           alert("mail send successfully");
           window.top.location.href="new_requests.py"
           </script>
           """)

