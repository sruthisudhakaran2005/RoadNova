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

cur.execute("""
    SELECT 
        r.request_id, r.status, r.price, r.extra_charge, r.cancellation_fee,
        s.id, s.shop_name, s.owner_email, s.phone, s.address, s.owner_name
    FROM service_requests r
    JOIN mechanicshops s ON r.shop_id = s.id
    WHERE s.status = 'Approved'
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
    (req_id, status, price, extra_charge, cancellation_fee,
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
    elif status.lower() == 'cancelled':
        # Add only cancellation fee to revenue
        shops_data[shop_id]['total_revenue'] += (cancellation_fee or 0)

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
          <th>All Requests</th>
          <th>Total Revenue</th>
          <th>Rating</th>
        </tr>
      </thead>
      <tbody>
""")

modals_html = ""

if shops_data:
    s_no = 1
    for shop_id, data in shops_data.items():
        details = data['details']
        completed_count = data['completed_count']
        total_revenue = data['total_revenue']

        # --- FIX: Moved these queries inside the loop for correct data fetching ---
        cur.execute("SELECT shop_image, owner_image FROM mechanicshops WHERE id=%s", (shop_id,))
        shop_images = cur.fetchone()
        shop_image = shop_images[0]
        owner_image = shop_images[1]

        cur.execute("SELECT rating FROM reviews WHERE shop_id=%s", (shop_id,))
        ratings = cur.fetchall()
        if ratings:
            avg_rating = sum(r[0] for r in ratings) / len(ratings)
            rounded_rating = round(avg_rating)
            stars_html = "&#9733;" * rounded_rating + "&#9734;" * (5 - rounded_rating)
        else:
            stars_html = "&#9734;" * 5

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
          <td> 
              <a href="service_details.py?shop_id={shop_id}" >View Details</a>
          </td>
          <td>₹{total_revenue:.2f}</td>
          <td>{stars_html}</td>
        </tr>
        """)

        # --- Append Shop Details Modal ---
        modals_html += f"""
        <div class="modal fade" id="shopModal{shop_id}" tabindex="-1" aria-labelledby="shopModalLabel{shop_id}" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered modal-lg">
            <div class="modal-content">
              <div class="modal-header bg-danger text-white">
                <h5 class="modal-title" id="shopModalLabel{shop_id}">Shop Details: {shop_name_safe}</h5>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
              <div class="container-fluid">
  <div class="row">
    <!-- Shop Section (Left Column on Desktop) -->
    <div class="col-12 col-md-6 text-center mb-4">
      <img src="./images/{shop_image}" alt="Shop Image" class="img-fluid rounded mb-3" style="max-height: 200px;">
      <h5>Shop Details</h5>
      <p><b>Shop Name:</b> {shop_name_safe}</p>
      <p><b>Address:</b> {saddr_safe}</p>
    </div>

    <!-- Owner Section (Right Column on Desktop) -->
    <div class="col-12 col-md-6 text-center mb-4">
      <img src="./images/{owner_image}" alt="Owner Image" class="img-fluid rounded mb-3" style="max-height: 200px;">
      <h5>Owner Details</h5>
      <p><b>Owner Name:</b> {owner_name_safe}</p>
      <p><b>Email:</b> {semail_safe}</p>
      <p><b>Phone:</b> {sphone_safe}</p>
      <p><b>Address:</b> {saddr_safe}</p>
    </div>
  </div>
