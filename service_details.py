#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe

print("Content-Type: text/html\r\n\r\n")

import pymysql, cgi, cgitb, html, sys
from datetime import datetime
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')
cgitb.enable()

form = cgi.FieldStorage()
shop_id = form.getvalue("shop_id")
status_filter = form.getvalue("status_filter", "all")
from_date = form.getvalue("from_date", "")
to_date = form.getvalue("to_date", "")

# DB Connection
try:
    con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
    cur = con.cursor()
except pymysql.MySQLError as e:
    print(f"<p>Database connection failed: {e}</p>")
    sys.exit()

# Get Admin Profile Image
cur.execute("SELECT image FROM admin WHERE id=1")
result = cur.fetchone()
profile = result[0] if result else "default.jpg"

print("""
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>All Service Requests - Admin</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
  <style>
    body { min-height: 100vh; display: flex; flex-direction: column; }
    .sidebar { min-height: 100vh; max-height: auto; }
    .sidebar .nav-link { color: #710019; }
    .sidebar .nav-link.active, .sidebar .nav-link:hover { background-color: #f7bec0; color: black; }
    .content-section { display: none; }
    .active-section { display: block; }
    @media (max-width: 768px) {
      .sidebar { position: fixed; top: 56px; left: -200px; width: 200px!important; z-index: 1031; transition: left 0.3s ease-in-out; }
      .sidebar.show { left: 0; }
      .overlay { display: none; position: fixed; top: 56px; left: 0; right: 0; bottom: 0; background-color: rgba(0, 0, 0, 0.5); z-index: 1030; }
      .overlay.show { display: block; }
      form label { margin-left: 0 !important; font-size: medium !important; display: block; margin-bottom: 10px; }
      form select { width: 200px!important; max-width: none !important; }
    }
    .navbar-brand { color: #c85250!important; }
    .main { background-color: #f8f9fa; padding: 20px; }
    .modal-title { font-weight: 600; }
   .table .status-completed { color: #28a745 !important; font-weight: bold !important; }
  .table .status-rejected { color: #dc3545 !important; font-weight: bold !important; }
  .table .status-cancelled { color: #6c757d !important; font-weight: bold !important; }
  .table .status-pending { color: #ffc107 !important; font-weight: bold !important; }
  .table .status-approved { color: #007bff !important; font-weight: bold !important; }

  </style>
</head>
<body>
""")

print(f"""
  <nav class="navbar navbar-dark bg-white fixed-top" style="box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
    <div class="container-fluid">
      <button class="btn btn-outline-dark d-md-none me-2" type="button" onclick="toggleSidebar()" style="color:5F9EA0">
        <i class="bi bi-list"></i>
      </button>
      <span class="navbar-brand mb-0 h1">RoadNova</span>
      <div class="d-flex align-items-center ms-auto">
        <img src="images/{profile}" alt="Admin Profile" class="rounded-circle" style="width:40px; height:40px; object-fit:cover;"/>
      </div>
    </div>
  </nav>
""")

print("""
<div class="container-fluid" style="padding-top: 56px;">
  <div class="row">

    <nav class="col-md-3 col-lg-2 d-md-block sidebar collapse" style="background-color:#fadcd9;color:#710019" id="sidebarMenu">
      <div class="position-sticky pt-3 text-white">
        <h5 class="px-3 mb-3">Admin Dashboard</h5>
        <ul class="nav flex-column">
          <li class="nav-item">
            <a class="nav-link active" href="admin.py">
              <i class="bi bi-speedometer2 me-2"></i>Dashboard
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse" href="#usersSubmenu" role="button" aria-expanded="false">
              <span><i class="bi bi-people me-2"></i>Users</span>
              <i class="bi bi-chevron-down small"></i>
            </a>
            <div class="collapse" id="usersSubmenu">
              <ul class="nav flex-column ms-3">
                <li><a href="viewuser.py" class="nav-link"><i class="bi bi-person me-2"></i>View Users</a></li>
              </ul>
            </div>
          </li>
          <li class="nav-item">
            <a class="nav-link d-flex justify-content-between align-items-center"  data-bs-toggle="collapse"  href="#mechanicsSubmenu" role="button" aria-expanded="false">
              <span><i class="bi bi-tools me-2"></i>Shop owners</span>
              <i class="bi bi-chevron-down small"></i>
            </a>
            <div class="collapse" id="mechanicsSubmenu">
              <ul class="nav flex-column ms-3">
                <li><a href="new_requests.py" class="nav-link"><i class="bi bi-person me-2"></i>New Requests</a></li>
                <li><a href="approved.py" class="nav-link"><i class="bi bi-person me-2"></i>Approved shops</a></li>
                <li><a href="rejected.py" class="nav-link"><i class="bi bi-person me-2"></i>Rejected shops</a></li>
                <li><a href="blocked.py" class="nav-link"><i class="bi bi-person me-2"></i>Blocked shops</a></li>
              </ul>
            </div>
          </li>
          <li class="nav-item">
            <a class="nav-link d-flex justify-content-between align-items-center" href="all_requests.py">
              <span><i class="bi-envelope"></i>Service Requests</span>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link d-flex justify-content-between align-items-center"  href="home.py" role="button" aria-expanded="false">
              <span><i class="bi bi-gear me-2"></i>Logout</span>
            </a>
          </li>
        </ul>
      </div>
    </nav>

    <main id="mainContent" class="col-md-9 col-lg-10 ms-sm-auto px-md-4" style="padding-top: 20px;">
""")

