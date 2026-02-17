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

# Count unseen notifications
cur.execute("SELECT COUNT(*) FROM notifications WHERE user_id=%s AND status='unseen'", (user_id,))
notification_count = cur.fetchone()[0]

# Mark unseen notifications as seen after fetching
cur.execute("UPDATE notifications SET status='seen' WHERE user_id=%s AND status='unseen'", (user_id,))
con.commit()

# Get user name (if needed)
cur.execute("SELECT * FROM users WHERE user_id=%s", (user_id,))
res = cur.fetchall()

# Date filters
start_date = form.getvalue("start_date")
end_date = form.getvalue("end_date")

if start_date and end_date:
    cur.execute("""
        SELECT n.id, n.message, n.created_at, n.status, s.shop_image, s.shop_name
        FROM notifications n
        JOIN mechanicshops s ON n.shop_name = s.shop_name
        WHERE n.user_id=%s AND n.created_at BETWEEN %s AND %s
        ORDER BY n.created_at DESC
    """, (user_id, start_date, end_date))
else:
    cur.execute("""
        SELECT n.id, n.message, n.created_at, n.status, s.shop_image, s.shop_name
        FROM notifications n
        JOIN mechanicshops s ON n.shop_name = s.shop_name
        WHERE n.user_id=%s
        ORDER BY n.created_at DESC
    """, (user_id,))

notifications = cur.fetchall()

# Begin HTML
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>User Dashboard</title>

  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"/>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet"/>

  <style>
    body {{
      overflow-x: hidden;
    }}
    .navbar-custom {{
      background-color: azure;
    }}
    .mainhead {{
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      font-weight: 500;
    }}
    .help:hover {{
      color: rgb(255, 106, 0);
    }}
    .sidebar {{
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
    }}
    .sidebar.show {{
      left: 0;
    }}
    .sidebar .nav-link {{
      color: #0b0b0b;
      padding: 15px 20px;
    }}
    .sidebar .nav-link:hover,
    .sidebar .nav-link.active {{
      background-color: #e2cccc;
      color: rgb(250, 4, 4);
    }}
    .overlay {{
      top: 0;
      left: 0;
      height: 100%;
      width: 100%;
      background-color: rgba(0, 0, 0, 0.5);
      z-index: 990;
      display: none;
    }}
    .overlay.show {{
      display: block;
    }}
    .main-content {{
      padding: 20px;
      margin-left: 0;
      margin-top: 90px;
      transition: margin-left 0.3s ease;
    }}
    @media (min-width: 768px) {{
      .sidebar {{
        left: 0;
      }}
      .main-content {{
        margin-left: 250px;
      }}
      .overlay {{
        display: none !important;
      }}
      #sidebarToggleBtn {{
        display: none;
      }}
    }}
    .content-section {{
      display: none;
    }}
    .content-section.active {{
      display: block;
    }}
    a {{
      text-decoration: none;
      color: black;
    }}
    a:hover {{
      color: rgb(19, 19, 73);
    }}
    .search-container {{
      z-index: 1050;
      position: relative;
      margin-top: 20px;
    }}
    .rounded-pill {{
      width: 300px;
      padding: 10px 20px;
      border: 2px solid #efbad0;
      border-radius: 50px;
      outline: none;
      box-shadow: 0 4px 10px rgba(239, 8, 201, 0.2);
      font-size: 16px;
    }}
    .search-button {{
      background-color: #f8fbff;
      border: none;
      border-radius: 50%;
      margin-left: -32px;
      cursor: pointer;
    }}
    .search-button:hover {{
      background-color: #f5f7f8;
      transform: scale(1.05);
    }}
    .submenu {{
      background-color: #f5f5f5;
      border-left: 2px solid #ccc;
    }}
    .submenu .nav-link {{
      padding-left: 30px;
      font-size: 0.95rem;
    }}
    .profile-btn {{
      background: linear-gradient(to right, #ff4500, #ff6347);
      color: white;
      border: none;
      border-radius: 25px;
      padding: 8px 18px;
      font-weight: 500;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
      transition: all 0.3s ease;
    }}
    .profile-btn:hover {{
      background: #d62900;
      color: #fff;
      transform: scale(1.05);
      box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }}
    /* Notification Bell Button Styling */
    .notification-btn {{
      position: relative;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      padding: 0;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .notification-badge {{
      position: absolute;
      top: 3px;
      right: 4px;
      width: 40px;
      font-size: 11px;
      padding: 2px 6px;
      border-radius: 50px;
      background-color: red;
      color: white;
      font-weight: bold;
      line-height: 1;
    }}
    #filterForm input[type="date"] {{
      width: 140px;
    }}
    #filterForm label {{
      font-size: 0.9rem;
      font-weight: 500;
    }}
  </style>