</div>


              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>
        """

        # Now prepare mechanic cards for Completed Requests modal
        cur.execute("""
            SELECT mech_id, name
            FROM mechanics
            WHERE shop_id = %s
        """, (shop_id,))
        all_mechanics = cur.fetchall()

        cur.execute("""
            SELECT sr.request_id, sr.request_date, sr.completed_date, sr.problem_type, sr.location,
                   sr.mech_id, sr.total_charge, sr.user_id
            FROM service_requests sr
            WHERE sr.shop_id = %s AND sr.status = 'completed'
        """, (shop_id,))
        completed_reqs = cur.fetchall()

        mechanic_tasks = {mech_id: {'name': name,  'requests': []} for (mech_id, name) in
                          all_mechanics}

        for (req_id, req_date, comp_date, problem, location, mech_id, total_charge, user_id) in completed_reqs:
            if mech_id in mechanic_tasks:
                mechanic_tasks[mech_id]['requests'].append(
                    (req_id, req_date, comp_date, problem, location, total_charge, user_id))

        inner_modals_html = ""
        mech_modals_html = ""

        for mech_id, mdata in mechanic_tasks.items():
            mech_name_safe = html.escape(mdata['name'])
            completed_count_mech = len(mdata['requests'])

            if completed_count_mech > 0:
                inner_modals_html += f"""
                <div class="col-md-4 mb-3">
                  <div class="card text-center" style="cursor:pointer;"
                       data-bs-toggle="modal" data-bs-target="#mechModal{mech_id}_{shop_id}">
                    <div class="card-body">
                      <h5 class="card-title">{mech_name_safe}</h5>
                      <p class="card-text">🛠️ {completed_count_mech} Completed</p>
                    </div>
                  </div>
                </div>
                """
            else:
                inner_modals_html += f"""
                <div class="col-md-4 mb-3">
                  <div class="card text-center" style="cursor:pointer;" onclick="alert('0 requests completed')">
                    <div class="card-body">
                      <h5 class="card-title">{mech_name_safe}</h5>
                      <p class="card-text text-muted">🛠️ 0 Completed</p>
                    </div>
                  </div>
                </div>
                """

            if completed_count_mech > 0:
                table_rows = ""
                for i, (req_id, req_date, comp_date, problem, location, total_charge, user_id) in enumerate(
                        mdata['requests'], 1):
                    cur.execute("SELECT name, email, phone FROM users WHERE user_id = %s", (user_id,))
                    user_row = cur.fetchone()
                    uname = html.escape(user_row[0]) if user_row else "N/A"
                    uemail = html.escape(user_row[1]) if user_row else "N/A"
                    uphone = html.escape(user_row[2]) if user_row else "N/A"

                    req_date_str = req_date.strftime('%Y-%m-%d') if isinstance(req_date, datetime) else str(req_date)
                    comp_date_str = comp_date.strftime('%Y-%m-%d') if isinstance(comp_date, datetime) else str(
                        comp_date)

                    table_rows += f"""
                    <tr>
                      <th scope="row">{i}</th>
                      <td>{req_date_str}</td>
                      <td>{comp_date_str}</td>
                      <td>{problem}</td>
                      <td>{location}</td>
                      <td>{total_charge}</td>
                      <td>{uname}</td>
                      <td>{uemail}</td>
                      <td>{uphone}</td>
                    </tr>
                    """

                mech_modals_html += f"""
                <div class="modal fade" id="mechModal{mech_id}_{shop_id}" tabindex="-1" aria-labelledby="mechModalLabel{mech_id}_{shop_id}" aria-hidden="true">
                  <div class="modal-dialog modal-xl modal-dialog-scrollable modal-dialog-centered">
                    <div class="modal-content">
                      <div class="modal-header bg-danger text-white">
                        <h5 class="modal-title" id="mechModalLabel{mech_id}_{shop_id}">Completed Requests for {mech_name_safe}</h5>
                        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
                      </div>
                      <div class="modal-body">
                        <div class="table-responsive">
                          <table class="table table-striped table-bordered align-middle">
                            <thead class="table-danger text-center">
                              <tr>
                                <th>S.NO</th>
                                <th>Request Date</th>
                                <th>Completed Date</th>
                                <th>Problem</th>
                                <th>Location</th>
                                <th>Service Charge</th>
                                <th>Customer Name</th>
                                <th>Customer Email</th>
                                <th>Customer Phone</th>
                              </tr>
                            </thead>
                            <tbody>
                              {table_rows}
                            </tbody>
                          </table>
                        </div>
                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
                      </div>
                    </div>
                  </div>
                </div>
                """

        modals_html += f"""
        <div class="modal fade" id="completedModal{shop_id}" tabindex="-1" aria-labelledby="completedModalLabel{shop_id}" aria-hidden="true">
          <div class="modal-dialog modal-xl modal-dialog-scrollable modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header bg-danger text-white">
                <h5 class="modal-title" id="completedModalLabel{shop_id}">Completed Requests Mechanics - {shop_name_safe}</h5>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <div class="row">
                  {inner_modals_html}
                </div>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>
        """

        modals_html += mech_modals_html

        s_no += 1
else:
    print('<tr><td colspan="6" class="text-center">No Shops Found.</td></tr>')

print("""
      </tbody>
    </table>
  </div>
</div>
""")

print(modals_html)

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
</script>
</body>
</html>
""")

# Close DB connection
cur.close()
con.close()