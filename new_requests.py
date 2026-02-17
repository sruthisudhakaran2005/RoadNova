#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')
print("content-type:text/html \r\n\r\n")

import pymysql, cgi, cgitb, html, random, string
from datetime import datetime

cgitb.enable()

# DB connection
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
  <title>New Requests | Admin</title>
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

    .navbar-brand {{
      color:#c85250!important;
    }}

    .mainContent {{
      padding: 20px;
      color: #333;
    }}

    .modal-header {{
      background-color: #6a1b9a;
      color: white;
    }}

    .btn-close {{
      filter: invert(1); /* make close button white */
    }}

    thead {{
      background-color: maroon;
      color: white;
    }}

    h2 {{
      color: #5F9EA0;
    }}
    textarea.form-control {{
  border-radius: 8px;
  border-color: #dc3545;
  box-shadow: 0 0 4px rgba(220, 53, 69, 0.3);
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
      <nav class="col-md-3 col-lg-2 d-md-block sidebar" style="background-color:#fadcd9;color:#710019" id="sidebarMenu">
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
                <span><i class="bi-envelope"></i>Service Requests</span>
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

# Fetch pending shops only once
cur.execute("SELECT * FROM mechanicshops WHERE status='pending'")
pending_shops = cur.fetchall()

print("""
<div class="container mt-4 mb-5">
  <h2>Mechanic Shops - New Requests</h2>
  <div class="table-responsive mt-4">
    <table class="table table-bordered table-hover align-middle text-center">
      <thead>
        <tr>
          <th>S.NO</th>
          <th>Date Joined</th>
          <th>Owner Name</th>
          <th>Shop Name</th>
          <th>Email</th>
          <th>Phone</th>
          <th>View</th>
          <th>Authenticate</th>
        </tr>
      </thead>
      <tbody>
""")

q = """select * from mechanicshops where status='Pending' """
cur.execute(q)
res = cur.fetchall()
for idx, i in enumerate(res, 1):
    shop_id = i[0]
    owner_name = i[1]
    email = i[17]
    phone = i[4]
    address = i[5]
    shop_name = i[10]
    shop_address = i[11]
    shop_image = i[12]
    date_joined = i[16]
    dob = i[2]
    gender = i[3]
    owner_image = i[9]
    print(f"""
      <tr>
        <td>{idx}</td>
        <td>{date_joined.strftime('%d-%m-%Y')}</td>
        <td>{owner_name}</td>
        <td>{shop_name}</td>
        <td>{email}</td>
        <td>{phone}</td>
        <td><button class="btn btn-primary btn-sm" data-bs-toggle="modal" data-bs-target="#shopModal{shop_id}">View</button></td>
        <td><button class="btn btn-warning btn-sm" data-bs-toggle="modal" data-bs-target="#statusModal{shop_id}">Authenticate</button></td>
      </tr>
    """)

    print(f"""
    <div class="modal fade" id="shopModal{shop_id}" tabindex="-1" aria-labelledby="shopModalLabel{shop_id}" aria-hidden="true">
      <div class="modal-dialog modal-lg modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Mechanic Shop - {shop_name}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="text-center mb-3">
              <img src="images/{shop_image}" class="img-fluid rounded" alt="Shop Image" style="max-height:250px;" onerror="this.src='images/placeholder.png'">
              <h4 class="mt-2 text-primary">{shop_name}</h4>
            </div>
            <hr>
            <div class="row">
              <div class="col-md-6">
                <h6 class="section-title">Owner Details</h6>
                <div class="text-center mb-3">
                  <img src="images/{owner_image}" class="rounded-circle" alt="Owner Image" width="130" height="130" onerror="this.src='images/placeholder.png'">
                  <p class="fw-bold mt-2">{owner_name}</p>
                </div>
                <ul class="list-group list-group-flush">
                  <li class="list-group-item"><strong>Reg ID:</strong> {shop_id}</li>
                  <li class="list-group-item"><strong>DOB:</strong> {dob}</li>
                  <li class="list-group-item"><strong>Gender:</strong> {gender}</li>
                  <li class="list-group-item"><strong>Email:</strong> {email}</li>
                  <li class="list-group-item"><strong>Phone:</strong> {phone}</li>
                  <li class="list-group-item"><strong>Address:</strong> {address}</li>
                  <li class="list-group-item"><strong>State:</strong> {i[7]}</li>
                  <li class="list-group-item"><strong>City:</strong> {i[8]}</li>
                  <li class="list-group-item">
                    <strong>Adhar:</strong>
                    <button class="btn btn-outline-warning btn-sm" data-bs-toggle="modal" data-bs-target="#adharModal{shop_id}">View</button>
                  </li>
                </ul>
              </div>
              <div class="col-md-6">
                <h6 class="section-title">Shop Details</h6>
                <ul class="list-group list-group-flush">
                  <li class="list-group-item"><strong>Location:</strong> {shop_address}</li>
                  <li class="list-group-item"><strong>Operating Hours:</strong> {i[14]}</li>
                  <li class="list-group-item">
                    <strong>License Proof:</strong>
                    <button class="btn btn-outline-warning btn-sm" data-bs-toggle="modal" data-bs-target="#licenseModal{shop_id}">View</button>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    """)
    print(f"""
    <div class="modal fade" id="adharModal{shop_id}" tabindex="-1" aria-labelledby="adharModalLabel{shop_id}" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header bg-primary text-white">
            <h5 class="modal-title">Adhar Card - {owner_name}</h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body text-center">
            <img src="images/{i[6]}" alt="Adhar Card Image" class="img-fluid rounded" style="max-height: 400px;" onerror="this.src='images/placeholder.png'">
          </div>
        </div>
      </div>
    </div>
    """)

    print(f"""
    <div class="modal fade" id="licenseModal{shop_id}" tabindex="-1" aria-labelledby="licenseModalLabel{shop_id}" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header bg-primary text-white">
            <h5 class="modal-title">License Proof - {owner_name}</h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body text-center">
            <img src="images/{i[13]}" alt="License Image" class="img-fluid rounded" style="max-height: 400px;" onerror="this.src='images/placeholder.png'">
          </div>
        </div>
      </div>
    </div>
    """)


    print(f"""
        <div class="modal fade" id="statusModal%s"  aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title">Approve/Reject user</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body text-center">
                <h4>%s</h4><br><br>
               <button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#acceptModal%s"style="width:100px;text-decoration-line:none;">Approve</button>
               <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#rejectModal%s" style="width:100px;text-decoration-line:none;">Reject</button>
              </div>
            </div>
          </div>
        </div>
        """ %(shop_id, i[10], i[0], i[0]))
def generate_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

for i in res:
    user_number = i[0]
    u_password = owner_name[0:2] + phone[1:4] + generate_string(2)
    print("""
    <div class="modal fade" id="acceptModal%s"  aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">send password</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body text-center">
         <form method="post" class="form-container" action="approve_shop.py">
              <input type="hidden" name="shop_id" value="%s">
              <input type="text" name="password" value="%s">
              <div class="modal-footer">
                <input type="submit" name="update" class="btn btn-outline-primary" value="submit">
              </div>
            </form>

          </div>
        </div>
      </div>
    </div>
    """ % (i[0], i[0], u_password))

    print("""
    <div class="modal fade" id="rejectModal%s" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Reject User</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body text-center">
            <p>Are you sure you want to reject <strong>%s</strong>?</p>
            <form method="post" action="reject_shop.py">
              <input type="hidden" name="shop_id" value="%s">
             
              <input type="submit" name="reject" class="btn btn-danger w-100" value="Confirm Reject"style="width:100px;text-decoration-line:none;">
            </form>
          </div>
        </div>
      </div>
    </div>
    """ % (i[0], i[10], i[0]))

print("""
      </tbody>
    </table>
  </div>
</div>
""")



print("""
</main>
</div>
</div>

<div id="overlay" class.toggle('show');" onclick="toggleSidebar()"></div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
<script>
  function toggleSidebar() {
    const sidebar = document.getElementById('sidebarMenu');
    const overlay = document.getElementById('overlay');
    if (!sidebar || !overlay) {
      console.log("Sidebar or overlay missing:", sidebar, overlay);
      return;
    }
    sidebar.classList.toggle('show');
    overlay.classList.toggle('show');
  }

  function toggleRejectReason(shopId) {
    const container = document.getElementById(`rejectReasonContainer${shopId}`);
    container.classList.toggle('d-none');
  }
</script>

</body>
</html>
""")

cur.close()
con.close()