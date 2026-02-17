#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys
import pymysql, cgi, cgitb, html

sys.stdout.reconfigure(encoding='utf-8')
print("Content-Type: text/html\r\n\r\n")

cgitb.enable()
form = cgi.FieldStorage()
user_id = form.getvalue("user_id")

try:
    con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
    cur = con.cursor()

    # Fetch unseen notification count
    cur.execute("SELECT COUNT(*) FROM notifications WHERE user_id=%s AND status='unseen'", (user_id,))
    notification_count = cur.fetchone()[0]

    print("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title> View shops | RoadNova</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .navbar-custom {
      background-color: azure;
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
      background: linear-gradient(to right, #ff4500, #ff6347);
      color: white;
      border: none;
      border-radius: 25px;
      padding: 8px 18px;
      font-weight: 500;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
      transition: all 0.3s ease;
    }

    .profile-btn:hover {
      background: #d62900;
      color: #fff;
      transform: scale(1.05);
      box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }

    .card {
      border: 1px solid #e0e0e0;
      border-radius: 15px;
      background: #ffffff;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      overflow: hidden;
      height: 100%;
      display: flex;
      flex-direction: column;
    }

    .card:hover {
      transform: translateY(-8px);
      box-shadow: 0 16px 32px rgba(0, 0, 0, 0.2);
      background-color: #f8f9fa;
    }

    .card-img-top {
      height: 200px;
      object-fit: cover;
      border-top-left-radius: 14px;
      border-top-right-radius: 14px;
      transition: transform 0.3s ease;
    }

    .card:hover .card-img-top {
      transform: scale(1.05);
    }

    .card-body {
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .card-title {
      font-size: 1.4rem;
      font-weight: 700;
      color: #2c3e50;
      margin-bottom: 0.5rem;
    }

    .rating-stars {
      color: #ffc107;
      font-size: 1.2rem;
      margin-bottom: 0.75rem;
    }

    .card-text {
      font-size: 0.95rem;
      margin-bottom: 0.3rem;
      color: #555;
    }

    .card-text strong {
      font-weight: 600;
      color: #333;
    }

    .card-footer {
      background-color: transparent;
      border-top: 1px solid #f0f0f0;
      padding: 1rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .main-content {
      padding: 20px;
      margin-left: 250px!important;
      margin-top: 90px;
      transition: margin-left 0.3s ease;
    }

    @media (max-width: 768px) {
      .card {
        width: 100% !important;
        margin: 0 auto;
      }
      .main-content {
        margin-left: 0px!important;
      }
      .card-body {
        padding: 1rem;
      }
      .card-footer {
        text-align: center;
      }
      .card-footer button {
        width: 100%;
      }
    }
  </style>
</head>
<body>
""")

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
              <span style="position: absolute; top: -4px; font-weight: bold; font-size: 17px; color: white;">
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
          <a href="user.py?user_id={user_id}" class="nav-link">Home</a>
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
    """)

    # Fetch approved mechanic shops
    q = "SELECT * FROM mechanicshops WHERE status='Approved'"
    cur.execute(q)
    res = cur.fetchall()

    print("""
    <div class="main-content">
      <div class="container mt-4">
        <h2 class="mb-4 text-center text-primary" style="font-weight:600;">Available Mechanic Shops</h2>
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-4">
    """)

    for i in res:
        shop_id = i[0]
        shop_name = html.escape(str(i[10]))
        owner_name = html.escape(str(i[1]))
        email = html.escape(str(i[17]))
        phone = html.escape(str(i[4]))
        hours = html.escape(str(i[14]))
        shop_address = html.escape(str(i[11]))
        shop_image = html.escape(str(i[12]))

        # Get ratings
        cur.execute("SELECT rating FROM reviews WHERE shop_id=%s", (shop_id,))
        ratings = cur.fetchall()

        if ratings:
            avg_rating = sum(r[0] for r in ratings) / len(ratings)
            rounded_rating = round(avg_rating)
            stars_html = f"<span class='rating-stars'>{'★' * rounded_rating}{'☆' * (5 - rounded_rating)}</span>"
        else:
            stars_html = f"<span class='rating-stars'>{'☆' * 5}</span>"

        print(f"""
        <div class="col">
          <div class="card shadow-sm">
            <img src="images/{shop_image}" class="card-img-top" alt="{shop_name}">
            <div class="card-body">
              <h5 class="card-title">{shop_name}</h5>
              {stars_html}
              <p class="card-text"><i class="bi bi-geo-alt-fill me-2"></i><strong>Address:</strong> {shop_address}</p>
              <p class="card-text"><i class="bi bi-person me-2"></i><strong>Owner:</strong> {owner_name}</p>
              <p class="card-text"><i class="bi bi-clock me-2"></i><strong>Hours:</strong> {hours}</p>
            </div>
            <div class="card-footer">
              <button type="button" class="btn btn-info btn-sm me-2" data-bs-toggle="modal" data-bs-target="#servicesModal{shop_id}">
                <i class="bi bi-eye-fill"></i> View Services
              </button>
              <a href="https://www.google.com/maps/search/?api=1&query={shop_address.replace(' ', '+')}" target="_blank" class="btn btn-outline-primary btn-sm me-2">
                <i class="bi bi-geo-alt-fill"></i> View on Map
              </a>
              <button type="button" class="btn btn-danger btn-sm" data-bs-toggle="modal" data-bs-target="#serviceModal{shop_id}">
                <i class="bi bi-tools"></i> Request Service
              </button>
            </div>
          </div>
        </div>
        """)

        # Services Modal
        cur.execute("SELECT service_name, price FROM services WHERE shop_id=%s", (shop_id,))
        services = cur.fetchall()
        service_list_html = "<ul class='list-group'>"
        for svc in services:
            service_name_esc = html.escape(str(svc[0]))
            price_esc = html.escape(str(svc[1]))
            service_list_html += f"""
                        <li class="list-group-item d-flex justify-content-between align-items-center">
                          {service_name_esc}
                          <span class="badge bg-primary rounded-pill">₹{price_esc}</span>
                        </li>
                        """
        service_list_html += "</ul>"

        print(f"""
        <div class="modal fade" id="servicesModal{shop_id}" tabindex="-1" aria-labelledby="servicesModalLabel{shop_id}" aria-hidden="true">
          <div class="modal-dialog modal-lg modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header bg-info text-white">
                <h5 class="modal-title" id="servicesModalLabel{shop_id}">Services at {shop_name}</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                {service_list_html if services else '<p class="text-muted">No services available for this shop.</p>'}
              </div>
              <div class="modal-footer">
                <button class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>
        """)

        # Service Request Modal
        cur.execute("SELECT service_name FROM services WHERE shop_id=%s", (shop_id,))
        service_options = cur.fetchall()
        service_options_html = ""
        for s in service_options:
            service_name_esc = html.escape(str(s[0]))
            service_options_html += f"<option value='{service_name_esc}'>{service_name_esc}</option>"

        print(f"""
        <div class="modal fade" id="serviceModal{shop_id}" tabindex="-1" aria-labelledby="serviceModalLabel{shop_id}" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <form method="post" action="request_service.py" onsubmit="return service(event)">
                <div class="modal-header">
                  <h5 class="modal-title" id="serviceModalLabel{shop_id}" style="color:black;">Request Service from {shop_name}</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <img src="./images/{shop_image}" width="250px" height="100px" alt="shop image" style="margin-left:100px">
                  <p style="color:black;"><strong>Address:</strong> {shop_address}</p>
                  <p style="color:black;"><strong>Contact:</strong> {phone}</p>
                  <input type="hidden" name="user_id" value="{user_id}">
                  <input type="hidden" name="shop_id" value="{shop_id}">
                  <input type="hidden" name="shop_name" value="{shop_name}">
                  <input type="hidden" name="email" value="{email}">

                  <div class="mb-3">
                    <label for="service_name{shop_id}" class="form-label" style="color:black;">Select Service</label>
                    <select class="form-select" id="service_name{shop_id}" name="service_name" required>
                      <option value="">-- Choose a service --</option>
                      {service_options_html if service_options else '<option disabled>No services available</option>'}
                      <option value="other">other</option>
                    </select>
                  </div>

                  <div class="mb-3">
                    <label for="vehicle_type{shop_id}" class="form-label" style="color:black;">Vehicle Type</label>
                    <select class="form-select" id="vehicle_type{shop_id}" name="vehicle_type" required>
                      <option value="">-- Choose type of vehicle --</option>
                      <option value="Two Wheeler">Two-Wheeler</option>
                      <option value="Three Wheeler">Three-Wheeler</option>
                      <option value="Four Wheeler">Four-Wheeler</option>
                      <option value="Multi Wheeler">Multi-Wheeler</option>
                    </select>
                  </div>

                  <div class="mb-3">
                    <label for="vehicle_brand{shop_id}" class="form-label" style="color:black;">Brand</label>
                    <input type="text" class="form-control" id="vehicle_brand{shop_id}" name="vehicle_brand" required>
                  </div>

                  <div class="mb-3">
                    <label for="reg_number{shop_id}" class="form-label" style="color:black;">Registration Number</label>
                    <input type="text" class="form-control" id="registration_number_{shop_id}" name="registration_number" required>
                  </div>

                  <div class="mb-3">
                    <label for="user_location{shop_id}" class="form-label" style="color:black;">Your Current Location</label>
                    <input type="text" class="form-control" id="user_location{shop_id}" name="user_location" placeholder="Enter your current location" required>
                  </div>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                  <button type="submit" class="btn btn-primary">Submit Request</button>
                </div>
              </form>
            </div>
          </div>
        </div>
        """)

    print("""
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
    </script>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """)

except pymysql.MySQLError as e:
    print(f"<h3 style='color:red;'>Database Error: {e}</h3>")
except Exception as e:
    print(f"<h3 style='color:red;'>An unexpected error occurred: {e}</h3>")
finally:
    if 'con' in locals() and con.open:
        cur.close()
        con.close()