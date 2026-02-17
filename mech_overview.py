#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe

print("Content-Type: text/html\r\n\r\n")

import pymysql, cgi, cgitb, html, sys
from datetime import datetime
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')
cgitb.enable()

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

# Fetch all relevant service request data
cur.execute("""
    SELECT 
        r.request_id, r.status, r.price, r.extra_charge,
        s.id, s.shop_name, s.owner_email, s.phone, s.address, s.owner_name
    FROM service_requests r
    JOIN mechanicshops s ON r.shop_id = s.id
""")
requests_data = cur.fetchall()

# Group data by shop and calculate metrics
shops_data = defaultdict(lambda: {
    'requests': [],
    'completed_count': 0,
    'total_revenue': 0,
    'details': None
})

for row in requests_data:
    (req_id, status, price, extra_charge,
     shop_id, shop_name, semail, sphone, saddr, owner_name) = row

    if shops_data[shop_id]['details'] is None:
        shops_data[shop_id]['details'] = {
            'shop_name': shop_name,
            'semail': semail,
            'sphone': sphone,
            'saddr': saddr,
            'owner_name': owner_name
        }

    if status.lower() == 'completed':
        shops_data[shop_id]['completed_count'] += 1
        total_price = (price or 0) + (extra_charge or 0)
        shops_data[shop_id]['total_revenue'] += total_price

# --- HTML Generation ---

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

print("""
<div class="container">
  <h2 class="text-center mb-4">📋 All Service Requests by Shop</h2>
  <div class="table-responsive">
    <table class="table table-bordered table-striped align-middle">
      <thead class="table-dark text-center">
        <tr>
          <th>S.No</th>
          <th>Shop Name</th>
          <th>Shop Details</th>
          <th>Completed Requests</th>
          <th>Total Revenue</th>
          <th>Rating</th>
        </tr>
      </thead>
      <tbody>
""")

# Initialize a string to hold all the modal HTML
modals_html = ""

