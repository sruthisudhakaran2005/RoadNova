#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type: text/html\r\n\r\n")

import pymysql
import cgi
import cgitb
import sys
import io

# Enable CGI traceback for debugging
cgitb.enable()

# Use cgi.FieldStorage() to get form data
form = cgi.FieldStorage()
request_id = form.getvalue("request_id")
shop_id = form.getvalue("shop_id")

if request_id is not None:
    con = None  # Initialize connection to None for safety
    try:
        con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
        cur = con.cursor()

        # SQL query to update payment status
        q = "UPDATE service_requests SET payment_status = 'Paid' WHERE request_id = %s"
        cur.execute(q, (request_id,))

        con.commit()

        # Redirect to the previous page using an HTML redirect
        print(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta http-equiv="refresh" content="0;url=current.py?id={shop_id}">
        </head>
        <body>
            <p>Payment status updated. Redirecting...</p>
        </body>
        </html>
        """)

    except pymysql.MySQLError as e:
        if con:
            con.rollback()
        print(f"<h2>Database Error: {e}</h2>")
    finally:
        if con:
            con.close()
else:
    print("<h2>Error: Missing request ID.</h2>")