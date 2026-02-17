#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
import pymysql, cgi, cgitb

print("content-type:text/html \r\n\r\n")

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

form = cgi.FieldStorage()
admin_email = form.getvalue("adminmail")
admin_pass = form.getvalue("adminpass")
Submit = form.getvalue("submit")

if Submit != None:
    q = """select id from admin where email="%s" and password="%s" """ % (admin_email, admin_pass)
    cur.execute(q)
    res = cur.fetchone()
    if res is not None:
        print("""
        <script>
        alert("login success!");
         window.top.location.href="admin.py?id=%s"
        </script>
        """ % (res[0]))
    else:
        print("""
        <script>
        alert("incorrect username or password" );
        location.href="home.py"
        </script>
        """)