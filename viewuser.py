#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb
from datetime import datetime

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
form = cgi.FieldStorage()
cur.execute("SELECT image FROM admin WHERE id=1")
result = cur.fetchone()
if result:
    profile = result[0]
else:
    profile = "default.jpg"
print("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Admin Dashboard</title>
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
  .mainContent{

      padding: 20px;
      color: #333;
      }

    mainContent {
      background: #f8f9fa;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

    }
    h2 {
      color: #ff5722;
      font-weight: 700;
      margin-top: 30px;
      margin-bottom: 20px;
      text-align: center;
    }
    .table-responsive {
      box-shadow: 0 0 15px rgba(0,0,0,0.1);
      border-radius: 10px;
      background: #fff;
      padding: 15px;
    }
    table {
      width: 100% !important;
      border-collapse: separate;
      border-spacing: 0 10px;
      overflow-x: auto;
    }
    th {
      font-size: 1.1rem;
      background-color: #ff5722;
      color:maroon;
      border: none !important;
      padding: 12px 15px;
      border-radius: 8px 8px 0 0;
      text-align: center;
    }
    td {
      background: #fff;
      padding: 12px 15px;
      vertical-align: middle;
      border-bottom: 10px solid transparent;
      text-align: center;
      font-weight: 500;
      color: #444;
      border-radius: 8px;
      box-shadow: 0 1px 3px rgb(0 0 0 / 0.1);
    }
    tr:hover td {
      background-color: #ffece6;
      cursor: pointer;
      color: #d84315;
      box-shadow: 0 3px 8px rgba(255, 87, 34, 0.3);
    }
    .btn-primary {
      background-color: #ff5722;
      border: none;
    }
    .btn-primary:hover {
      background-color: #e64a19;
    }
    /* Modal Styling */
    .modal-content {
      border-radius: 15px;
      box-shadow: 0 6px 20px rgb(255 87 34 / 0.4);
      border: none;
    }
    .modal-header {
      background-color: #ff7043;
      color: white;
      border-top-left-radius: 15px;
      border-top-right-radius: 15px;
      border-bottom: none;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .modal-title {
      font-weight: 700;
      font-size: 1.5rem;
    }
    .btn-close {
      filter: brightness(0) invert(1);
    }
    .modal-body {
      padding: 2rem;
      background: #fff3e0;
      border-bottom-left-radius: 15px;
      border-bottom-right-radius: 15px;
      color: #5d4037;
    }
    .modal-body h4 {
      color: #bf360c;
      margin-bottom: 20px;
      font-weight: 700;
    }
    .row.mb-3 > .col-5 {
      font-weight: 600;
      color: #d84315;
    }
    @media (max-width: 575.98px) {
      th, td {
        font-size: 0.9rem;
        padding: 10px 8px;
      }
      .modal-body {
        padding: 1rem;
      }
      .modal-title {
        font-size: 1.25rem;
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
  <div class="container">
    <h2>User Management</h2>
    <div class="table-responsive">
      <table class="table table-bordered align-middle">
        <thead>
          <tr>
            <th>S.NO</th>
            <th>Date Joined</th>
            <th>Full Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Address</th>
          </tr>
        </thead>
        <tbody>
""")

q = """SELECT * FROM users"""
cur.execute(q)
res = cur.fetchall()
for idx, i in enumerate(res, start=1):
    date_joined = datetime.strptime(str(i[8]), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
    print(f"""
      <tr>
        <td>{idx}</td>
        <td>{date_joined}</td>
        <td>{i[1]}</td>
        <td>{i[3]}</td>
        <td>{i[4]}</td>
        <td style="text-align:left">{i[5]}</td>
      </tr>
    """)

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

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
<script>
  function toggleSidebar() {
    const sidebar = document.getElementById('sidebarMenu');
    sidebar.classList.toggle('show');
  }
</script>
</body>
</html>
""")
con.close()