print(f"""
<div class="container">
  <h2 class="text-center mb-4">📋 All Service Requests by Shop</h2>
  <form id="filterForm" action="service_details.py" method="get" class="mb-3 d-flex flex-wrap align-items-center justify-content-between">
    <input type="hidden" name="shop_id" value="{shop_id}">
    <div class="d-flex align-items-center mb-2 mb-md-0">
      <label for="status_filter" class="form-label mb-0 me-2 fw-bold">Filter by Status:</label>
      <select class="form-select w-auto me-3" id="status_filter" name="status_filter" onchange="this.form.submit()">
        <option value="all" {"selected" if status_filter == "all" else ""}>All</option>
        <option value="pending" {"selected" if status_filter == "pending" else ""}>Pending</option>
        <option value="completed" {"selected" if status_filter == "completed" else ""}>Completed</option>
        <option value="approved" {"selected" if status_filter == "approved" else ""}>Approved</option>
        <option value="rejected" {"selected" if status_filter == "rejected" else ""}>Rejected</option>
        <option value="cancelled" {"selected" if status_filter == "cancelled" else ""}>Cancelled</option>
      </select>
    </div>
    <div class="d-flex align-items-center mb-2 mb-md-0">
      <label for="from_date" class="form-label mb-0 me-2 fw-bold">From:</label>
      <input type="date" class="form-control me-2" id="from_date" name="from_date" value="{from_date}">
      <label for="to_date" class="form-label mb-0 me-2 fw-bold">To:</label>
      <input type="date" class="form-control me-2" id="to_date" name="to_date" value="{to_date}">
      <button type="submit" class="btn btn-primary me-2">Filter</button>
      <button type="button" class="btn btn-outline-secondary" onclick="clearDateFilter()">Clear </button>
    </div>
  </form>
  <div class="table-responsive">
    <table class="table table-bordered table-striped align-middle">
      <thead class="table-dark text-center">
        <tr>
          <th>S.No</th>
          <th>Date</th>
          <th>Issue</th>
          <th>Assisted By</th>
          <th>Customer Name</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
""")

# Build the base query and parameters
query = "SELECT * FROM service_requests WHERE shop_id = %s"
params = [shop_id]

# Add status filter
if status_filter != "all":
    query += " AND status = %s"
    params.append(status_filter)

# Add date range filter
if from_date and to_date:
    query += " AND request_date BETWEEN %s AND %s"
    params.append(from_date)
    params.append(to_date)
elif from_date:
    query += " AND request_date >= %s"
    params.append(from_date)
elif to_date:
    query += " AND request_date <= %s"
    params.append(to_date)

# Execute the query
cur.execute(query, tuple(params))
res = cur.fetchall()

for idx, request in enumerate(res, start=1):
    request_id, user_id, user_location, issue, date_from_db, status, mech_id = request[:7]

    # Clean the status string to prevent issues with whitespace or case
    status_cleaned = str(status).strip().lower()

    try:
        formatted_date = date_from_db.strftime('%d/%m/%Y %I:%M %p')
    except (TypeError, ValueError):
        formatted_date = str(date_from_db)

    # Fetch user name for the current request
    cur.execute("SELECT name FROM users WHERE user_id = %s", (user_id,))
    user_data = cur.fetchone()
    user_name = user_data[0] if user_data else "N/A"

    # Fetch mechanic name for the current request
    cur.execute("SELECT name FROM mechanics WHERE mech_id = %s", (mech_id,))
    mech_data = cur.fetchone()
    mech_name = mech_data[0] if mech_data else "N/A"

    # Determine the CSS class based on the cleaned status
    status_class = ""
    if status_cleaned == "completed":
        status_class = "status-completed"
    elif status_cleaned == "rejected":
        status_class = "status-rejected"
    elif status_cleaned == "cancelled":
        status_class = "status-cancelled"
    elif status_cleaned == "pending":
        status_class = "status-pending"
    elif status_cleaned == "approved":
        status_class = "status-approved"

    # Use the original status variable for display, but the cleaned one for the class
    print(f"""
          <tr class="text-center">
            <td>{idx}</td>
            <td>{formatted_date}</td>
            <td>{issue}</td>
            <td>{mech_name}</td>
            <td>{user_name}</td>
            <td class="{status_class}">{status}</td>
          </tr>
          """)

print("""
      </tbody>
    </table>
  </div>
</div>
""")

print("""
    </main>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<script>
  function toggleSidebar() {
    const sidebar = document.getElementById('sidebarMenu');
    sidebar.classList.toggle('show');
  }

  function clearDateFilter() {
    document.getElementById('from_date').value = '';
    document.getElementById('to_date').value = '';
    document.getElementById('filterForm').submit();
  }
</script>
</body>
</html>
""")

# Close DB connection
cur.close()
con.close()