if shops_data:
    s_no = 1
    for shop_id, data in shops_data.items():
        details = data['details']
        completed_count = data['completed_count']
        total_revenue = data['total_revenue']

        shop_name_safe = html.escape(details['shop_name'])
        owner_name_safe = html.escape(details['owner_name'])
        semail_safe = html.escape(details['semail'])
        sphone_safe = html.escape(details['sphone'])
        saddr_safe = html.escape(details['saddr'])

        print(f"""
        <tr class="text-center">
          <td>{s_no}</td>
          <td>{shop_name_safe}</td>
          <td>
            <button class="btn btn-sm btn-outline-primary" data-bs-toggle="modal" data-bs-target="#shopModal{shop_id}">
              🏪 View
            </button>
          </td>
          <td> <button class="btn btn-sm btn-outline-warning" data-bs-toggle="modal" data-bs-target="#completedModal{shop_id}">
             Total: {completed_count}-View Details
            </button>
          </td>
          <td>₹{total_revenue:.2f}</td>
          <td>⭐ N/A</td>
        </tr>
        """)

        # --- Append Shop Details Modal to the string ---
        modals_html += f"""
        <div class="modal fade" id="shopModal{shop_id}" tabindex="-1">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header bg-primary text-white">
                <h5 class="modal-title">Shop Details</h5>
                <button class="btn-close" data-bs-dismiss="modal"></button>
              </div>
              <div class="modal-body">
                <p><strong>Shop Name:</strong> {shop_name_safe}</p>
                <p><strong>Owner:</strong> {owner_name_safe}</p>
                <p><strong>Email:</strong> {semail_safe}</p>
                <p><strong>Phone:</strong> {sphone_safe}</p>
                <p><strong>Address:</strong> {saddr_safe}</p>
              </div>
              <div class="modal-footer">
                <button class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>
        """

        # --- Append Completed Requests Modal to the string ---
        cur.execute("""
            SELECT sr.request_id, sr.request_date, sr.completed_date, sr.problem_type, sr.location,
                   sr.mech_id, m.name, m.image, sr.total_charge, sr.user_id
            FROM service_requests sr
            JOIN mechanics m ON sr.mech_id = m.mech_id
            WHERE sr.shop_id = %s AND sr.status = 'completed'
        """, (shop_id,))
        mech_reqs = cur.fetchall()
        mechanic_tasks = defaultdict(lambda: {'name': '', 'image': '', 'requests': []})
        for (req_id, req_date, comp_date, problem, location, mech_id, mech_name, mech_img, total_charge,
             user_id) in mech_reqs:
            mechanic_tasks[mech_id]['name'] = mech_name
            mechanic_tasks[mech_id]['image'] = mech_img
            mechanic_tasks[mech_id]['requests'].append(
                (req_id, req_date, comp_date, problem, location, total_charge, user_id)
            )

        inner_modals_html = ""
        if mechanic_tasks:
            for mech_id, mdata in mechanic_tasks.items():
                inner_modals_html += f"""
                  <div class="col-md-4 mb-3">
                    <div class="card text-center" style="cursor:pointer;" data-bs-toggle="modal" data-bs-target="#mechModal{mech_id}_{shop_id}">
                      <img src="images/{mdata['image']}" class="card-img-top" alt="{html.escape(mdata['name'])}" style="height:150px; object-fit:cover;">
                      <div class="card-body">
                        <h5 class="card-title">{html.escape(mdata['name'])}</h5>
                        <p class="card-text">🛠️ {len(mdata['requests'])} Completed</p>
                      </div>
                    </div>
                  </div>
                """

                # --- Append Mechanic's Detailed Modal to the string ---
                table_rows = ""
                for i, (req_id, req_date, comp_date, problem, location, total_charge, user_id) in enumerate(
                        mdata['requests'], 1):
                    cur.execute("SELECT name, email, phone FROM users WHERE user_id = %s", (user_id,))
                    user_details = cur.fetchone()
                    user_name = html.escape(user_details[0]) if user_details else 'N/A'
                    user_email = html.escape(user_details[1]) if user_details else 'N/A'
                    user_phone = html.escape(user_details[2]) if user_details else 'N/A'

                    table_rows += f"""
                    <tr>
                      <td>{i}</td>
                      <td>{req_date}</td>
                      <td>{comp_date or 'N/A'}</td>
                      <td>{html.escape(problem)}</td>
                      <td>{html.escape(location)}</td>
                      <td>₹{total_charge:.2f}</td>
                      <td>
                        <button class="btn btn-sm btn-outline-success" data-bs-toggle="modal" data-bs-target="#custModal{req_id}">
                          👤 View
                        </button>
                      </td>
                    </tr>
                    """
                    # --- Append Customer Modal to the string ---
                    modals_html += f"""
                    <div class="modal fade" id="custModal{req_id}" tabindex="-1">
                      <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content">
                          <div class="modal-header bg-success text-white">
                            <h5 class="modal-title">Customer Details</h5>
                            <button class="btn-close" data-bs-dismiss="modal"></button>
                          </div>
                          <div class="modal-body">
                            <p><strong>Name:</strong> {user_name}</p>
                            <p><strong>Email:</strong> {user_email}</p>
                            <p><strong>Phone:</strong> {user_phone}</p>
                          </div>
                          <div class="modal-footer">
                            <button class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                          </div>
                        </div>
                      </div>
                    </div>
                    """

                modals_html += f"""
                <div class="modal fade" id="mechModal{mech_id}_{shop_id}" tabindex="-1">
                  <div class="modal-dialog modal-xl modal-dialog-scrollable">
                    <div class="modal-content">
                      <div class="modal-header bg-info text-white">
                        <h5 class="modal-title">{html.escape(mdata['name'])} - Completed Requests</h5>
                        <button class="btn-close" data-bs-dismiss="modal"></button>
                      </div>
                      <div class="modal-body">
                        <table class="table table-bordered">
                          <thead>
                            <tr>
                              <th>S.No</th>
                              <th>Request Date</th>
                              <th>Completed Date</th>
                              <th>Problem Type</th>
                              <th>Location</th>
                              <th>Service Charge</th>
                              <th>Customer Details</th>
                            </tr>
                          </thead>
                          <tbody>{table_rows}</tbody>
                        </table>
                      </div>
                      <div class="modal-footer">
                        <button class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                      </div>
                    </div>
                  </div>
                </div>
                """

        else:
            inner_modals_html = """
              <div class="col-12 text-center text-muted">
                No completed requests found for this shop.
              </div>
            """

        modals_html += f"""
        <div class="modal fade" id="completedModal{shop_id}" tabindex="-1">
          <div class="modal-dialog modal-lg modal-dialog-scrollable">
            <div class="modal-content">
              <div class="modal-header bg-warning text-dark">
                <h5 class="modal-title">Completed Requests by Mechanics - {html.escape(shop_name_safe)}</h5>
                <button class="btn-close" data-bs-dismiss="modal"></button>
              </div>
              <div class="modal-body">
                <div class="row">{inner_modals_html}</div>
              </div>
              <div class="modal-footer">
                <button class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>
        """
        s_no += 1
else:
    print("""
    <tr>
      <td colspan="6" class="text-center text-muted py-4">🚫 No service requests found.</td>
    </tr>
    """)

print("""
      </tbody>
    </table>
  </div>
</div>
</main>
""")

# Print all collected modal HTML here, outside the main content
print(modals_html)

print("""
</div>
</div>
<script>
  function toggleSidebar() {
    const sidebar = document.getElementById('sidebarMenu');
    sidebar.classList.toggle('show');
    document.getElementById('mainContent').classList.toggle('min-height-100');
  }
</script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")

con.close()