#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe

print("Content-Type: text/html\r\n\r\n")

import pymysql, cgi, cgitb
cgitb.enable()

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

form = cgi.FieldStorage()
user_id = form.getvalue("user_id")
q = "SELECT * FROM users WHERE user_id=%s"
cur.execute(q, (user_id,))
res = cur.fetchall()

print("""
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Current Bookings</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
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
.container {
  margin-top: 100px;
  margin-left: auto;
  margin-right: auto;
  max-width: 800px;
  width: 80%;
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

        <!-- RIGHT ALIGNED PROFILE BUTTON -->
      <div class="d-flex align-items-center ms-auto me-2">
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
              <a href="user.py?user_id={user_id}" class="nav-link" >Home</a>
            </li>

            <li class="nav-item">
              <a href="#" class="nav-link" onclick="toggleSubMenu('bookingSubMenu')">Booking <i class="bi bi-caret-down-fill"></i></a>
              <ul id="bookingSubMenu" class="nav flex-column ms-3 submenu d-none">
                <li><a href="current_booking.py?user_id={user_id}" class="nav-link" >Booked</a></li>
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

print("""
<div class="container">
  <h2 class="mb-4 text-center" style="color:#ff8300">Current Bookings</h2>
""")

# Query current bookings for user
query = """
SELECT sr.request_id, sr.problem_type, sr.request_date,
       ms.shop_name, ms.shop_address, ms.phone, ms.shop_image
FROM service_requests sr
LEFT JOIN mechanicshops ms ON sr.shop_id = ms.id
WHERE sr.user_id = %s AND sr.status = 'Pending'
"""

cur.execute(query, (user_id,))
results = cur.fetchall()

if results:
    for i in results:
        shop_img = i[6]
        req_id = i[0]
        problem = i[1]
        date = i[2]
        shop_name = i[3]
        shop_address = i[4]
        phone = i[5]

        print(f"""
                <div class="card mb-4 shadow-sm">
          <div class="row g-0">
            <!-- Shop Image -->
            <div class="col-md-4">
              <img src="/roadassist/images/{shop_img}" class="img-fluid rounded-start h-auto w-auto" style="object-fit: cover;" alt="{shop_name}">
            </div>

            <!-- Booking Details -->
            <div class="col-md-8">
              <div class="card-body">
                <h5 class="card-title text-success mb-2">🔧 Problem: {problem}</h5>

                
               

                <p class="card-text mb-1"><strong>Date:</strong> {date.strftime('%d-%m-%Y')}</p>
                <p class="card-text mb-1"><strong>Shop:</strong> {shop_name}</p>
                <p class="card-text mb-1"><strong>Address:</strong> {shop_address}</p>
                <p class="card-text mb-1"><strong>Contact:</strong> {phone}</p>
              

                <!-- Map -->
                <div class="mb-6">
                <div class="d-flex flex-wrap  align-items-center">
                  <a href="https://www.google.com/maps/search/?api=1&query={shop_address.replace(' ', '+')}" target="_blank" class="btn btn-outline-primary btn-sm">
                    <i class="bi bi-geo-alt-fill"></i> View on Map
                  </a>
                    <form method="post" action="cancel_service.py" class="d-inline" onsubmit="return confirm('Are you sure you want to cancel this booking?');">
                      <input type="hidden" name="request_id" value="{req_id}">
                      <button type="submit" class="btn btn-danger btn-sm" style="margin-left:10px;">
                        <i class="bi bi-x-circle"></i> Cancel
                      </button>
                    </form>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <script>
        document.getElementById('payment_method_{req_id}').addEventListener('change', function () {{
            const method = this.value;
            document.getElementById('creditCardFields{req_id}').style.display = method === 'Credit Card' ? 'block' : 'none';
            document.getElementById('upiField{req_id}').style.display = method === 'UPI' ? 'block' : 'none';
        }});
        </script>
        """)

else:
    print("""
    <div class="alert alert-info text-center" role="alert">
      No current bookings found.
    </div>
    """)

# HTML Footer
print(f"""
</div>
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


</script>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")

# Close DB connection
con.close()
