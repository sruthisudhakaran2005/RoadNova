#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Content-Type: text/html\r\n\r\n")

import pymysql, cgi, cgitb
cgitb.enable()

try:
    # Connect to DB
    con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
    cur = con.cursor()

    # Get form data
    form = cgi.FieldStorage()
    user_id = form.getvalue("user_id")
    cur.execute("SELECT COUNT(*) FROM notifications WHERE user_id=%s AND status='unseen'", (user_id,))
    notification_count = cur.fetchone()[0]
    # HTML Start
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Rejected Booking | RoadNova</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">
      <style>
        .card-title { font-weight: bold; color: #198754; }
        .modal-header { background-color: #0d6efd; color: white; }
        .badge-completed { background-color: #198754; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        .navbar-custom { background-color: azure; }
        .mainhead { font-weight: 500; }
        .sidebar { position: fixed; top: 74px; left: -250px; width: 250px; height: 100%; background-color: rgb(253, 248, 248); padding-top: 30px; transition: all 0.3s ease; z-index: 1000; }
        .sidebar.show { left: 0; }
        .sidebar .nav-link { color: #0b0b0b; padding: 15px 20px; }
        .sidebar .nav-link:hover, .sidebar .nav-link.active { background-color: #e2cccc; color: rgb(250, 4, 4); }
        .overlay { top: 0; left: 0; height: 100%; width: 100%; background-color: rgba(0, 0, 0, 0.5); z-index: 990; display: none; }
        .overlay.show { display: block; }
        .main-content { padding: 20px; margin-left: 0; margin-top: 90px; transition: margin-left 0.3s ease; }
        @media (min-width: 768px) { .sidebar { left: 0; } .main-content { margin-left: 250px; } .overlay { display: none !important; } #sidebarToggleBtn { display: none; } }
        .submenu { background-color: #f5f5f5; border-left: 2px solid #ccc; }
        .submenu .nav-link { padding-left: 30px; font-size: 0.95rem; }
        .profile-btn { background: linear-gradient(to right, #ff4500, #ff6347); color: white; border: none; border-radius: 25px; padding: 8px 18px; font-weight: 500; box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: all 0.3s ease; }
        .profile-btn:hover { background: #d62900; color: #fff; transform: scale(1.05); box-shadow: 0 6px 12px rgba(0,0,0,0.15); }
        .container { margin-top: 20px; margin-left: auto; margin-right: auto; max-width: 1200px; width: 95%; }
        .table thead { background-color: #343a40; color: white; }
        .table tbody tr:hover { background-color: #f8f9fa; }
        .card-title { font-weight: bold; color: #dc3545; }
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

    # Navbar and Sidebar HTML with user_id inserted properly
    print(f"""
    <nav class="navbar navbar-expand-lg navbar-custom fixed-top py-2">
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
          </button></a>
        </div>
      </div>
    </nav>

    <div class="sidebar" id="sidebar">
      <ul class="nav flex-column">
        <li class="nav-item"><a href="user.py?user_id={user_id}" class="nav-link">Home</a></li>
        <li class="nav-item">
          <a href="#" class="nav-link" onclick="toggleSubMenu('bookingSubMenu'); return false;">Booking <i class="bi bi-caret-down-fill"></i></a>
          <ul id="bookingSubMenu" class="nav flex-column ms-3 submenu d-none">
             <li><a href="approved_booking.py?user_id={user_id}" class="nav-link">On Going</a></li>
             <li><a href="completed_booking.py?user_id={user_id}" class="nav-link">Completed</a></li>
             <li><a href="cancelled_booking.py?user_id={user_id}" class="nav-link">Cancelled</a></li>
             <li><a href="rejected_booking.py?user_id={user_id}" class="nav-link">Rejected</a></li>
          </ul>
        </li>
        <li class="nav-item"><a href="shops.py?user_id={user_id}" class="nav-link">Mechanic shops</a></li>
        <li class="nav-item"><a href="home.py" class="nav-link">Logout</a></li>
      </ul>
    </div>
    """)

    print("""
    <div class="main-content">
      <div class="container">
        <h2 class="mb-4 text-center text-failed">Rejects Requests</h2>
        """)
    print("""
                <div class="table-responsive">
                  <table class="table table-bordered table-striped">
                    <thead>
                      <tr>
                        <th>S.NO</th>
                        <th>Shop Name</th>
                        <th>Problem Description</th>
                        <th>Request Date</th>
                        <th>Status</th>
                      </tr>
                    </thead>
                    <tbody>
                """)
    x = """select * from service_requests where status='Rejected' and user_id=%s """%(user_id)
    cur.execute(x)
    r = cur.fetchall()

    if r is not None:
        for index, i in enumerate(r, 1):
            request_id = i[0]
            shop_id =i[2]
            problem = i[3]
            date = i[4]
            q = """select shop_name from mechanicshops where id=%s """ % (shop_id)
            cur.execute(q)
            res = cur.fetchone()
            if res is not None:
                shop_name = res[0]

            print(f"""
                        <tr>
                          <td>{index}</td>
                          <td>{shop_name}</td>
                          <td>{problem}</td>
                          <td>{date.strftime('%d-%m-%Y')}</td>
                          <td><span class="badge bg-danger">Rejected</span></td>
                        </tr>
                      """)
    else:
        print("""<h3>No Rejected services</h3>""")




    print("""
      </div>
    </div>
    <script>
      const sidebar = document.getElementById('sidebar');
      const toggleBtn = document.getElementById('sidebarToggleBtn');
      toggleBtn.addEventListener('click', () => { sidebar.classList.toggle('show'); });
      function toggleSubMenu(id) {
        const submenu = document.getElementById(id);
        submenu.classList.toggle('d-none');
      }
    </script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """)

except Exception as e:
    print(f"<pre>Error: {e}</pre>")

finally:
    con.close()
