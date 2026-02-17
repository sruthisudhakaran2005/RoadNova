#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe

print("Content-Type: text/html\r\n\r\n")

import pymysql, cgi, cgitb, html, sys
from datetime import datetime
sys.stdout.reconfigure(encoding='utf-8')
cgitb.enable()


con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()



form = cgi.FieldStorage()
shop_id = form.getvalue("id")

try:
    shop_id = int(shop_id)
except (TypeError, ValueError):
    print("<h3>Invalid shop ID</h3>")
    exit()

# Fetch requests
cur.execute("""
SELECT r.request_id, r.user_id, r.shop_id, r.problem_type, r.location, 
       r.request_date ,  r.vehicle_brand,r.vehicle_type, r.reg_no, 
       u.name, u.phone, u.email
FROM service_requests r
JOIN users u ON r.user_id = u.user_id
WHERE r.shop_id = %s AND r.status = 'Pending'
ORDER BY r.request_date DESC
""", (shop_id,))
requests = cur.fetchall()
q = """ select vehicle_brand from service_requests requests where shop_id='%s' """%(shop_id)
cur.execute(q)
r = cur.fetchone()
if r is not None:
    vehicle_brand = r[0]
# Fetch mechanics
cur.execute("SELECT mech_id, name FROM mechanics WHERE shop_id=%s", (shop_id,))
mechanics = cur.fetchall()

# Fetch services
cur.execute("SELECT service_id, service_name, price FROM services")
services = cur.fetchall()

q = """SELECT * FROM mechanicshops WHERE id=%s"""
cur.execute(q, (shop_id,))

res = cur.fetchall()
con.close()

