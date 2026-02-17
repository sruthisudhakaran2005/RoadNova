#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys
import cgi
import cgitb
import pymysql
import html

sys.stdout.reconfigure(encoding='utf-8')  # UTF-8 encoding for ₹ etc.

cgitb.enable()
print("Content-type: text/html\n")

# Get form data
form = cgi.FieldStorage()
shop_id = form.getvalue("id")

if not shop_id:
    print("<h3 style='color:red;'>Error: No Shop ID provided.</h3>")
    sys.exit()

# Initialize DB connection and cursor
try:
    con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
    cur = con.cursor()
except Exception as e:
    print(f"<h3 style='color:red;'>Database connection error: {html.escape(str(e))}</h3>")
    sys.exit()

# Get values from form
service_name = form.getvalue("service_name")
price = form.getvalue("price")

success = False

# Insert into DB only if all fields are present
if service_name and price:
    try:
        query = "INSERT INTO services (shop_id, service_name, price) VALUES (%s, %s, %s)"
        cur.execute(query, (shop_id, service_name, price))
        con.commit()
        success = True
    except Exception as e:
        print(f"<div class='alert alert-danger'>Database error: {html.escape(str(e))}</div>")

# Fetch shop details
try:
    query = "SELECT * FROM mechanicshops WHERE id=%s"
    cur.execute(query, (shop_id,))
    shop = cur.fetchone()
except Exception as e:
    print(f"<h3 style='color:red;'>Database query error: {html.escape(str(e))}</h3>")
    con.close()
    sys.exit()

if not shop:
    print("<h3 style='color:red;'>Error: Invalid Shop ID</h3>")
    con.close()
    sys.exit()

# Extract shop info safely escaping HTML
shop_name = html.escape(str(shop[10]))
owner_name = html.escape(str(shop[1]))
shop_img = html.escape(str(shop[12]))
email = html.escape(str(shop[17]))
phone = html.escape(str(shop[4]))
address = html.escape(str(shop[11]))
city = html.escape(str(shop[8]))
profile_img = html.escape(str(shop[9]))

# Success message HTML (only if insert was successful)
success_message = ""
if success:
    success_message = """
    <div class='alert alert-success text-center' id='success-message'>✅ Service added successfully!</div>
    <script>
      setTimeout(function() {
        var msg = document.getElementById('success-message');
        if (msg) {
          msg.style.display = 'none';
        }
        document.querySelector("form").reset();
      }, 2000);
    </script>
    """

