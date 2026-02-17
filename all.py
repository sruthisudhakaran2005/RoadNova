#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, string, random, smtplib

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
form = cgi.FieldStorage()
print("""
 <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Admin Dashboard</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" />
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet" />
</head>
<style>
html, body {
    margin: 0;
    padding: 0;
    background-color: transparent;
  }

  .modal-content {
    box-shadow: none;
  }

  .modal {
    padding: 0 !important;
    margin: 0 !important;
  }
</style>
<body>
""")

print("""

    <div id="all" class="content-section">
      <h2>Mechanic shops</h2>
      <br>
      <div class="table-responsive">
       <table class="table table-bordered">

        <tr>
        <th> ID</th>
        <th> Owner Name</th>
        <th> Shop Name</th>
        <th>Email</th>
        <th>Phone</th>
        <th>Date of joined</th>
        <th>View Details</th>
        <th>status</th>
        </tr>
       """)
q = """select * from mechanicshops"""
cur.execute(q)
res = cur.fetchall()
for i in res:
    print("""
      <tr>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
      <td> <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#viewModal%s">View Details </button></td>
      <td>%s</td>
        
        </tr>
    """%(i[0], i[1], i[10], i[17], i[4], i[16], i[0], i[15]))
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
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>

""")