for i in res:
    profile_img = i[9]
    shop_name = i[10]
    print(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Pending Service Requests | RoadNova</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" />

      <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet" />
      <style>
        /* Sidebar fixed width */
        .sidebar {{
          color: #050a30;
          min-height: 100vh;
          width: 250px;
          max-width: 250px;
          background-color: #b1d4e0;
        }}
        .sidebar .nav-link {{
          color: #050a30;
        }}
        .sidebar .nav-link:hover,
        .sidebar .nav-link.active {{
          background-color: #2e8bc0;
          color: white;
        }}

        /* Responsive sidebar for small screens */
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

        /* Limit main container width */
        main > .container {{
          max-width: 1200px;
        }}

        /* Table cell truncation */
        table td, table th {{
          white-space: nowrap;
          max-width: 150px;
          overflow: hidden;
          text-overflow: ellipsis;
        }}

        /* Allow wrapping on smaller screens */
        @media (max-width: 768px) {{
          table td, table th {{
            white-space: normal;
            max-width: none;
          }}
        }}
        .sidebar {{
    background-color: #b1d4e0;
    color: #050a30;
    min-height: 100vh;
    width: 250px;
  }}

  .sidebar .nav-link {{
    color: #050a30;
  }}

  .sidebar .nav-link:hover,
  .sidebar .nav-link.active {{
    background-color: #2e8bc0;
    color: white;
  }}

  /* ✅ Mobile sidebar behavior */
  @media (max-width: 768px) {{
    .sidebar {{
      position: fixed;
      top: 56px; /* height of navbar */
      left: -250px;
      width: 250px;
      height: calc(100vh - 56px);
      z-index: 1050;
      transition: left 0.3s ease-in-out;
      box-shadow: 2px 0 5px rgba(0, 0, 0, 0.3);
    }}

    .sidebar.show {{
      left: 0;
    }}

    #sidebarOverlay {{
      display: none;
      position: fixed;
      top: 56px;
      left: 0;
      width: 100%;
      height: calc(100vh - 56px);
      background-color: rgba(0, 0, 0, 0.5);
      z-index: 1049;
    }}

    #sidebarOverlay.show {{
      display: block;
    }}
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
     <nav class="navbar navbar-dark bg-white shadow-sm">
  <div class="container-fluid d-flex align-items-center">
    
    <!-- Sidebar toggle button FIRST -->
    <button class="btn btn-outline-dark d-md-none me-2" id="toggleSidebar">
      <i class="bi bi-list"></i>
    </button>

    <!-- Brand name -->
    <span class="navbar-brand mb-0 h1 flex-grow-1" style="color:#050a30">RoadNova</span>
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
     <div id="sidebarOverlay"></div>
      <div class="container-fluid">
        <div class="row">
          <!-- Sidebar -->
          <nav class="col-md-3 col-lg-2 sidebar d-md-block p-0" id="sidebarMenu">
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
                    <li><a href="rejected_service.py?id={shop_id}" class="nav-link"><i class="bi bi-card-checklist"></i> Rejected</a></li>
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
            <div class="container py-5">
              <h2 class="mb-4 text-center">🚗 Pending Service Requests</h2>
              <div class="table-responsive">
                <table class="table table-hover table-bordered table-striped align-middle shadow-sm">
                  <thead class="table-dark">
                    <tr>
                      <th>S.NO</th>
                      <th>Problem</th>
                      <th>Date</th>
                      <th>Customer</th>
                      <th>Location</th>
                      <th>Details</th>
                      <th>Actions</th>
                    </tr>
                  </thead>
                  <tbody>
    """)

    if requests:
        for idx, req in enumerate(requests, start=1):
            req_id = req[0]
            problem = req[3]
            req_time = req[5]
            username = req[9]
            contact = req[10]
            location = req[4]
            email = req[11]
            vehicle_type = req[7]

            reg_no = req[8]
            # Row
            print(f"""
            <tr>
              <td>{idx}</td>
              <td>{problem}</td>
              <td>{req_time.strftime('%b %d, %Y %I:%M %p')}</td>
              <td>{username}</td>
              <td>{location}</td>
              <td>
                <button class="btn btn-info btn-sm" data-bs-toggle="modal" data-bs-target="#viewModal{req_id}">👁️ View</button>
              </td>
              <td>
                <button class="btn btn-success btn-sm" data-bs-toggle="modal" data-bs-target="#approveModal{req_id}">✅ Approve</button>
               <button class="btn btn-danger btn-sm" data-bs-toggle="modal" data-bs-target="#rejectModal{req_id}">
                  ❌ Reject
                </button>
              </td>
            </tr>
            """)

            # View Modal
            print(f"""
            <div class="modal fade" id="viewModal{req_id}" tabindex="-1">
              <div class="modal-dialog modal-lg modal-dialog-centered">
                <div class="modal-content">
                  <div class="modal-header bg-primary text-white">
                    <h5 class="modal-title">Customer Details </h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                  </div>
                  <div class="modal-body">
                  <div class="row">
                  <div class="col-md-6">
                    <p><strong>Customer Name:</strong> {username}</p>
                    <p><strong>Current Location:</strong> {location}</p>
                    <p><strong>Phone Number:</strong> {contact}</p>
                    <p><strong>Email id:</strong> {email}</p>
                    </div>
                    <div class="col-md-6">
                    <p><strong>Problem:</strong> {problem}</p>
                     <p><strong>Vehicle Type:</strong> {vehicle_type}</p>
                     <p><strong>Vehicle Brand:</strong> {vehicle_brand}</p>
                     <p><strong>Registration Number:</strong> {reg_no}</p>
                    <p><strong>Date:</strong> {req_time.strftime('%b %d, %Y %I:%M %p')}</p>
                  </div>
                  </div>
                  </div>
                  <div class="modal-footer">
                    <button class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                  </div>
                </div>
              </div>
            </div>
            """)

            # Approve Modal
            print(f"""
            <div class="modal fade" id="approveModal{req_id}" tabindex="-1">
              <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                  <form method="post" action="approve_service.py">
                    <div class="modal-header bg-success text-white">
                      <h5 class="modal-title">Approve Request </h5>
                      <button class="btn-close" data-bs-dismiss="modal"></button>
                    </div>
                    <div class="modal-body">
                      <input type="hidden" name="request_id" value="{req_id}">
                      <input type="hidden" name="status" value="Approved">
                      <input type="hidden" name="shop_id" value="{shop_id}">
                      <input type="hidden" name="email" value="{email}">

                      <div class="mb-3">
                        <label class="form-label">Assign Mechanic</label>
                        <select name="mechanic_id" class="form-select" required>
                          <option value="">Select Mechanic</option>
            """)
            for mech_id, mech_name in mechanics:
                print(f'<option value="{mech_id}">{html.escape(mech_name)}</option>')

            print(f"""
                        </select>
                      </div>

                      <div class="mb-3">
            """)
            con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
            cur = con.cursor()
            cur.execute("SELECT service_id, price FROM services WHERE service_name = %s AND shop_id = %s",
                        (problem, shop_id))
            matched_service = cur.fetchone()
            con.close()

            if matched_service:
                service_id, price = matched_service
                print(f"""
                  <input type="hidden" name="service_id" value="{service_id}">
                  <div class="mb-3">
                    <label class="form-label">Service Price (Auto)</label>
                    <input type="text" class="form-control" value="₹{price}" readonly>
                  </div>
                """)
            else:
                print(f"""
                  <div class="mb-3">
                    <label class="form-label">Service Amount (Manual)</label>
                    <input type="number" name="manual_price" class="form-control" placeholder="Enter price manually" required>
                  </div>
                """)

            print(f"""
                      </div>

                      <div class="mb-3">
                        <label class="form-label">Message to Customer</label>
                        <textarea name="notification_message" class="form-control" rows="3"></textarea>
                      </div>
                    </div>
                    <div class="modal-footer">
                      <button class="btn btn-success" type="submit">Approve</button>
                      <button class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
            """)
            print(f"""
            <div class="modal fade" id="rejectModal{req_id}" tabindex="-1">
              <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                  <form method="post" action="reject_service.py">
                    <div class="modal-header bg-danger text-white">
                      <h5 class="modal-title">Reject Request </h5>
                      <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                    </div>
                    <div class="modal-body">
                      <input type="hidden" name="request_id" value="{req_id}">
                      <input type="hidden" name="status" value="Rejected">
                      <input type="hidden" name="shop_id" value="{shop_id}">
                      <input type="hidden" name="email" value="{email}">
            
                      <div class="mb-3">
                        <label for="rejection_note_{req_id}" class="form-label">Reason / Note to Customer</label>
                        <textarea class="form-control" name="rejection_note" id="rejection_note_{req_id}" rows="4"></textarea>
                      </div>
                    </div>
                    <div class="modal-footer">
                      <button type="submit" class="btn btn-danger">Reject</button>
                      <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
            
            """)

    else:
        print("""
        <tr>
          <td colspan="9" class="text-center text-muted py-4">🚫 No pending requests found.</td>
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
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """)



