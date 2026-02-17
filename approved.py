#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
print("content-type:text/html \r\n\r\n")

import pymysql, cgi, cgitb
from datetime import datetime

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
form = cgi.FieldStorage()

cur.execute("SELECT image FROM admin WHERE id=1")
result = cur.fetchone()
if result and result[0]:
    profile = result[0]
else:
    profile = "default.jpg"

print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Approved Mechanic Shops | Admin</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" />
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet" />
  <style>
    body {{
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}

    .sidebar {{
      min-height: 100vh;
      max-height: auto;
    }}

    .sidebar .nav-link {{
      color: #710019;
    }}

    .sidebar .nav-link.active,
    .sidebar .nav-link:hover {{
      background-color: #f7bec0;
      color: black;
    }}

    .card {{
      margin-bottom: 20px;
    }}

    .content-section {{
      display: none;
    }}

    .active-section {{
      display: block;
    }}

    @media (max-width: 768px) {{
      .sidebar {{
        position: fixed;
        top: 56px;
        left: -200px;
        width: 200px !important;
        z-index: 1031;
        transition: left 0.3s ease-in-out;
        /* ensure hidden by default on small */
      }}

      .sidebar.show {{
        left: 0;
      }}

      .overlay {{
        display: none;
        position: fixed;
        top: 56px;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: 1030;
      }}

      .overlay.show {{
        display: block;
      }}
    }}

    @media (max-width: 768px) {{
      form label {{
        margin-left: 0 !important;
        font-size: medium !important;
        display: block;
        margin-bottom: 10px;
      }}
      form select {{
        width:200px !important;
        max-width: none !important;
      }}
    }}

    .navbar-brand{{ color:#c85250!important; }}

    .mainContent{{
      padding: 20px;
      color: #333;
      background-color: #f5f5f5;
    }}

    h2 {{
      text-align: center;
      color: #4a148c;
      margin-top: 20px;
    }}
    .table th {{
      background-color: #6a1b9a;
      color: white;
    }}
    .btn-outline-warning {{
      text-decoration: underline;
    }}
    .modal-header {{
      background-color: #6a1b9a;
      color: white;
    }}
    .btn-close {{
      filter: invert(1); /* make it white */
    }}
    img {{
      object-fit: cover;
    }}
    .section-title {{
      color: #333;
      margin: 10px 0;
      border-bottom: 1px solid #ccc;
      padding-bottom: 5px;
    }}
  </style>
</head>
<body>
  <nav class="navbar navbar-dark bg-white fixed-top" style="box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
    <div class="container-fluid">
      <button class="btn btn-outline-dark d-md-none me-2" type="button" onclick="toggleSidebar()" style="color:#5F9EA0;">
        <i class="bi bi-list"></i>
      </button>
      <span class="navbar-brand mb-0 h1">RoadNova</span>
      <div class="d-flex align-items-center ms-auto">
        <img src="images/{profile}" alt="Admin Profile" class="rounded-circle" style="width:40px; height:40px; object-fit:cover;"/>
      </div>
    </div>
  </nav>

  <div class="container-fluid" style="padding-top: 56px;">
    <div class="row">
      <nav class="col-md-3 col-lg-2 d-md-block sidebar" style="background-color:#fadcd9; color:#710019;" id="sidebarMenu">
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
              <a class="nav-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse" href="#mechanicsSubmenu" role="button" aria-expanded="false">
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
                <span><i class="bi bi-envelope"></i>Service Requests</span>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link d-flex justify-content-between align-items-center" href="home.py">
                <span><i class="bi bi-gear me-2"></i>Logout</span>
              </a>
            </li>
          </ul>
        </div>
      </nav>

      <main id="mainContent" class="col-md-9 col-lg-10 ms-sm-auto px-md-4" style="padding-top: 20px;">
""")

# The rest of your table/modals code remains the same
# Print table header
print("""
<div class="container mt-4 mb-5">
  <h2>Approved Mechanic Shops</h2>
  <div class="table-responsive mt-4">
    <table class="table table-bordered table-hover text-center align-middle">
      <thead>
        <tr>
          <th>S.NO</th>
          <th>Date Joined</th>
          <th>Owner Name</th>
          <th>Shop Name</th>
          <th>Email</th>
          <th>Phone</th>
          <th>View</th>
          <th>Status</th>
          <th>Block</th>
        </tr>
      </thead>
      <tbody>
""")

q = """SELECT * FROM mechanicshops WHERE status='Approved'"""
cur.execute(q)
res = cur.fetchall()

for idx, i in enumerate(res, start=1):
    # assuming i[16] is datetime
    date_joined = datetime.strptime(str(i[16]), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
    print(f"""
        <tr>
          <td>{idx}</td>
          <td>{date_joined}</td>
          <td>{i[1]}</td>
          <td>{i[10]}</td>
          <td>{i[17]}</td>
          <td>{i[4]}</td>
          <td>
            <button class="btn btn-primary btn-sm" data-bs-toggle="modal" data-bs-target="#viewModal{i[0]}">
              View
            </button>
          </td>
          <td><span class="badge bg-success">{i[15]}</span></td>
          <td>
            <form method="post" action="block_shop.py" onsubmit="return confirm('Are you sure you want to block this shop?');">
              <input type="hidden" name="shop_id" value="{i[0]}">
              <button type="submit" class="btn btn-danger btn-sm">🚫 Block</button>
            </form>
          </td>
        </tr>
    """)

print("</tbody></table></div></div>")

# Print the view modals, adhar, license etc. (same as before)
for i in res:
    print(f"""
<div class="modal fade" id="viewModal{i[0]}" tabindex="-1" aria-labelledby="viewModalLabel{i[0]}" aria-hidden="true">
  <div class="modal-dialog modal-lg modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Mechanic Shop - {i[10]}</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <div class="text-center mb-3">
          <img src="images/{i[12]}" class="img-fluid rounded" alt="Shop Image" style="max-height:250px;" onerror="this.src='images/placeholder.png'">
          <h4 class="mt-2 text-primary">{i[10]}</h4>
        </div>
        <hr>
        <div class="row">
          <div class="col-md-6">
            <h6 class="section-title">Owner Details</h6>
            <div class="text-center mb-3">
              <img src="images/{i[9]}" class="rounded-circle" alt="Owner Image" width="130" height="130" onerror="this.src='images/placeholder.png'">
              <p class="fw-bold mt-2">{i[1]}</p>
            </div>
            <ul class="list-group list-group-flush">
              <li class="list-group-item"><strong>Reg ID:</strong> {i[0]}</li>
              <li class="list-group-item"><strong>DOB:</strong> {i[2]}</li>
              <li class="list-group-item"><strong>Gender:</strong> {i[3]}</li>
              <li class="list-group-item"><strong>Email:</strong> {i[17]}</li>
              <li class="list-group-item"><strong>Phone:</strong> {i[4]}</li>
              <li class="list-group-item"><strong>Address:</strong> {i[5]}</li>
              <li class="list-group-item"><strong>State:</strong> {i[7]}</li>
              <li class="list-group-item"><strong>City:</strong> {i[8]}</li>
              <li class="list-group-item">
                <strong>Adhar:</strong>
                <button class="btn btn-outline-warning btn-sm" data-bs-toggle="modal" data-bs-target="#adharModal{i[0]}">View</button>
              </li>
            </ul>
          </div>
          <div class="col-md-6">
            <h6 class="section-title">Shop Details</h6>
            <ul class="list-group list-group-flush">
              <li class="list-group-item"><strong>Location:</strong> {i[11]}</li>
              <li class="list-group-item"><strong>Operating Hours:</strong> {i[14]}</li>
              <li class="list-group-item">
                <strong>License Proof:</strong>
                <button class="btn btn-outline-warning btn-sm" data-bs-toggle="modal" data-bs-target="#licenseModal{i[0]}">View</button>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
""")

for i in res:
    print(f"""
<div class="modal fade" id="adharModal{i[0]}" tabindex="-1" aria-labelledby="adharModalLabel{i[0]}" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header bg-primary text-white">
        <h5 class="modal-title">Adhar Card - {i[1]}</h5>
        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body text-center">
        <img src="images/{i[6]}" alt="Adhar Card Image" class="img-fluid rounded" style="max-height: 400px;" onerror="this.src='images/placeholder.png'">
      </div>
    </div>
  </div>
</div>
""")

for i in res:
    print(f"""
<div class="modal fade" id="licenseModal{i[0]}" tabindex="-1" aria-labelledby="licenseModalLabel{i[0]}" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header bg-primary text-white">
        <h5 class="modal-title">License Proof - {i[1]}</h5>
        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body text-center">
        <img src="images/{i[13]}" alt="License Image" class="img-fluid rounded" style="max-height: 400px;" onerror="this.src='images/placeholder.png'">
      </div>
    </div>
  </div>
</div>
""")

# End page, including overlay and script
print("""
</main>
</div>
</div>

<!-- Overlay outside sidebar -->
<div id="overlay" class="overlay" onclick="toggleSidebar()"></div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
<script>
  function toggleSidebar() {
    console.log("toggleSidebar called");
    const sidebar = document.getElementById('sidebarMenu');
    const overlay = document.getElementById('overlay');
    if (!sidebar || !overlay) {
      console.error("Sidebar or overlay element is missing", sidebar, overlay);
      return;
    }
    sidebar.classList.toggle('show');
    overlay.classList.toggle('show');
  }
</script>
</body>
</html>
""")

cur.close()
con.close()