print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Add Service | RoadNova</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">
  <style>
    .sidebar {{
      color: #050a30;
      min-height: 100vh;
    }}
    .sidebar .nav-link {{
      color: #050a30;
    }}
    .sidebar .nav-link:hover,
    .sidebar .nav-link.active {{
      background-color: #2e8bc0;
      color: white;
    }}
    @media (max-width: 768px) {{
      .sidebar {{
        position: fixed;
        top: 56px;
        left: -250px;
        width: 250px;
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
    .card {{
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
      border: none;
      border-radius: 10px;
    }}
    .form-control:focus {{
      box-shadow: none;
      border-color: #007bff;
    }}
    .btn-primary {{
      background-color: #2c3e50;
      border: none;
    }}
    .btn-primary:hover {{
      background-color: #34495e;
    }}
    .profile-button {{
  background-color: #2e8bc0;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 50px; /* This creates the capsule shape */
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.3s ease;
}}
.profile-button:hover {{
  background-color: #1a6a9b;
}}
.profile-button a {{
  color: white;
  text-decoration: none;
}}
  </style>
</head>
<body>
 <nav class="navbar navbar-dark bg-white" style="box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
      <div class="container-fluid">
        <button class="btn btn-outline-dark d-md-none me-2" id="toggleSidebar">
          <i class="bi bi-list"></i>
        </button>
        <span class="navbar-brand mb-0 h1" style="color:#050a30">RoadNova</span>
        <div class="d-flex align-items-center ms-auto gap-3">
         <button class="profile-button">
        <a href="owner.py?id={shop_id}" class="text-white text-decoration-none">
          <i class="bi bi-person-lines-fill me-1"></i>
          <span>Profile</span>
        </a>
      </button>

          <img src="images/{profile_img}" alt="mechanic Profile" class="rounded-circle" style="width:40px; height:40px; object-fit:cover;"/>
        </div>
      </div>
    </nav>

    <div class="container-fluid">
      <div class="row">
        <!-- Sidebar -->
        <nav class="col-md-3 col-lg-2 sidebar d-md-block p-0" id="sidebarMenu" style="background-color:#b1d4e0">
          <h5 class="text-center py-3">{shop_name}</h5>
          <ul class="nav flex-column">
            <li class="nav-item">
              <a class="nav-link active" href="mech.py?id={shop_id}">
                <i class="bi bi-speedometer2 me-2"></i>Dashboard
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" data-bs-toggle="collapse" href="#serviceSubmenu" role="button" aria-expanded="false" aria-controls="serviceSubmenu">
                <i class="bi bi-wrench-adjustable"></i> Services
              </a>
              <div class="collapse" id="serviceSubmenu">
                <ul class="nav flex-column ms-3">
                  <li class="nav-item"><a class="nav-link" href="add_service.py?id={shop_id}" onclick="showSection('addservice')"><i class="bi bi-bag-plus-fill"></i> Add services</a></li>
                  <li class="nav-item"><a class="nav-link" href="view_services.py?id={shop_id}" onclick="showSection('services')"><i class="bi bi-eye"></i> View services</a></li>
                </ul>
              </div>
            </li>
            <li class="nav-item">
              <a class="nav-link" data-bs-toggle="collapse" href="#employeeSubmenu" role="button" aria-expanded="false" aria-controls="employeeSubmenu">
                <i class="bi bi-tools me-2"></i>Employees
              </a>
              <div class="collapse" id="employeeSubmenu">
                <ul class="nav flex-column ms-3">
                  <li class="nav-item"><a class="nav-link" href="add.py?id={shop_id}" onclick="showSection('addMechanic')"><i class="bi bi-person-plus me-2"></i>Add Mechanic</a></li>
                  <li class="nav-item"><a class="nav-link" href="view.py?id={shop_id}"><i class="bi bi-people me-2"></i>View Mechanics</a></li>
                </ul>
              </div>
            </li>
            <li class="nav-item">
              <a class="nav-link" data-bs-toggle="collapse" href="#requestSubmenu" role="button" aria-expanded="false" aria-controls="requestSubmenu">
                <span><i class="bi bi-envelope me-2"></i>Requests</span>
              </a>
              <div class="collapse" id="requestSubmenu">
                <ul class="nav flex-column ms-3">
                  <li><a href="pending.py?id={shop_id}" class="nav-link"><i class="bi bi-card-list"></i> Pending</a></li>
                  <li><a href="current.py?id={shop_id}" class="nav-link"><i class="bi bi-journal-check"></i> Process</a></li>
                  <li><a href="completed.py?id={shop_id}" class="nav-link"><i class="bi bi-card-checklist"></i> Completed</a></li>
                   <li><a href="rejected_service.py?id={shop_id}" class="nav-link"><i class="bi bi-x-square"></i> Rejected</a></li>
                  <li><a href="cancelled_service.py?id={shop_id}" class="nav-link"><i class="bi bi-x-octagon"></i></i>cancelled</a></li>
                </ul>
              </div>
            </li>
            
            <li class="nav-item">
              <a class="nav-link" href="home.py"><i class="bi bi-box-arrow-right me-2"></i>Logout</a>
            </li>
          </ul>
        </nav>


    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-4">
      <div class="content-section">
        <div class="container mt-5">
          <div class="row justify-content-center">
            <div class="col-md-8">
              <div class="card p-4">
                <h3 class="text-center mb-4">Add New Service</h3>

                {success_message}

                <form method="post" action="add_service.py?id={shop_id}">
                  <div class="mb-3">
                      <label for="service_name" class="form-label">Service Name</label>
                      <input type="text" class="form-control" name="service_name" id="service_name" required >
                    </div>
                                      

                  <div class="mb-3">
                    <label for="price" class="form-label">Price (&#8377;)</label>
                    <input type="number" class="form-control" name="price" id="price" required placeholder="e.g. 1500">
                  </div>

                  <div class="d-grid">
                    <button type="submit" class="btn btn-primary">Add Service</button>
                  </div>
                </form>

              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js"></script>

<script>
  // Example sidebar toggle (optional)
  document.getElementById('toggleSidebar')?.addEventListener('click', function() {{
    document.getElementById('sidebarMenu').classList.toggle('show');
  }});
</script>

</body>
</html>
""")

con.close()
