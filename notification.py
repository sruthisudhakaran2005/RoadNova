#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')
print("Content-type: text/html\n")
import pymysql, cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
user_id = form.getvalue("user_id")

con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

# Fetch notifications for the user
query = """
    SELECT n.message, n.created_at, s.shop_name, s.shop_image, n.request_id
    FROM notifications n 
    JOIN mechanicshops s ON n.shop_name = s.shop_name 
    WHERE n.user_id = %s 
    ORDER BY n.created_at DESC
"""
cur.execute(query, (user_id,))
notifications = cur.fetchall()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Notifications</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">
    <style>
        body {
            background-color: #f4f7fa;
            padding: 20px;
            font-family: 'Segoe UI', sans-serif;
        }
        .notif-card {
            transition: 0.3s;
            border-left: 5px solid #0d6efd;
        }
        .notif-card:hover {
            transform: scale(1.01);
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        .shop-img {
            width: 60px;
            height: 60px;
            object-fit: cover;
            border-radius: 10px;
            margin-right: 15px;
        }
        .timestamp {
            font-size: 0.85rem;
            color: #6c757d;
        }
    </style>
</head>
<body>
    <h3 class="mb-4 text-primary"><i class="bi bi-bell-fill"></i> Notifications from Shops</h3>
""")

if notifications:
    for notif in notifications:
        message, timestamp, shop_name, shop_image, request_id = notif
        print(f"""
        <div class="card notif-card mb-3 p-3">
            <div class="d-flex align-items-center">
                <img src="/roadassist/images/{shop_image}" alt="Shop" class="shop-img">
                <div>
                    <h5 class="mb-1">{shop_name}</h5>
                    <p class="mb-1">{message}</p>
                    <div class="timestamp"><i class="bi bi-clock"></i> {timestamp}</div>
                   
                   
                </div>
            </div>
        </div>
        """)
else:
    print("""
    <div class="alert alert-info text-center">
        <i class="bi bi-info-circle"></i> No notifications yet.
    </div>
    """)

print("""
</body>
</html>
""")

cur.close()
con.close()
