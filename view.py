#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb
from datetime import datetime

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
form = cgi.FieldStorage()
shop_id = form.getvalue("id")
q = """ select * from mechanicshops where id='%s' """%(shop_id)
cur.execute(q)
res = cur.fetchall()
for i in res:
    profile_img = i[9]
    shop_name = i[10]

    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <title> View Mechanics | RoadNova</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" />
      <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet" />
      <style>

        body {
          font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
     
          color: #333;
        }
        .sidebar {
            color: #050a30 !important;
            min-height: 100vh;
            width: 250px;
            background-color: #b1d4e0;
          }

          .sidebar .nav-link {
            color: #050a30 !important;
            font-weight: 500;
          }

          .sidebar .nav-link:hover,
          .sidebar .nav-link.active {
            background-color: #2e8bc0 !important;
            color: #ffffff !important;
          }

            @media (max-width: 768px) {
              .sidebar {
                position: fixed;
                top: 56px;
                left: -250px;
                width: 250px;
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

        h1 {
          margin-bottom: 40px;
          color: #1E3C72;
          text-align: center;
          font-weight: 700;
          text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
        }
        table {
          background: #fff;
          border-radius: 10px;
          box-shadow: 0 8px 24px rgba(0,0,0,0.12);
          overflow: hidden;
          width: 100%;
        }
        th {
          background-color: #1E90FF;
          color: red;
          font-weight: 600;
          text-align: center;
          vertical-align: middle;
          padding: 12px;
        }
        td {
          vertical-align: middle;
          text-align: center;
          padding: 12px;
        }
        .btn-primary {
          background-color: #1E90FF;
          border: none;
          transition: background-color 0.3s ease;
        }
        .btn-primary:hover {
          background-color: #0a60d1;
        }
        .btn-warning {
          background-color: #f0ad4e;
          border: none;
          color: white;
          transition: background-color 0.3s ease;
        }
        .btn-warning:hover {
          background-color: #ec971f;
          color: white;
        }
        /* Modal Custom */
        .modal-header {
          background: linear-gradient(90deg, #1E90FF, #104E8B);
          color: white;
          border-bottom: none;
        }
        .modal-title {
          font-weight: 700;
          font-size: 1.5rem;
        }
        .modal-body {
          background: #f7f9fc;
          border-radius: 0 0 10px 10px;
          padding: 30px;
          color: #444;
        }
        .profile-pic {
          display: block;
          margin: 0 auto 20px;
          width: 120px;
          height: 120px;
          border-radius: 50%;
          object-fit: cover;
          box-shadow: 0 4px 15px rgba(0,0,0,0.2);
          border: 3px solid #1E90FF;
        }
        .detail-label {
          font-weight: 600;
          color: #1E3C72;
        }
        .detail-row {
          margin-bottom: 15px;
        }
        hr {
          border-top: 2px solid #1E90FF;
          margin: 25px 0;
          opacity: 0.7;
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
    <body>
    """)
    print(f"""
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
           <div id="sidebarOverlay" style="display:none; position: fixed; top: 0; left: 0; width:100%; height:100%; background: rgba(0,0,0,0.5); z-index:1049;"></div>
          <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-4">
      <h1>Employees</h1>
      <div class="table-responsive">
        <table class="table table-bordered align-middle">
          <thead>
            <tr>
              <th>S.NO</th>
              <th>Date Joined</th>
              <th>Full Name</th>
              <th>Email</th>
              <th>Phone</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
    """)



query = """SELECT * FROM mechanics WHERE shop_id=%s"""
cur.execute(query, (shop_id,))
results = cur.fetchall()

for idx, row in enumerate(results, start=1):
    joined_date = datetime.strptime(str(row[7]), "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
    print(f"""
        <tr>
          <td>{idx}</td>
          <td>{joined_date}</td>
          <td>{row[1]}</td>
          <td>{row[3]}</td>
          <td>{row[2]}</td>
          <td>
            <button class="btn btn-primary me-2" data-bs-toggle="modal" data-bs-target="#viewModal{row[0]}">
              <i class="bi bi-eye"></i> View Details
            </button>
            <button class="btn btn-warning" data-bs-toggle="modal" data-bs-target="#editModal{row[0]}">
              <i class="bi bi-pencil-square"></i> Edit
            </button>
          </td>
        </tr>
    """)

print("""
      </tbody>
    </table>
  </div>
""")

for row in results:
    dob_display = datetime.strptime(str(row[8]), "%Y-%m-%d").strftime("%d-%m-%Y") if row[8] else "N/A"
    dob_input = datetime.strptime(str(row[8]), "%Y-%m-%d").strftime("%Y-%m-%d") if row[8] else ""
    id_proof_file = row[12] if row[12] else "default-idproof.png"
    profile_pic = row[11] if row[11] else "default-profile.png"

    print(f"""
    <!-- View Details Modal -->
    <div class="modal fade" id="viewModal{row[0]}" tabindex="-1" aria-labelledby="viewModalLabel{row[0]}" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="viewModalLabel{row[0]}">Employee Details</h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <img src="uploads/photos/{profile_pic}" alt="Profile Picture" class="profile-pic" />
            <h3 class="text-center mb-4" style="color:#1E90FF;">{row[1]}</h3>
            <hr />
            <div class="row detail-row">
              <div class="col-md-4 detail-label">Date of Birth:</div>
              <div class="col-md-8">{dob_display}</div>
            </div>
            <div class="row detail-row">
              <div class="col-md-4 detail-label">Gender:</div>
              <div class="col-md-8">{row[9]}</div>
            </div>
            <div class="row detail-row">
              <div class="col-md-4 detail-label">Email:</div>
              <div class="col-md-8">{row[3]}</div>
            </div>
            <div class="row detail-row">
              <div class="col-md-4 detail-label">Phone:</div>
              <div class="col-md-8">{row[2]}</div>
            </div>
            <div class="row detail-row">
              <div class="col-md-4 detail-label">Address:</div>
              <div class="col-md-8">{row[4]}</div>
            </div>
            <div class="row detail-row">
              <div class="col-md-4 detail-label">Specialization:</div>
              <div class="col-md-8">{row[5]}</div>
            </div>
            <div class="row detail-row">
              <div class="col-md-4 detail-label">Experience:</div>
              <div class="col-md-8">{row[6]}</div>
            </div>
            <div class="row detail-row">
              <div class="col-md-4 detail-label">ID Proof:</div>
              <div class="col-md-8">
                <button class="btn btn-link p-0" data-bs-toggle="modal" data-bs-target="#idProofModal{row[0]}">
                  View ID Proof
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ID Proof Modal -->
    <div class="modal fade" id="idProofModal{row[0]}" tabindex="-1" aria-labelledby="idProofModalLabel{row[0]}" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="idProofModalLabel{row[0]}">ID Proof</h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body text-center">
            <img src="uploads/idproofs/{id_proof_file}" alt="ID Proof" class="img-fluid rounded" />
          </div>
        </div>
      </div>
    </div>

    <!-- Edit Modal -->
    <div class="modal fade" id="editModal{row[0]}" tabindex="-1" aria-labelledby="editModalLabel{row[0]}" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
          <form method="post" action="update_employee.py?shop_id={shop_id}" enctype="multipart/form-data" onsubmit="return fun(event)">
            <div class="modal-header">
              <h5 class="modal-title" id="editModalLabel{row[0]}">Edit Employee Details</h5>
              <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <input type="hidden" name="mechanic_id" value="{row[0]}" />

              <div class="mb-3">
                <label for="fullName{row[0]}" class="form-label">Full Name</label>
                <input type="text" class="form-control" id="fullName{row[0]}" name="full_name" value="{row[1]}" readonly />
              </div>

              <div class="mb-3">
                <label for="phone{row[0]}" class="form-label">Phone</label>
                <input type="text" class="form-control" id="phone" name="phone" value="{row[2]}" required />
              </div>

              <div class="mb-3">
                <label for="email{row[0]}" class="form-label">Email</label>
                <input type="email" class="form-control" id="email" name="email" value="{row[3]}" required />
              </div>

              <div class="mb-3">
                <label for="address{row[0]}" class="form-label">Address</label>
                <textarea class="form-control" id="address" name="address" rows="2" required>{row[4]}</textarea>
              </div>

              <div class="mb-3">
                <label for="specialization{row[0]}" class="form-label">Specialization</label>
                <input type="text" class="form-control" id="specialization{row[0]}" name="specialization" value="{row[5]}" required />
              </div>

              <div class="mb-3">
                <label for="experience{row[0]}" class="form-label">Experience</label>
                <input type="text" class="form-control" id="experience{row[0]}" name="experience" value="{row[6]}" readonly />
              </div>

              <div class="mb-3">
                <label for="dob{row[0]}" class="form-label">Date of Birth</label>
                <input type="date" class="form-control" id="dob{row[0]}" name="dob" value="{dob_input}" readonly />
              </div>

              <div class="mb-3">
                <label for="gender{row[0]}" class="form-label">Gender</label>
                <input type="text" class="form-control" id="gender{row[0]}" name="gender" value="{row[9]}"readonly>
              </div>

              <div class="mb-3">
                <label for="profilePic{row[0]}" class="form-label">Profile Picture (Upload to replace)</label>
                <input type="file" class="form-control" id="profilePic{row[0]}" name="profile_pic" accept="image/*" />
              </div>

              <div class="mb-3">
                <label for="idProof{row[0]}" class="form-label">ID Proof (Upload to replace)</label>
                <input type="file" class="form-control" id="idProof{row[0]}" name="id_proof" accept="image/*,application/pdf" />
              </div>

            </div>
            <div class="modal-footer">
              <button type="submit" class="btn btn-success">Save Changes</button>
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
            </div>
          </form>
        </div>
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
  function fun(event) {
  const email = document.getElementById("email").value.trim();
  const phone = document.getElementById("phone").value.trim();
  const address = document.getElementById("address").value.trim();
  

  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (!emailPattern.test(email)) {
    alert("Please enter a valid email address.");
    return false;
  }

  if (!/^\d{10}$/.test(phone)) {
    alert("Please enter a valid 10-digit phone number.");
    return false;
  }

  if (address === "") {
    alert("Please enter your address.");
    return false;
  }


  return true;
}
            </script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")
