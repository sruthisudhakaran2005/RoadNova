#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi, cgitb
import pymysql
import sys
from datetime import datetime

cgitb.enable()
form = cgi.FieldStorage()

request_id = form.getvalue("request_id")
shop_id = form.getvalue("shop_id")

try:
    con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
    cur = con.cursor()

    # Get current extra charge amount and update status
    cur.execute("SELECT extra_charge, extra_charge_status FROM service_requests WHERE request_id=%s", (request_id,))
    result = cur.fetchone()
    if result:
        extra_charge_amount, current_status = result

        # Only update if the status is 'On Hand'
        if current_status == 'On Hand':
            update_query = "UPDATE service_requests SET extra_charge_status = 'Paid' WHERE request_id = %s"
            cur.execute(update_query, (request_id,))

            con.commit()

    con.close()

    print(f"""
    <script>
        alert("Extra charge payment received successfully!");
        window.location.href = "current.py?id={shop_id}";
    </script>
    """)

except pymysql.Error as e:
    print(f"""
    <script>
        alert("Database error: {e}");
        window.location.href = "current.py?id={shop_id}";
    </script>
    """)
    con.rollback()
    con.close()