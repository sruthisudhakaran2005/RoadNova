#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print("content-type:text/html\r\n\r\n")

import pymysql
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
user_id = form.getvalue("user_id")

con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
query = """
SELECT 
    sr.request_id,
    ms.shop_name,
    sr.problem_type,
    sr.refund_date,
    sr.refund,
    sr.status,
    sr.cancelled_date
FROM 
    service_requests sr
JOIN 
    mechanicshops ms ON sr.shop_id = ms.id
WHERE 
    sr.user_id = %s AND sr.status = 'Cancelled'
"""
cur.execute(query, (user_id,))
bookings = cur.fetchall()
q = "SELECT * FROM users WHERE user_id=%s"
cur.execute(q, (user_id,))
res = cur.fetchall()
cur.execute("SELECT COUNT(*) FROM notifications WHERE user_id=%s AND status='unseen'", (user_id,))
notification_count = cur.fetchone()[0]
print("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Cancelled Bookings | RoadNova</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" />
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

    h2 {
      color: #dc3545; /* Bootstrap danger red */
      margin-bottom: 20px;
    }
    table {
      background-color: white;
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(220, 53, 69, 0.2);
    }
    th {
      background-color: #dc3545;
      color: black;
      text-align: center;
    }
    td {
      vertical-align: middle;
      text-align: center;
    }
    tbody tr:hover {
      background-color: #f8d7da;
    }
    .no-data {
      font-style: italic;
      color: #6c757d;
      margin-top: 30px;
      text-align: center;
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
print("""
<div class="main-content">
<div class="container">
    <h2>Cancelled Bookings</h2>""")
if bookings:
    print("""
    <div class="table-responsive">
      <table class="table table-bordered table-hover">
        <thead>
          <tr>
            <th>SN</th>
            <th>Cancelled Date</th>
            <th>Shop Name</th>
            <th>Service</th>
            <th>Refund Details</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
    """)
    for i, booking in enumerate(bookings, start=1):
        booking_id, shop_name, service_name, refund_date, refund, status, cancelled_date = booking

        # Format refund info for modal
        refund_text = f"₹{refund:.2f}" if refund is not None and refund > 0 else "No refund amount found"
        # Format refund date to show day, month, year, hour, minute, and AM/PM
        formatted_date = cancelled_date.strftime("%d %B %Y ") if cancelled_date else 'N/A'
        format_date = refund_date.strftime("%d %B %Y ") if refund_date else 'N/A'

        # Modal id unique per booking
        modal_id = f"refundModal{i}"

        print(f"""
              <tr>
                <td>{i}</td>
                <td>{formatted_date}</td>
                <td>{shop_name}</td>
                <td>{service_name}</td>
                <td>
                  <button type="button" class="btn btn-info btn-sm" data-bs-toggle="modal" data-bs-target="#{modal_id}">
                    View Refund
                  </button>

                  <div class="modal fade" id="{modal_id}" tabindex="-1" aria-labelledby="{modal_id}Label" aria-hidden="true">
                    <div class="modal-dialog">
                      <div class="modal-content">
                        <div class="modal-header">
                          <h5 class="modal-title" id="{modal_id}Label">Refund Details</h5>
                          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                          <p><strong>Refund Amount:</strong> {refund_text}</p>
                          {f'<p><strong>Refund Date:</strong> {format_date}</p>' if refund is not None and refund > 0 else ''}

                        </div>
                        <div class="modal-footer">
                          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        </div>
                      </div>
                    </div>
                  </div>
                </td>
                <td><span class="badge bg-danger">{status}</span></td>
              </tr>
            """)

    print("""
        </tbody>
      </table>
    </div>
    """)
else:
    print('<p class="no-data">You have no cancelled bookings.</p>')

# Close HTML
print(f"""
</div>
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