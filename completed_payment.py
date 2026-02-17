#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
print("Content-type: text/html\n")

import pymysql, cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
shop_id = form.getvalue("id")

con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

query = """
    SELECT sr.request_id, u.name, sr.price, sr.payment_status, sr.request_date
    FROM service_requests sr
    JOIN users u ON sr.user_id = u.user_id
    WHERE sr.payment_status = 'Paid' AND sr.shop_id = %s 
    ORDER BY sr.request_date DESC
"""
cur.execute(query, (shop_id,))
data = cur.fetchall()


print("""
<!DOCTYPE html>
<html>
<head>
    <title>Completed Payments</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f4f7fa;
            padding: 20px;
        }
        .table-wrapper {
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
            padding: 20px;
        }
        .table thead {
            background-color: #2e8bc0;
            color: white;
        }
        .table tbody tr:hover {
            background-color: #eef7ff;
        }
        .status-pending {
            background-color: #fff3cd;
            color: #856404;
            padding: 4px 10px;
            border-radius: 15px;
            font-size: 0.9rem;
            font-weight: 500;
        }
    </style>
</head>
<body>

    <div class="table-wrapper">
        <h3 class="mb-4 text-primary"><i class="bi bi-wallet2 me-2"></i>Completed Payments</h3>
""")

if data:
    print("""
        <div class="table-responsive">
            <table class="table table-bordered table-hover align-middle">
                <thead class="text-center">
                    <tr><th>S.NO</th>
                        <th>Customer Name</th>
                        <th>Amount (₹)</th>
                        <th>Date</th>
                        <th>Payment Status</th>
                    </tr>
                </thead>
                <tbody>
    """)
    for idx, row in enumerate(data, start=1):
        req_id, username, price, status, date = row
        price_display = f"₹{price:.2f}" if price is not None else "N/A"
        date_display = date.strftime('%b %d, %Y') if hasattr(date, 'strftime') else str(date)
        print(f"""
        <tr class="text-center">
            <td>{idx}</td>
            <td>{username}</td>
            <td class="text-end">{price_display}</td>
            <td>{date_display}</td>
            <td><span class="status-pending">{status}</span></td>
        </tr>
        """)

    print("""
                </tbody>
            </table>
        </div>
    """)
else:
    print("""
        <div class="alert alert-info text-center">
            <i class="bi bi-info-circle"></i> No Completed  payments found.
        </div>
    """)

print("""
    </div> <!-- end wrapper -->

</body>
</html>
""")

cur.close()
con.close()
