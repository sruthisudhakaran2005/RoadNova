#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
import cgi, cgitb, pymysql, json

cgitb.enable()
print("Content-Type: application/json\n")

form = cgi.FieldStorage()
id = form.getvalue("id")
status = form.getvalue("status")  # "Open" or "Closed"

response = {"success": False, "message": ""}

if id and status in ("Open", "Closed"):
    try:
        con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
        cur = con.cursor()
        query = "UPDATE mechanicshops SET availability=%s WHERE id=%s"
        cur.execute(query, (status, id))
        con.commit()
        cur.close()
        con.close()
        response["success"] = True
        response["message"] = f"Availability updated to {status}"
    except Exception as e:
        response["message"] = str(e)
else:
    response["message"] = "Invalid parameters"

print(json.dumps(response))
