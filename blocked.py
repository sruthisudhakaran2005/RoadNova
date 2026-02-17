#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
print("content-type:text/html\r\n\r\n")
import pymysql, cgi, cgitb
from datetime import datetime

cgitb.enable()
form = cgi.FieldStorage()

con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
cur.execute("SELECT image FROM admin WHERE id=1")
result = cur.fetchone()
if result:
    profile = result[0]
else:
    profile = "default.jpg"
cur.execute("SELECT image FROM admin WHERE id=1")
result = cur.fetchone()
if result and result[0]:
    profile = result[0]
else:
    profile = "default.jpg"
if "unblock" in form:
    shop_id = form.getvalue("unblock")
    cur.execute("UPDATE mechanicshops SET status='Approved' WHERE id=%s", (shop_id,))
    con.commit()

# Fetch blocked shops
cur.execute("SELECT * FROM mechanicshops WHERE status='Blocked'")
shops = cur.fetchall()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Blocked Shops | Admin</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" />
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet" />
  <style>
     body {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    .sidebar {
      min-height: 100vh;
      max-height:auto;
    }

    .sidebar .nav-link {
      color: #710019;
    }

    .sidebar .nav-link.active,
    .sidebar .nav-link:hover {
      background-color:#f7bec0;
      color:black;
    }

    .card {
      margin-bottom: 20px;
    }

    .content-section {
      display: none;
    }

    .active-section {
      display: block;
    }

    @media (max-width: 768px) {
      .sidebar {
        position: fixed;
        top: 56px;
        left: -200px;
        width: 200px!important;
        z-index: 1031;
        transition: left 0.3s ease-in-out;
      }

      .sidebar.show {
        left: 0;
      }
      .content-section {
  display: none;
}


      .overlay {
        display: none;
        position: fixed;
        top: 56px;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: 1030;
      }

      .overlay.show {
        display: block;
      }
    }
    @media (max-width: 768px) {
  form label {
    margin-left: 0 !important;
    font-size: medium !important;
    display: block;
    margin-bottom: 10px;
  }
  form select {
    width:200px!important;
    max-width: none !important;
  }
}
.navbar-brand{
color:#c85250!important;
}

 }
  </style>
</head>
<body>
""")
print("""
  <nav class="navbar navbar-dark bg-white fixed-top" style="box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
    <div class="container-fluid">
      <button class="btn btn-outline-dark d-md-none me-2" type="button" onclick="toggleSidebar()" style="color:5F9EA0">
        <i class="bi bi-list"></i>
      </button>
      <span class="navbar-brand mb-0 h1">RoadNova</span>
      <div class="d-flex align-items-center ms-auto">
        <img src="images/%s" alt="Admin Profile" class="rounded-circle" style="width:40px; height:40px; object-fit:cover;"/>
      </div>
    </div>
  </nav>
""" % (profile))

print("""
<div class="container-fluid" style="padding-top: 56px;"> <!-- padding for fixed navbar -->
  <div class="row">

    <nav class="col-md-3 col-lg-2 d-md-block sidebar collapse" style="background-color:#fadcd9;color:#710019" id="sidebarMenu">
      <div class="position-sticky pt-3 text-white">
        <h5 class="px-3 mb-3">Admin Dashboard</h5>
        <ul class="nav flex-column">
          <li class="nav-item">
            <a class="nav-link active" href="admin.py">
              <i class="bi bi-speedometer2 me-2"></i>Dashboard
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse" href="#usersSubmenu" role="button" aria-expanded="false">
              <span><i class="bi bi-people me-2"></i>Users</span>
              <i class="bi bi-chevron-down small"></i>
            </a>
            <div class="collapse" id="usersSubmenu">
              <ul class="nav flex-column ms-3">
                <li><a href="viewuser.py" class="nav-link"><i class="bi bi-person me-2"></i>View Users</a></li>
              </ul>
            </div>
          </li>
          <li class="nav-item">
            <a class="nav-link d-flex justify-content-between align-items-center"  data-bs-toggle="collapse"  href="#mechanicsSubmenu" role="button" aria-expanded="false">
              <span><i class="bi bi-tools me-2"></i>Shop owners</span>
              <i class="bi bi-chevron-down small"></i>
            </a>
            <div class="collapse" id="mechanicsSubmenu">
              <ul class="nav flex-column ms-3">
                <li><a href="new_requests.py" class="nav-link"><i class="bi bi-person me-2"></i>New Requests</a></li>
                <li><a href="approved.py" class="nav-link"><i class="bi bi-person me-2"></i>Approved shops</a></li>
                <li><a href="rejected.py" class="nav-link"><i class="bi bi-person me-2"></i>Rejected shops</a></li>
                <li><a href="blocked.py" class="nav-link"><i class="bi bi-person me-2"></i>Blocked shops</a></li>
              </ul>
            </div>
          </li>
          <li class="nav-item">
            <a class="nav-link d-flex justify-content-between align-items-center" href="all_requests.py">
              <span><i class="bi-envelope"></i>Service Requests</span>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link d-flex justify-content-between align-items-center"  href="home.py" role="button" aria-expanded="false">
              <span><i class="bi bi-gear me-2"></i>Logout</span>
            </a>
          </li>
        </ul>
      </div>
    </nav>

    <main id="mainContent" class="col-md-9 col-lg-10 ms-sm-auto px-md-4" style="padding-top: 20px;">
""")

print("""
<div class="container mt-4">
  <h2 class="text-center text-danger mb-4">Blocked Mechanic Shops</h2>
  <div class="table-responsive">
    <table class="table table-bordered table-striped text-center">
      <thead>
        <tr>
          <th>S.NO</th>
          <th>Shop Name</th>
          <th>Owner</th>
          <th>Email</th>
          <th>Phone</th>
          <th>Joined Date</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
""")

for idx, shop in enumerate(shops, start=1):
    shop_id = shop[0]
    owner = shop[1]
    email = shop[17]
    phone = shop[4]
    shop_name = shop[10]
    joined_date = datetime.strptime(str(shop[16]), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
    print(f"""
      <tr>
        <td>{idx}</td>
        <td>{shop_name}</td>
        <td>{owner}</td>
        <td>{email}</td>
        <td>{phone}</td>
        <td>{joined_date}</td>
        <td>
          <form method="post">
            <input type="hidden" name="unblock" value="{shop_id}">
            <button type="submit" class="btn btn-success btn-sm btn-unblock">✅ Unblock</button>
          </form>
        </td>
      </tr>
    """)

if not shops:
    print("""
      <tr>
        <td colspan="7" class="text-muted">No blocked shops found.</td>
      </tr>
    """)

print("""
      </tbody>
    </table>
  </div>
</div>
</main>
</div>
</div>
<script>

  function toggleSidebar() {
    const sidebar = document.getElementById('sidebarMenu');
    sidebar.classList.toggle('show');
  }
</script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")

cur.close()
con.close()
