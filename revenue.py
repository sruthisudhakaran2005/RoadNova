#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
print("Content-type: text/html\r\n\r\n")

import pymysql
import cgi
import cgitb

cgitb.enable()

# Connect to database
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

# Query to get total earnings per shop
query = """
SELECT m.shop_name, SUM(s.price) AS total_earning
FROM service_requests s
JOIN mechanicshops m ON s.shop_id = m.id 
GROUP BY s.shop_id
"""
cur.execute(query)
results = cur.fetchall()

# HTML Output
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Revenue</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container mt-4">
    <h2 class="mb-4">Shop Revenue Report</h2>
    <table class="table table-bordered table-striped">
        <thead class="table-dark">
            <tr>
                <th>Serial No</th>
                <th>Shop Name</th>
                <th>Total Earnings (₹)</th>
            </tr>
        </thead>
        <tbody>
""")


serial_no = 1
for shop_name, total in results:
    print(f"""
        <tr>
            <td>{serial_no}</td>
            <td>{shop_name}</td>
            <td>{total}</td>
        </tr>
    """)
    serial_no += 1

print("""
        </tbody>
    </table>
</div>
</body>
</html>
""")

  
