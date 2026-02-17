#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

import cgi, cgitb
import pymysql

cgitb.enable()
print("Content-type: text/html\n")

form = cgi.FieldStorage()
shop_id = form.getvalue("id")

services = []
error_msg = ""
if shop_id:
    try:
        con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
        cur = con.cursor()
        query = "SELECT service_id, service_name, price, added FROM services WHERE shop_id=%s"
        cur.execute(query, (shop_id,))
        services = cur.fetchall()

    except Exception as e:
        error_msg = f"Error fetching services: {str(e)}"
else:
    error_msg = "Shop ID not provided."
q = """ select * from mechanicshops where id="%s" """%(shop_id)
cur.execute(q)

res = cur.fetchall()
con.close()
for i in res:
    profile_img = i[9]
    shop_name = i[10]
    print(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <title>View Services | RoadNova</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" />
      <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet" />
      <style>
        .sidebar {{
          color: #050a30;
          min-height: 100vh;
        }}
        .sidebar .nav-link {{
          color: #050a30;
        }}
        .sidebar .nav-link:hover,
        .sidebar .nav-link.active {{
          background-color: #2e8bc0;
          color: white;
        }}
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

        .container {{
          max-width: 900px;
          margin: auto;
          padding: 20px;
        }}

        h2 {{
          color: #3a66cc; /* medium blue */
          margin-bottom: 30px;
          text-align: center;
        }}

        table {{
          width: 100%;
          border-collapse: collapse;
          background-color: white;
          box-shadow: 0 4px 12px rgba(58, 102, 204, 0.2);
          border-radius: 10px;
          overflow: hidden;
        }}

        thead {{
          background-color: #5a86e6; /* lighter blue */
          color: white;
        }}

        th, td {{
          padding: 12px 15px;
          text-align: left;
        }}

        tbody tr {{
          border-bottom: 1px solid #d0d9f7;
          transition: background-color 0.25s ease;
        }}

        tbody tr:hover {{
          background-color: #dbe6ff;
        }}

        .price {{
          color: #2a4d99; /* dark blue */
          font-weight: 700;
        }}

        .edit-btn {{
          display: inline-flex;
          align-items: center;
          padding: 6px 12px;
          font-size: 0.9rem;
          font-weight: 600;
          color: #3a66cc;
          border: 2px solid #3a66cc;
          border-radius: 8px;
          background-color: transparent;
          cursor: pointer;
          transition: background-color 0.3s, color 0.3s;
          text-decoration: none;
        }}

        .edit-btn:hover {{
          background-color: #3a66cc;
          color: white;
          text-decoration: none;
        }}

        .edit-btn i {{
          margin-right: 6px;
        }}

        .no-services {{
          text-align: center;
          color: #666;
          margin-top: 50px;
          font-size: 1.2rem;
        }}

        @media (max-width: 600px) {{
          table, thead, tbody, th, td, tr {{
            display: block;
          }}

          thead tr {{
            position: absolute;
            top: -9999px;
            left: -9999px;
          }}

          tbody tr {{
            margin-bottom: 20px;
            border-bottom: 2px solid #aabfff;
            border-radius: 10px;
            padding: 15px;
            background-color: white;
            box-shadow: 0 4px 8px rgba(58, 102, 204, 0.1);
          }}

          tbody td {{
            padding-left: 50%;
            position: relative;
            text-align: right;
          }}

          tbody td::before {{
            position: absolute;
            top: 12px;
            left: 15px;
            width: 45%;
            padding-right: 10px;
            white-space: nowrap;
            font-weight: 700;
            text-align: left;
            color: #3a66cc;
            content: attr(data-label);
          }}

          .edit-btn {{
            width: 100%;
            text-align: center;
            padding: 10px 0;
            margin-top: 10px;
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
        <nav class="col-md-3 col-lg-2 sidebar d-md-block p-0" id="sidebarMenu" style="background-color:#b1d4e0">
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
      <h2>Services Offered</h2>
      <div class="container">
    """)

    if services:
        print('''
        <table>
          <thead>
            <tr>
              <th>date </th>
              <th>Service Name</th>
              <th>Price (₹)</th>
              <th>Edit</th>
            </tr>
          </thead>
          <tbody>
        ''')
        for service_id, service_name, price, added in services:
            print(f"""
            <tr>
              <td data-label="Date">{added.strftime('%d-%m-%Y')}</td>
              <td data-label="Service Name">{service_name}</td>
              <td data-label="Price" class="price">₹ {price}</td>
              <td data-label="Edit">
                <a href="edit_service.py?id={service_id}" class="edit-btn" title="Edit Service">
                  <i class="bi bi-pencil-fill"></i> Edit
                </a>
              </td>
            </tr>
            """)
        print("""
          </tbody>
        </table>
        """)
    else:
        msg = error_msg if error_msg else "No services available yet."
        print(f'<div class="no-services">{msg}</div>')

    print("""
      </div>
      </main>
      <script>
       const toggleBtn = document.getElementById('toggleSidebar');
  const sidebar = document.getElementById('sidebarMenu');
  const overlay = document.getElementById('overlay');

  toggleBtn.addEventListener('click', () => {
    sidebar.classList.toggle('show');
    overlay.classList.toggle('show');
  });

  overlay.addEventListener('click', () => {
    sidebar.classList.remove('show');
    overlay.classList.remove('show');
  });
            </script>
      <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js"></script>

    </body>
    </html>
    """)


