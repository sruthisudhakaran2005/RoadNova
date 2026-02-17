#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type: text/html\r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
form = cgi.FieldStorage()
user_id = form.getvalue("user_id")
updated = form.getvalue("updated")
pwd_updated = form.getvalue("pwd_updated")

con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
cur.execute("SELECT COUNT(*) FROM notifications WHERE user_id=%s AND status='unseen'", (user_id,))
notification_count = cur.fetchone()[0]
q = "SELECT * FROM users WHERE user_id=%s"
cur.execute(q, (user_id,))
res = cur.fetchall()

# Start HTML
print("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>User Profile</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .navbar-custom {
      background-color: azure;
    }

    .logo {
      border-radius: 50%;
      height: 60px;
      margin-right: 10px;
    }

    .mainhead {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      font-weight: 500;
    }

    .section1 {
      position: relative;
      min-height: 300px;
      display: flex;
      justify-content: center;
      align-items: center;
      text-align: center;
      color: white;
      background-image: url('/roadassist/images/img1.jpg');
      background-size: cover;
      background-position: center;
    }

    .section1::before {
      content: "";
      position: absolute;
      inset: 0;
      background: inherit;
      filter: blur(4px);
      z-index: 1;
    }

    .section1 .data {
      position: relative;
      z-index: 2;
      padding: 20px;
    }

    .help:hover {
      color: rgb(255, 106, 0);
    }

    .sidebar {
      position: fixed;
      top: 74px;
      left: -250px;
      width: 250px;
      height: 100%;
      background-color: rgb(253, 248, 248);
      color: rgb(252, 2, 2);
      padding-top: 30px;
      transition: all 0.3s ease;
      z-index: 1000;
    }

    .sidebar.show {
      left: 0;
    }

    .sidebar .nav-link {
      color: #0b0b0b;
      padding: 15px 20px;
    }

    .sidebar .nav-link:hover,
    .sidebar .nav-link.active {
      background-color: #e2cccc;
      color: rgb(250, 4, 4);
    }

    .overlay {
      top: 0;
      left: 0;
      height: 100%;
      width: 100%;
      background-color: rgba(0, 0, 0, 0.5);
      z-index: 990;
      display: none;
    }

    .overlay.show {
      display: block;
    }

    .main-content {
      padding: 20px;
      margin-left: 0;
      margin-top: 90px;
      transition: margin-left 0.3s ease;
    }

    @media (min-width: 768px) {
      .sidebar {
        left: 0;
      }
      .main-content {
        margin-left: 250px;
      }
      .overlay {
        display: none !important;
      }
      #sidebarToggleBtn {
        display: none;
      }
    }
     .submenu {
  background-color: #f5f5f5;
  border-left: 2px solid #ccc;
}

