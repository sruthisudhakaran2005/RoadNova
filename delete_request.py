#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe

print("Content-Type: text/html\r\n\r\n")

import pymysql, cgi, cgitb

cgitb.enable()

form = cgi.FieldStorage()
request_id = form.getvalue("request_id")

if request_id:
    try:
        con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
        cur = con.cursor()

        # Delete the service request
        cur.execute("DELETE FROM service_requests WHERE request_id = %s", (request_id,))
        con.commit()

        # Redirect back to the admin dashboard
        print("<script>window.location.href='all_requests.py';</script>")  # Replace with your admin page
    except Exception as e:
        print(f"<h4>Error: {e}</h4>")
    finally:
        con.close()
else:
    print("<h4>Invalid request. No ID provided.</h4>")
