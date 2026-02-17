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
  <title>Rejected shops | Admin</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" />
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet" />
</head>
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
  .modal-content {
    box-shadow: none;
  }

  .modal {
    padding: 0 !important;
    margin: 0 !important;
  }
  th{
  background-color:	#CD5C5C!important;
  }
  h2{
  text-align:center !important;
  color:#FF4500 !important;
</style>
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

    <div id="rejected" class="content-section active-section">
      <h2> Rejected -Mechanic shops</h2>
      <br>
      <div class="table-responsive">
       <table class="table table-bordered">

        <tr>
        <th>S.no</th>
        <th>Date of joined</th>
        <th> Owner Name</th>
        <th> Shop Name</th>
        <th>Email</th>
        <th>Phone</th>
        <th>View Details</th>
        <th>status</th>
        </tr>
       """)
q = """select * from mechanicshops where status="Rejected" """
cur.execute(q)
res = cur.fetchall()
for idx, i in enumerate(res, start=1):
    print("""
      <tr>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
      <td><button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#viewModal%s">View Details </button></td>
      <td style="color:red;">%s</td>

        </tr>
    """ % (idx, datetime.strptime(str(i[16]), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y"), i[1], i[10], i[17], i[4], i[0], i[15]))
for i in res:
    print("""
     <div class="modal fade" tabindex="-1" id="viewModal%s" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header" style="background-color:pink;">
            <h5 class="modal-title">MECHANIC SHOPS</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body p-4" >
           <img src="images/%s" alt="shop Image" class=" mb-3" style="width: 300px; height: 200px;margin-left:70px;">
            <h4 class="text-center fw-bold mb-3" style="color:orange;">%s</h4>
            <hr class="my-3" />
            <div class="owner">
            <h6 class="text-center fw-bold">Owner Details</h6>
             <img src="images/%s" alt="person Image" class=" mb-3" style="width: 150px; height: 150px;margin-left:140px;">
            <div class="row mb-2">
              <div class="col-5 fw-bold">reg_id:</div>
              <div class="col-7">%s</div>
            </div>
            <div class="row mb-2">
              <div class="col-5 fw-bold">Owner Name:</div>
              <div class="col-7">%s</div>
            </div>

             <div class="row mb-2">
              <div class="col-5 fw-bold">Dob:</div>
              <div class="col-7">%s</div>
            </div>

            <div class="row mb-2">
              <div class="col-5 fw-bold">Gender:</div>
              <div class="col-7">%s</div>
            </div>

            <div class="row mb-2">
              <div class="col-5 fw-bold">Email:</div>
              <div class="col-7">%s</div>
            </div>

            <div class="row mb-2">
              <div class="col-5 fw-bold">Phone No:</div>
              <div class="col-7">%s</div>
            </div>

            <div class="row mb-2">
              <div class="col-5 fw-bold">Address:</div>
              <div class="col-7">%s</div>
            </div>

            <div class="row mb-2">
              <div class="col-5 fw-bold">state:</div>
              <div class="col-7">%s</div>
            </div>
            <div class="row mb-2">
              <div class="col-5 fw-bold">city:</div>
              <div class="col-7">%s</div>
            </div>

            <div class="row mb-2">
              <div class="col-5 fw-bold">Adhar:</div>
              <div class="col-7"><button type="button" class="btn btn-outline-warning" data-bs-toggle="modal" data-bs-target="#adharModal%s" style="text-decoration-line:underline;">view</button></div>
            </div>
              </div>
              <div class="shop">
              <h6 class="text-center fw-bold">Shop Details</h6>
            <div class="row mb-2">
              <div class="col-5 fw-bold">Location:</div>
              <div class="col-7">%s</div>
            </div>
            <div class="row mb-2">
              <div class="col-5 fw-bold">Operating hours:</div>
              <div class="col-7">%s</div>
            </div>
            <div class="row mb-2">
              <div class="col-5 fw-bold">License proof:</div>
               <div class="col-7"><button type="button" class="btn btn-outline-warning" data-bs-toggle="modal" data-bs-target="#licenseModal%s" style="text-decoration-line:underline;">view</button></div>
            </div>
           </div>
          </div>
        </div>
      </div>
    </div>
    """ % (i[0], i[12], i[10], i[9], i[0], i[1], i[2], i[3], i[17], i[4], i[5], i[7], i[8], i[0], i[11], i[14], i[0]))
for i in res:
    print("""
    <div class="modal fade" tabindex="-1" id="adharModal%s" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header" style="background-color:blue;">
            <h5 class="modal-title">ADHAR - %s</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body " >
           <img src="images/%s" alt="person Image" width="300px" height="300px">
          </div>
          </div>
          </div>
          </div>
    """ % (i[0], i[1], i[6]))
for i in res:
    print("""
    <div class="modal fade" tabindex="-1" id="licenseModal%s" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header" style="background-color:blue;">
            <h5 class="modal-title">License - %s</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body " >
           <img src="images/%s" alt="person Image"width="300px" height="300px">
          </div>
          </div>
          </div>
          </div>
    """ % (i[0], i[1], i[13]))

print("""
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
