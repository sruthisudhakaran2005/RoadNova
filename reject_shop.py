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
q = """select * from mechanicshops where id='%s' """%(shop_id)
cur.execute(q)
res = cur.fetchall()
for i in res:
    email = i[17]
    name = i[1]
if shop_id is not None:
    q = """ update mechanicshops set status='%s'  where id='%s' """%('Rejected', shop_id)
    cur.execute(q)
    con.commit()
    print("""
    <script>
    alert("mechanic shop rejected");
    </script>
    """)
    fromadd = 'sruthisudhakaran2005@gmail.com'
    ppasswod = 'trng sjeu embt htce'
    toadd = email
    subject = "your registration request is rejected from roadnova"
    body = "hello %s your application has been rejected " % (name)
    msg = """Subject:%s \n\n%s """ % (subject, body)
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

