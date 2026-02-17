#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type: text/html\r\n\r\n")

import pymysql, cgi, cgitb
cgitb.enable()
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Database connection and form input
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
form = cgi.FieldStorage()
shop_id = form.getvalue("id")

# Fetch shop details
q = """SELECT * FROM mechanicshops WHERE id=%s"""
cur.execute(q, (shop_id,))
res = cur.fetchall()
con.close()

# Start HTML
print("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Rejected Requests | RoadNova</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" />
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet" />
  <style>
    .sidebar {
      color: #050a30!important;
      min-height: 100vh;
      width: 250px!important;
      background-color: #b1d4e0!important;
    }
    .sidebar .nav-link {
      color: #050a30!important;
    }
    .sidebar .nav-link:hover,
    .sidebar .nav-link.active {
      background-color: #2e8bc0!important;
      color: white;
    }
    @media (max-width: 768px) {
      .sidebar {
        position: fixed;
        top: 56px;
        left: -250px;
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
    .profile-button {
  background-color: #2e8bc0;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 50px; /* This creates the capsule shape */
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
.profile-button:hover {
  background-color: #1a6a9b;
}
.profile-button a {
  color: white;
  text-decoration: none;
}
  </style>
</head>
""")

# Loop to print shop-specific header
for i in res:
    profile_img = i[9]
    shop_name = i[10]
    print(f"""
    <body>
     <nav class="navbar navbar-dark bg-white shadow-sm">
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
          <nav class="col-md-3 col-lg-2 sidebar d-md-block p-0" id="sidebarMenu">
            <h5 class="text-center py-3">{shop_name}</h5>
            <ul class="nav flex-column">
              <li class="nav-item"><a class="nav-link active" href="mech.py?id={shop_id}"><i class="bi bi-speedometer2 me-2"></i>Dashboard</a></li>
              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="collapse" href="#serviceSubmenu" role="button" aria-expanded="false" aria-controls="serviceSubmenu">
                  <i class="bi bi-wrench-adjustable"></i> Services
                </a>
                <div class="collapse" id="serviceSubmenu">
                  <ul class="nav flex-column ms-3">
                    <li class="nav-item"><a class="nav-link" href="add_service.py?id={shop_id}"><i class="bi bi-bag-plus-fill"></i> Add services</a></li>
                    <li class="nav-item"><a class="nav-link" href="view_services.py?id={shop_id}"><i class="bi bi-eye"></i> View services</a></li>
                  </ul>
                </div>
              </li>
              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="collapse" href="#employeeSubmenu" role="button" aria-expanded="false" aria-controls="employeeSubmenu">
                  <i class="bi bi-tools me-2"></i>Employees
                </a>
                <div class="collapse" id="employeeSubmenu">
                  <ul class="nav flex-column ms-3">
                    <li class="nav-item"><a class="nav-link" href="add.py?id={shop_id}"><i class="bi bi-person-plus me-2"></i>Add Mechanic</a></li>
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
              <li class="nav-item"><a class="nav-link" href="home.py"><i class="bi bi-box-arrow-right me-2"></i>Logout</a></li>
            </ul>
          </nav>
           <div id="sidebarOverlay" style="display:none; position: fixed; top: 0; left: 0; width:100%; height:100%; background: rgba(0,0,0,0.5); z-index:1049;"></div>

          <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-4">
    """)
# Table start
print("""
<div class="container py-4">
<h2 style="color:red;text-align:center">Rejected Requests</h2>
  <div class="table-responsive">
    <table class="table table-striped table-hover table-bordered align-middle">
      <thead class="table-dark">
        <tr>
          <th>S.NO</th>
          <th>Problem</th>
          <th>Date</th>
          <th>Customer Name</th>
          <th>Customer Details</th>
        </tr>
      </thead>
      <tbody>
""")

# Fetch rejected requests
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
cur.execute("""
  SELECT r.request_id, r.problem_type, r.request_date, r.status,
         u.name, u.phone, u.email, u.address
  FROM service_requests r
  JOIN users u ON r.user_id = u.user_id
  WHERE r.shop_id = %s AND r.status = 'Rejected'
""", (shop_id,))
rows = cur.fetchall()

sn = 1
for req_id, prob, req_date, status, name, phone, email, addr in rows:
    modal_id = f"customerModal{req_id}"

    print(f"""
    <tr>
      <td>{sn}</td>
      <td>{prob}</td>
      <td>{req_date.strftime('%d-%m-%Y')}</td>
      <td>{name}</td>
      <td>
        <button type="button" class="btn btn-info btn-sm" data-bs-toggle="modal" data-bs-target="#{modal_id}">
          View Details
        </button>
      </td>
    </tr>

    <!-- Customer Modal -->
    <div class="modal fade" id="{modal_id}" tabindex="-1" aria-labelledby="{modal_id}Label" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="{modal_id}Label">Customer Details </h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Phone:</strong> {phone}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Address:</strong> {addr}</p>
            <p><strong>Status:</strong> <span class="badge bg-danger">{status}</span></p>
          </div>
          <div class="modal-footer">
            <button class="btn btn-secondary btn-sm" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
    """)

    sn += 1

if not rows:
    print('<tr><td colspan="5" class="text-center">No rejected requests found.</td></tr>')

# Close HTML table
print("""
      </tbody>
    </table>
  </div>
</div>
""")

print("""
</main>
<script>
     const toggleBtn = document.getElementById('toggleSidebar');
  const sidebar = document.getElementById('sidebarMenu');
  const overlay = document.getElementById('sidebarOverlay');


  toggleBtn.addEventListener('click', () => {
    sidebar.classList.toggle('show');
    overlay.classList.toggle('show');
  });

  overlay.addEventListener('click', () => {
    sidebar.classList.remove('show');
    overlay.classList.remove('show');
  });
            </script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")

con.close()
