#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, html

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
form = cgi.FieldStorage()
id = form.getvalue("id")
q = """ select * from mechanicshops where id='%s' """%(id)
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
  <title>owner profile</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"/>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet"/>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
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

    .profile-card {
      max-width: 900px;
      margin: 40px auto;
      background: white;
      border-radius: 12px;
      box-shadow: 0 0 20px rgb(0 0 0 / 0.1);
      padding: 30px;
    }
    .profile-img {
      width: 120px;
      height: 120px;
      object-fit: cover;
      border-radius: 50%;
      border: 4px solid #0d6efd;
    }
    .shop-img {
      width: 100%;
      max-height: 250px;
      object-fit: cover;
      border-radius: 10px;
      border: 2px solid #ddd;
    }
    .status-badge {
      font-size: 1rem;
      padding: 0.35em 0.8em;
      border-radius: 20px;
      font-weight: 600;
      user-select: none;
    }
    .toggle-switch {
      transform: scale(1.4);
      cursor: pointer;
    }
    /* Modal wider */
    .modal-lg {
      max-width: 800px !important;
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
              <a href="owner.py?id={id}" class="text-white text-decoration-none">
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
                <a class="nav-link active" href="mech.py?id={id}">
                  <i class="bi bi-speedometer2 me-2"></i>Dashboard
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="collapse" href="#serviceSubmenu" role="button" aria-expanded="false" aria-controls="serviceSubmenu">
                  <i class="bi bi-wrench-adjustable"></i> Services
                </a>
                <div class="collapse" id="serviceSubmenu">
                  <ul class="nav flex-column ms-3">
                    <li class="nav-item"><a class="nav-link" href="add_service.py?id={id}" onclick="showSection('addservice')"><i class="bi bi-bag-plus-fill"></i> Add services</a></li>
                    <li class="nav-item"><a class="nav-link" href="view_services.py?id={id}" onclick="showSection('services')"><i class="bi bi-eye"></i> View services</a></li>
                  </ul>
                </div>
              </li>
              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="collapse" href="#employeeSubmenu" role="button" aria-expanded="false" aria-controls="employeeSubmenu">
                  <i class="bi bi-tools me-2"></i>Employees
                </a>
                <div class="collapse" id="employeeSubmenu">
                  <ul class="nav flex-column ms-3">
                    <li class="nav-item"><a class="nav-link" href="add.py?id={id}" onclick="showSection('addMechanic')"><i class="bi bi-person-plus me-2"></i>Add Mechanic</a></li>
                    <li class="nav-item"><a class="nav-link" href="view.py?id={id}"><i class="bi bi-people me-2"></i>View Mechanics</a></li>
                  </ul>
                </div>
              </li>
              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="collapse" href="#requestSubmenu" role="button" aria-expanded="false" aria-controls="requestSubmenu">
                  <span><i class="bi bi-envelope me-2"></i>Requests</span>
                </a>
                <div class="collapse" id="requestSubmenu">
                  <ul class="nav flex-column ms-3">
                    <li><a href="pending.py?id={id}" class="nav-link"><i class="bi bi-card-list"></i> Pending</a></li>
                    <li><a href="current.py?id={id}" class="nav-link"><i class="bi bi-journal-check"></i> Process</a></li>
                    <li><a href="completed.py?id={id}" class="nav-link"><i class="bi bi-card-checklist"></i> Completed</a></li>
                    <li><a href="rejected_service.py?id={id}" class="nav-link"><i class="bi bi-x-square"></i> Rejected</a></li>
                    <li><a href="cancelled_service.py?id={id}" class="nav-link"><i class="bi bi-x-octagon"></i>cancelled</a></li>
                  </ul>
                </div>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="home.py"><i class="bi bi-box-arrow-right me-2"></i>Logout</a>
              </li>
            </ul>
          </nav>
          <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-4">
""")
q = """SELECT * FROM mechanicshops WHERE id=%s"""
cur.execute(q, (id,))
res = cur.fetchall()

for i in res:
    owner_name = html.escape(i[1] or "")
    dob = i[2].strftime('%Y-%m-%d') if i[2] else ""
    gender = html.escape(i[3] or "")
    email = html.escape(i[17] or "")
    phone = html.escape(i[4] or "")
    address = html.escape(i[5] or "")
    state = html.escape(i[7] or "")
    city = html.escape(i[8] or "")
    owner_image = i[9] or "default_owner.png"
    shop_image = i[12] or "default_shop.png"
    shop_name = html.escape(i[10] or "")
    shop_address = html.escape(i[11] or "")
    operating_hours = html.escape(i[14] or "")
    availability = i[19] if len(i) > 19 else 'Closed'  # Adjust index if different

    # Availability badge color and toggle state
    badge_class = "bg-success" if availability == "Open" else "bg-danger"
    toggle_checked = 'checked' if availability == "Open" else ''

    print(f"""
    <div class="profile-card shadow-sm">
      <div class="row g-4">
        <div class="col-md-4 text-center">
          <img src="./images/{owner_image}" alt="Owner Image" class="profile-img mb-3" />
          <h3 class="text-primary">{owner_name}</h3>
          <p><i class="bi bi-calendar3"></i> DOB: {dob}</p>
          <p><i class="bi bi-gender-{gender.lower()}"></i> Gender: {gender}</p>
          <p><i class="bi bi-envelope"></i> {email}</p>
          <p><i class="bi bi-phone"></i> {phone}</p>
          <p><i class="bi bi-geo-alt"></i> {address}, {city}, {state}</p>
        </div>
        <div class="col-md-8">
          <img src="./images/{shop_image}" alt="Shop Image" class="shop-img mb-3" />
          <h4 class="text-secondary">{shop_name}</h4>
          <p><i class="bi bi-geo-alt-fill"></i> {shop_address}</p>
          <p><i class="bi bi-clock"></i> Operating Hours: {operating_hours}</p>

          <div class="d-flex align-items-center justify-content-between mt-4">
            <div>
              <span class="status-badge {badge_class}" id="availabilityBadge{i[0]}">{availability}</span>
            </div>
            <div>
              <label class="form-check form-switch d-flex align-items-center">
                <input class="form-check-input toggle-switch" type="checkbox" id="availabilitySwitch{i[0]}" {toggle_checked} onchange="toggleAvailability({i[0]})" />
                <span class="form-check-label ms-2">Toggle Availability</span>
              </label>
            </div>
          </div>

          <div class="mt-4 d-flex gap-3">
            <button class="btn btn-primary flex-grow-1" data-bs-toggle="modal" data-bs-target="#editModal{i[0]}">Edit Profile</button>
            <button class="btn btn-warning flex-grow-1" data-bs-toggle="modal" data-bs-target="#passwordModal{i[0]}">Change Password</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Edit Profile Modal -->
    <div class="modal fade" id="editModal{i[0]}" tabindex="-1" aria-labelledby="editModalLabel{i[0]}" aria-hidden="true">
      <div class="modal-dialog modal-lg modal-dialog-centered">
        <form method="post" action="update_owner.py" enctype="multipart/form-data" onsubmit="return fun(event)">
          <div class="modal-content">
            <div class="modal-header bg-primary text-white">
              <h5 class="modal-title" id="editModalLabel{i[0]}">Edit Profile</h5>
              <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <input type="hidden" name="id" value="{i[0]}">
              <div class="container-fluid">
                <div class="row g-3">
                  <!-- Personal Details -->
                  <div class="col-md-6">
                    <h6 class="mb-3 text-primary">Personal Details</h6>
                    <div class="mb-3">
                      <label for="name{i[0]}" class="form-label">Owner Name</label>
                      <input type="text" class="form-control" id="name{i[0]}" name="name" value="{owner_name}" readonly>
                      <div class="invalid-feedback">Please enter owner name.</div>
                    </div>
                    <div class="mb-3">
                      <label for="dob{i[0]}" class="form-label">Date of Birth</label>
                      <input type="date" class="form-control" id="dob{i[0]}" name="dob" value="{dob}" readonly>
                      <div class="invalid-feedback">Please enter date of birth.</div>
                    </div>
                    <div class="mb-3">
                      <label for="gender{i[0]}" class="form-label">Gender</label>
                      <input class="form-control" id="gender{i[0]}" name="gender" value="{i[3]}" readonly >
                    </div>
                    <div class="mb-3">
                      <label for="email{i[0]}" class="form-label">Email</label>
                      <input type="email" class="form-control" id="email" name="email" value="{email}" required>
                      <div class="invalid-feedback">Please enter a valid email address.</div>
                    </div>
                    <div class="mb-3">
                      <label for="phone{i[0]}" class="form-label">Phone</label>
                      <input type="tel" class="form-control" id="phone" name="phone" value="{phone}" required >
                      <div class="invalid-feedback">Please enter a valid phone number.</div>
                    </div>
                    <div class="mb-3">
                      <label for="address{i[0]}" class="form-label">Address</label>
                      <textarea class="form-control" id="address" name="address" rows="2" required>{address}</textarea>
                      <div class="invalid-feedback">Please enter your address.</div>
                    </div>
                    <div class="mb-3">
                      <label for="owner_image{i[0]}" class="form-label">Owner Image</label>
                      <input type="file" class="form-control" id="image" name="owner_Image" value="{owner_image}" accept="image/*">
                    </div>
                  </div>

                  <!-- Shop Details -->
                  <div class="col-md-6">
                    <h6 class="mb-3 text-primary">Shop Details</h6>
                    <div class="mb-3">
                      <label for="shop_name{i[0]}" class="form-label">Shop Name</label>
                      <input type="text" class="form-control" id="shop_name{i[0]}" name="shop_name" value="{shop_name}" readonly>
                      <div class="invalid-feedback">Please enter shop name.</div>
                    </div>
                    <div class="mb-3">
                      <label for="shop_address{i[0]}" class="form-label">Shop Address</label>
                      <textarea class="form-control" id="saddress" name="shop_address" rows="2" required>{shop_address}</textarea>
                      <div class="invalid-feedback">Please enter shop address.</div>
                    </div>
                    <div class="mb-3">
                      <label for="shop_image{i[0]}" class="form-label">Shop Image</label>
                      <input type="file" class="form-control" id="simage" name="shop_image" accept="image/*">
                    </div>
                    <div class="mb-3">
                      <label for="operating_hours{i[0]}" class="form-label">Operating Hours</label>
                      <input type="text" class="form-control" id="hours" name="operating_hours" value="{operating_hours}" required>
                      <div class="invalid-feedback">Please enter operating hours.</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="modal-footer">
              <button type="submit" class="btn btn-primary" name="submit">Save Changes</button>
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <!-- Change Password Modal -->
    <div class="modal fade" id="passwordModal{i[0]}" tabindex="-1" aria-labelledby="passwordModalLabel{i[0]}" aria-hidden="true">
      <div class="modal-dialog modal-xl modal-dialog-centered">
        <form method="post" action="change_password_shop.py" class="needs-validation" novalidate>
          <div class="modal-content">
            <div class="modal-header bg-warning text-dark">
              <h5 class="modal-title" id="passwordModalLabel{i[0]}"><i class="bi bi-key"></i> Change Password</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body py-4 px-5">
              <input type="hidden" name="id" value="{i[0]}">
              <div class="row g-4">
                <div class="col-md-4">
                  <label for="current_password{i[0]}" class="form-label">
                    <i class="bi bi-lock-fill"></i> Current Password
                  </label>
                  <input type="password" class="form-control" id="current_password{i[0]}" name="current_password" required>
                  <div class="invalid-feedback">Please enter your current password.</div>
                </div>
                <div class="col-md-4">
                  <label for="new_password{i[0]}" class="form-label">
                    <i class="bi bi-lock"></i> New Password
                  </label>
                  <input type="password" class="form-control" id="new_password{i[0]}" name="new_password" required minlength="6">
                  <div class="invalid-feedback">New password must be at least 6 characters.</div>
                </div>
                <div class="col-md-4">
                  <label for="confirm_password{i[0]}" class="form-label">
                    <i class="bi bi-lock-check"></i> Confirm New Password
                  </label>
                  <input type="password" class="form-control" id="confirm_password{i[0]}" name="confirm_password" required>
                  <div class="invalid-feedback">Please confirm your new password.</div>
                </div>
              </div>
            </div>
            <div class="modal-footer">
              <button type="submit" class="btn btn-warning">
                <i class="bi bi-shield-lock"></i> Change Password
              </button>
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
            </div>
          </div>
        </form>
      </div>
    </div>
    </main>
    """)

print("""
    <div class="overlay" id="overlay"></div>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js"></script>
    <script>
      function fun(event) {
        const email = document.getElementById("email").value.trim();
        const phone = document.getElementById("phone").value.trim();
        const address = document.getElementById("address").value.trim();
        const saddress = document.getElementById("saddress").value.trim();
        const hours = document.getElementById("hours").value.trim();

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

        if (saddress === "") {
          alert("Please enter your shop address.");
          return false;
        }

        if (hours === "") {
          alert("Please enter your working hours.");
          return false;
        }

        return true;
      }

      function toggleAvailability(id) {
        const switchEl = document.getElementById('availabilitySwitch' + id);
        const badge = document.getElementById('availabilityBadge' + id);
        const newStatus = switchEl.checked ? 'Open' : 'Closed';

        // Update UI immediately
        if (switchEl.checked) {
          badge.innerText = 'Open';
          badge.classList.remove('bg-danger');
          badge.classList.add('bg-success');
        } else {
          badge.innerText = 'Closed';
          badge.classList.remove('bg-success');
          badge.classList.add('bg-danger');
        }

        // Send POST request to backend Python CGI script
        fetch('update_availability.py', {
          method: 'POST',
          headers: {'Content-Type': 'application/x-www-form-urlencoded'},
          body: `id=${encodeURIComponent(id)}&status=${encodeURIComponent(newStatus)}`
        })
        .then(response => response.json())
        .then(data => {
          if (data.success) {
            alert("Availability updated successfully to " + newStatus + "!");
          } else {
            alert('Failed to update availability: ' + data.message);
            // Revert UI on failure
            switchEl.checked = !switchEl.checked;
            badge.innerText = newStatus === 'Open' ? 'Closed' : 'Open';
            badge.classList.toggle('bg-danger');
            badge.classList.toggle('bg-success');
          }
        })
        .catch(() => {
          alert('Error connecting to server.');
          // Revert UI on error
          switchEl.checked = !switchEl.checked;
          badge.innerText = newStatus === 'Open' ? 'Closed' : 'Open';
          badge.classList.toggle('bg-danger');
          badge.classList.toggle('bg-success');
        });
      }

      document.addEventListener('DOMContentLoaded', () => {
        // Sidebar toggle for mobile view
        document.getElementById('toggleSidebar').addEventListener('click', () => {
          document.getElementById('sidebarMenu').classList.toggle('show');
          document.getElementById('overlay').classList.toggle('show');
        });

        // Close sidebar when clicking overlay
        document.getElementById('overlay').addEventListener('click', () => {
          document.getElementById('sidebarMenu').classList.remove('show');
          document.getElementById('overlay').classList.remove('show');
        });

        // Password toggle visibility
        document.querySelectorAll('input[type="password"]').forEach(input => {
          const toggle = document.createElement('span');
          toggle.innerHTML = '<i class="bi bi-eye-slash"></i>';
          toggle.style.position = 'absolute';
          toggle.style.right = '10px';
          toggle.style.top = '50%';
          toggle.style.transform = 'translateY(-50%)';
          toggle.style.cursor = 'pointer';
          toggle.style.color = '#888';

          const wrapper = document.createElement('div');
          wrapper.classList.add('position-relative');

          input.parentNode.insertBefore(wrapper, input);
          wrapper.appendChild(input);
          wrapper.appendChild(toggle);

          toggle.addEventListener('click', () => {
            const type = input.getAttribute('type') === 'password' ? 'text' : 'password';
            input.setAttribute('type', type);
            toggle.innerHTML = type === 'password' ? '<i class="bi bi-eye-slash"></i>' : '<i class="bi bi-eye"></i>';
          });
        });
      });
    </script>
</body>
</html>
""")

cur.close()
con.close()