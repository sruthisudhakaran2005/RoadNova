#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
import pymysql, cgi, cgitb

print("content-type:text/html \r\n\r\n")

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

form = cgi.FieldStorage()

Email = form.getvalue("usermail")
Password = form.getvalue("password")
Submit = form.getvalue("submit")

if Submit != None:
    q = """select user_id from users where email="%s" and password="%s" """ %( Email, Password)
    cur.execute(q)
    res = cur.fetchone()
    if res is not None:
        print("""
        <script>
        alert("login success!");
        window.top.location.href="user.py?user_id=%s"
        </script>
        """ % (res[0]))
    else:
        print("""
        <script>
        alert("incorrect username or password" );
        </script>
        """)