</head>
<body>

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
      <a href="user_profile.py?user_id={user_id}">
        <button class="btn profile-btn">
          <i class="bi bi-person-circle"></i> Profile
        </button>
      </a>
    </div>
  </div>
</nav>

<div class="sidebar" id="sidebar" style="box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
  <ul class="nav flex-column">
    <li class="nav-item">
      <a href="user.py?user_id={user_id}" class="nav-link " >Home</a>
    </li>
    <li class="nav-item">
      <a href="#" class="nav-link" onclick="toggleSubMenu('bookingSubMenu')">Booking <i class="bi bi-caret-down-fill"></i></a>
      <ul id="bookingSubMenu" class="nav flex-column ms-3 submenu d-none">
        <li><a href="approved_booking.py?user_id={user_id}" class="nav-link">On Going</a></li>
        <li><a href="completed_booking.py?user_id={user_id}" class="nav-link">Completed</a></li>
        <li><a href="cancelled_booking.py?user_id={user_id}" class="nav-link">Cancelled</a></li>
        <li><a href="rejected_booking.py?user_id={user_id}" class="nav-link">Rejected</a></li>
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

<div class="overlay" id="overlay"></div>

<div class="main-content">
  <div class="d-flex justify-content-between align-items-center mb-3">
    <h4>Notifications</h4>
  </div>

  <form id="filterForm" method="get" action="notification_users.py" class="d-flex align-items-center gap-2 mb-3" style="display:none;">
    <input type="hidden" name="user_id" value="{user_id}">
    <label for="start_date" class="mb-0">From:</label>
    <input type="date" id="start_date" name="start_date" class="form-control form-control-sm" required>
    <label for="end_date" class="mb-0">To:</label>
    <input type="date" id="end_date" name="end_date" class="form-control form-control-sm" required>
    <button type="submit" class="btn btn-sm btn-primary">Apply</button>
    <button type="button" id="filterResetBtn" class="btn btn-sm btn-secondary">Reset</button>
  </form>

  <div class="list-group" style="max-height: 400px; overflow-y: auto;">
""")

# Print notifications (if any)
if notifications:
    for notif_id, notif_text, notif_date, notif_status, image_url, shop_name in notifications:
        notif_date_str = notif_date.strftime("%Y-%m-%d %H:%M")
        print(f"""
    <div class="card mb-2 notification-card" id="notif-{notif_id}">
      <div class="card-body d-flex gap-3 align-items-center">
        <img src="images/{image_url}" alt="{shop_name}" style="width:50px; height:50px; object-fit:cover; border-radius:5px;">
        <div style="flex-grow:1;">
          <h6 class="card-title">{shop_name}</h6>
          <p class="card-text">{notif_text}</p>
        </div>
        <div class="text-end">
          <small class="text-muted">{notif_date_str}</small><br/>
        </div>
      </div>
    </div>
        """)
else:
    print("""
    <div class="alert alert-info" role="alert">
      No notifications found for the selected date range.
    </div>
    """)

# Close list-group and other containers, then JavaScript
print(f"""
  </div> </div> <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
<script>
  const sidebar = document.getElementById('sidebar');
  const overlay = document.getElementById('overlay');
  const toggleBtn = document.getElementById('sidebarToggleBtn');

  toggleBtn.addEventListener('click', function(evt) {{
    sidebar.classList.toggle('show');
    overlay.classList.toggle('show');
  }});

  overlay.addEventListener('click', function(evt) {{
    sidebar.classList.remove('show');
    overlay.classList.remove('show');
  }});

  function toggleSubMenu(id) {{
    const submenu = document.getElementById(id);
    if (submenu) {{
      submenu.classList.toggle('d-none');
    }}
  }}

  function showSection(id) {{
    const sections = document.querySelectorAll('.content-section');
    sections.forEach(section => {{
      section.classList.remove('active');
    }});
    const target = document.getElementById(id);
    if (target) {{
      target.classList.add('active');
    }}
    document.querySelectorAll('.sidebar .nav-link').forEach(link => {{
      link.classList.remove('active');
    }});
    if (event && event.target) {{
      event.target.classList.add('active');
    }}
    if (window.innerWidth < 768) {{
      sidebar.classList.remove('show');
      overlay.classList.remove('show');
    }}
  }}

  // This is the correct way to handle the filter form visibility
  const filterForm = document.getElementById('filterForm');
  const filterToggleBtn = document.getElementById('filterToggleBtn');

  filterToggleBtn.addEventListener('click', function() {{
    filterForm.style.display = (filterForm.style.display === 'none' || filterForm.style.display === '') ? 'flex' : 'none';
  }});

  document.getElementById('filterResetBtn').addEventListener('click', function() {{
    window.location.href = "notification_users.py?user_id={user_id}";
  }});

</script>

</body>
</html>
""")

con.close()