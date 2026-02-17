#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
import pymysql, cgi, cgitb

print("content-type:text/html \r\n\r\n")

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

form = cgi.FieldStorage()
owner_email = form.getvalue("ownermail")
owner_pass = form.getvalue("mechanicpass")
cur.execute("SELECT status FROM mechanicshops WHERE owner_email=%s", (owner_email,))
result = cur.fetchone()
if result is not None:
    status = result[0]
    if status != 'Blocked':
        if owner_email != None and owner_pass != None:
            q = """select id from mechanicshops where owner_email="%s" and password="%s" """ % (owner_email, owner_pass)
            cur.execute(q)
            res = cur.fetchone()
            if res is not None:
                print("""
                                    <script>
                                    alert("login success!");
                                     window.top.location.href="mech.py?id=%s"
                                    </script>
                                    """ % (res[0]))

            else:
                print("""
                        <script>
                        alert("incorrect email or password" );
                         location.href="home.py"
                        </script>
                        """)
    else:
        print("""
                <script>
                    alert("Your account has been blocked by the system administrator. Please contact support or your administrator for further assistance.");
                    location.href="home.py";
                </script>
            """)



