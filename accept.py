#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type: text/html\r\n\r\n")

import pymysql, cgi, cgitb

cgitb.enable()

# Get form data
form = cgi.FieldStorage()
request_id = form.getvalue("request_id")

# Connect to database
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

# Update request status to "InProgress"
if request_id:
    try:
        query = "UPDATE service_requests SET status = 'Approved' WHERE id = %s"
        cur.execute(query, (request_id,))
        con.commit()

        # Redirect back to pending.py after update
        print("""
            <script>
                alert("Request accepted successfully!");
                window.location.href = "pending.py?id={}";
            </script>
        """.format(getattr(form.getvalue("id"), 'value', '')))
    except Exception as e:
        print("<p>Error: {}</p>".format(str(e)))
else:
    print("<p>Invalid Request</p>")

con.close()
