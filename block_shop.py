#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe

print("Content-Type: text/html\r\n\r\n")

import pymysql, cgi, cgitb

cgitb.enable()

form = cgi.FieldStorage()
shop_id = form.getvalue("shop_id")

if shop_id:
    try:
        con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
        cur = con.cursor()

        cur.execute("UPDATE mechanicshops SET status = 'Blocked' WHERE id = %s", (shop_id,))
        con.commit()

        # Redirect back to the page
        print(
            "<script>alert('Shop has been blocked successfully.'); window.location.href='approved.py';</script>")
    except Exception as e:
        print(f"<h4>Error: {e}</h4>")
    finally:
        con.close()
else:
    print("<h4>Invalid request. Shop ID not provided.</h4>")