.submenu .nav-link {
  padding-left: 30px;
  font-size: 0.95rem;
}
.profile-btn {
  background: linear-gradient(to right, #ff4500, #ff6347); /* red-orange gradient */
  color: white;
  border: none;
  border-radius: 25px;
  padding: 8px 18px;
  font-weight: 500;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  transition: all 0.3s ease;
}

.profile-btn:hover {
  background: #d62900; /* darker red-orange on hover */
  color: #fff;
  transform: scale(1.05);
  box-shadow: 0 6px 12px rgba(0,0,0,0.15);
}

    .profile-card {
      margin-top:100px;
      background-color: #ffffff;
      border-radius: 15px;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
      overflow: hidden;
      transition: all 0.3s ease-in-out;
    }
    .profile-header {
      background-color: #0d6efd;
      color: white;
      padding: 2rem;
      text-align: center;
    }
    .profile-header i {
      font-size: 4rem;
    }
    .profile-header h2 {
      margin-top: 1rem;
      font-weight: 700;
    }
    .profile-body {
      padding: 2rem;
    }
    .info-label {
      font-weight: 600;
      color: #6c757d;
    }
    .info-value {
      color: #212529;
    }
    .btn-custom {
      border-radius: 30px;
      padding: 0.5rem 1.5rem;
      font-weight: 600;
    }
    .action-buttons {
      text-align: center;
      padding-bottom: 2rem;
    }
    .badge-custom {
      background-color: #6c757d;
      font-size: 0.9rem;
      padding: 0.4em 0.8em;
      border-radius: 1em;
    }
    
.notification-btn {
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}


  </style>
</head>
<body>
""")
for i in res:
    name = i[1]
    print(f"""
    <nav class="navbar navbar-expand-lg navbar-custom fixed-top py-2" style="box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
    <div class="container-fluid d-flex flex-wrap align-items-center justify-content-between">
    <div class="d-flex align-items-center">
      <button class="btn btn-outline-dark me-2 d-md-none" id="sidebarToggleBtn">
        <i class="bi bi-list"></i>
      </button>
      
      <h3 class="mainhead mb-0 ms-2">RoadNova</h3>
     </div>

      <div class="d-flex align-items-center ms-auto me-2 gap-3">
      <a href="notification_users.py?user_id={user_id}">
       <button class="btn profile-btn" style="position: relative;">
        <i class="bi bi-bell"></i>
        <span style="position: absolute; top: 0px; right: 8px; font-weight: bold; font-size: 17px; color: white;">
          {notification_count if notification_count > 0 else ""}
        </span>
      </button>
      </a>
      <a href="user_profile.py?user_id={user_id}"><button class="btn profile-btn">
        <i class="bi bi-person-circle"></i> Profile
      </button>
      </a>
      </div>
    </div>
    </nav>


        <div class="sidebar" id="sidebar" style="box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
          <ul class="nav flex-column">
            <li class="nav-item">
              <a href="user.py?user_id={user_id}" class="nav-link">Home</a>
            </li>
            
            <li class="nav-item">
              <a href="#" class="nav-link" onclick="toggleSubMenu('bookingSubMenu')">Booking <i class="bi bi-caret-down-fill"></i></a>
              <ul id="bookingSubMenu" class="nav flex-column ms-3 submenu d-none">
        <li><a href="approved_booking.py?user_id={user_id}" class="nav-link" >On Going</a></li>
        <li><a href="completed_booking.py?user_id={user_id}" class="nav-link" >Completed</a></li>
        <li><a href="cancelled_booking.py?user_id={user_id}" class="nav-link" >Cancelled</a></li>
         <li><a href="rejected_booking.py?user_id={user_id}" class="nav-link" >Rejected</a></li>
              </ul>
            </li>
            <li class="nav-item">
             <a href="shops.py?user_id={user_id}" class="nav-link">Mechanic shops</a>
           </li>
            <li class="nav-item">
              <a href="home.py" class="nav-link">Logout</a>
            </li>
          </ul>
        </div>
        
        """)
# Show alerts if any
if updated == "1":
    print("""<div class="container"><div class="alert alert-success text-center">Profile updated successfully!</div></div>""")
if pwd_updated == "1":
    print("""<div class="container"><div class="alert alert-success text-center">Password changed successfully!</div></div>""")
if pwd_updated == "0":
    print("""<div class="container"><div class="alert alert-danger text-center">Current password is incorrect!</div></div>""")

# Display user
if res:
    i = res[0]
    user_id, name, gender, email, phone, address, pincode = i[:7]

    print(f"""
    <div class="container">
      <div class="profile-card mx-auto" style="max-width: 700px;">
        <div class="profile-header">
          <i class="bi bi-person-circle"></i>
          <h2>{name}</h2>
          <span class="badge badge-custom">{gender}</span>
        </div>
        <div class="profile-body">
          <p><span class="info-label"><i class="bi bi-envelope-fill me-2"></i>Email:</span> <span class="info-value">{email}</span></p>
          <p><span class="info-label"><i class="bi bi-telephone-fill me-2"></i>Phone:</span> <span class="info-value">{phone}</span></p>
          <p><span class="info-label"><i class="bi bi-geo-alt-fill me-2"></i>Address:</span> <span class="info-value">{address}</span></p>
          <p><span class="info-label"><i class="bi bi-mailbox2 me-2"></i>Pincode:</span> <span class="info-value">{pincode}</span></p>
        </div>
        <div class="action-buttons">
          <button class="btn btn-primary btn-custom me-2" data-bs-toggle="modal" data-bs-target="#editModal">Edit Profile</button>
          <button class="btn btn-warning btn-custom" data-bs-toggle="modal" data-bs-target="#passwordModal">Change Password</button>
        </div>
      </div>
    </div>

    <!-- Edit Profile Modal -->
    <div class="modal fade" id="editModal" tabindex="-1">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <form method="post" action="update_profile.py">
            <div class="modal-header bg-primary text-white">
              <h5 class="modal-title"><i class="bi bi-pencil-fill me-2"></i>Edit Profile</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
              <input type="hidden" name="user_id" value="{user_id}">
              <input type="text" name="name" class="form-control mb-3" value="{name}" readonly>
              <input type="text" name="gender" class="form-control mb-3" value="{gender}" readonly >
              <input type="email" name="email" class="form-control mb-3" value="{email}" required>
              <input type="text" name="phone" class="form-control mb-3" value="{phone}" required>
              <textarea name="address" class="form-control mb-3" required>{address}</textarea>
              <input type="text" name="pincode" class="form-control mb-3" value="{pincode}" required>
            </div>
            <div class="modal-footer">
              <button type="submit" class="btn btn-success">Save</button>
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
            </div>
          </form>
        </div>
      </div>
    </div>
<!-- Change Password Modal -->
<div class="modal fade" id="passwordModal" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <form method="post" action="change_password.py">
        <div class="modal-header bg-warning text-white">
          <h5 class="modal-title"><i class="bi bi-key-fill me-2"></i>Change Password</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body">
          <input type="hidden" name="user_id" value="{user_id}">

          <!-- Current Password -->
          <div class="input-group mb-3">
            <input type="password" name="current_password" class="form-control" placeholder="Current Password" id="currentPwd" required>
            <button type="button" class="btn btn-outline-secondary" onclick="togglePassword('currentPwd', this)">
              <i class="bi bi-eye-slash"></i>
            </button>
          </div>

          <!-- New Password -->
          <div class="input-group mb-3">
            <input type="password" name="new_password" class="form-control" placeholder="New Password" id="newPwd" required>
            <button type="button" class="btn btn-outline-secondary" onclick="togglePassword('newPwd', this)">
              <i class="bi bi-eye-slash"></i>
            </button>
          </div>

          <!-- Confirm Password -->
          <div class="input-group mb-3">
            <input type="password" name="confirm_password" class="form-control" placeholder="Confirm Password" id="confirmPwd" required>
            <button type="button" class="btn btn-outline-secondary" onclick="togglePassword('confirmPwd', this)">
              <i class="bi bi-eye-slash"></i>
            </button>
          </div>

        </div>
        <div class="modal-footer">
          <button type="submit" class="btn btn-warning">Update Password</button>
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
        </div>
      </form>
    </div>
  </div>
</div>

    """)

print(f"""
<script>
  const sidebar = document.getElementById('sidebar');
  const overlay = document.getElementById('overlay');
  const toggleBtn = document.getElementById('sidebarToggleBtn');

  toggleBtn.addEventListener('click', () => {{
    sidebar.classList.toggle('show');
    overlay.classList.toggle('show');
  }});

  overlay.addEventListener('click', () => {{
    sidebar.classList.remove('show');
    overlay.classList.remove('show');
  }});

  

  function toggleSubMenu(id) {{
    const submenu = document.getElementById(id);
    submenu.classList.toggle('d-none');
  }}

  function showSection(id) {{
    document.querySelectorAll('.content-section').forEach(section => {{
      section.classList.remove('active');
    }});
    document.getElementById(id).classList.add('active');

    document.querySelectorAll('.sidebar .nav-link').forEach(link => {{
      link.classList.remove('active');
    }});
    event.target.classList.add('active');

    if (window.innerWidth < 768) {{
      sidebar.classList.remove('show');
      overlay.classList.remove('show');
    }}
  }}

 function togglePassword(inputId, btn) {{
    const input = document.getElementById(inputId);
    const icon = btn.querySelector('i');
    if (input.type === "password") {{
      input.type = "text";
      icon.classList.remove("bi-eye-slash");
      icon.classList.add("bi-eye");
    }} else {{
      input.type = "password";
      icon.classList.remove("bi-eye");
      icon.classList.add("bi-eye-slash");
    }}
  }}
</script>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")
