#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys
import datetime
import pymysql, cgi, cgitb, html
import json

sys.stdout.reconfigure(encoding='utf-8')
print("content-type:text/html\r\n\r\n")

cgitb.enable()

# DB Connection
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

# Get ID and filter parameters
form = cgi.FieldStorage()
id = form.getvalue("id")
start_date_str = form.getvalue("start_date")
end_date_str = form.getvalue("end_date")
period = form.getvalue("period")
mechanic_id_str = form.getvalue("mechanic")

# Validate ID
if not id:
    print("<h3 style='color:red;'>Error: No ID provided</h3>")
    sys.exit()

# Fetch Mechanic Shop Info
query = "SELECT * FROM mechanicshops WHERE id=%s"
cur.execute(query, (id,))
shop = cur.fetchone()

# Check if shop exists
if not shop:
    print("<h3 style='color:red;'>Error: Invalid Shop ID</h3>")
    sys.exit()

# Escape values
shop_name = html.escape(str(shop[10]))
owner_name = html.escape(str(shop[1]))
shop_img = html.escape(str(shop[12]))
email = html.escape(str(shop[17]))
phone = html.escape(str(shop[4]))
address = html.escape(str(shop[11]))
city = html.escape(str(shop[8]))
profile_img = html.escape(str(shop[9]))

def get_filtered_data(shop_id, start_date, end_date):
    base_params = [shop_id]
    date_clause = ""

    if start_date and end_date:
        date_clause = "AND request_date BETWEEN %s AND %s"
        base_params.extend([start_date, end_date])

    cur.execute(f"SELECT COUNT(*) FROM service_requests WHERE shop_id=%s {date_clause}", tuple(base_params))
    service_count = cur.fetchone()[0]

    cur.execute(f"SELECT COUNT(*) FROM service_requests WHERE shop_id=%s AND status='Completed' {date_clause}",
                tuple(base_params))
    completed_requests = cur.fetchone()[0]

    cur.execute(f"SELECT COUNT(*) FROM service_requests WHERE shop_id=%s AND status='Approved' {date_clause}",
                tuple(base_params))
    inprogress_requests = cur.fetchone()[0]

    cur.execute(f"SELECT COUNT(*) FROM service_requests WHERE shop_id=%s AND status='Rejected' {date_clause}",
                tuple(base_params))
    rejected_count = cur.fetchone()[0]

    cur.execute(f"SELECT COUNT(*) FROM service_requests WHERE shop_id=%s AND status='Cancelled' {date_clause}",
                tuple(base_params))
    cancelled_count = cur.fetchone()[0]

    cur.execute(f"SELECT COUNT(*) FROM service_requests WHERE shop_id=%s AND status='Pending' {date_clause}",
                tuple(base_params))
    pending_count = cur.fetchone()[0]

    cur.execute(
        f"SELECT IFNULL(SUM(total_charge), 0) FROM service_requests WHERE shop_id = %s AND payment_status = 'Paid' AND status='Completed' {date_clause}",
        tuple(base_params))
    total_revenue = float(cur.fetchone()[0])

    cur.execute("SELECT mech_id, name FROM mechanics WHERE shop_id=%s", (shop_id,))
    mechanics_list = cur.fetchall()

    mechanic_count = len(mechanics_list)

    mechanic_stats = {}
    for m_id, m_name in mechanics_list:
        mech_params = [m_id]
        mech_date_clause = ""
        if start_date and end_date:
            mech_date_clause = "AND request_date BETWEEN %s AND %s"
            mech_params.extend([start_date, end_date])

        cur.execute(f"SELECT COUNT(*) FROM service_requests WHERE mech_id=%s {mech_date_clause}", tuple(mech_params))
        total = cur.fetchone()[0]

        cur.execute(f"SELECT COUNT(*) FROM service_requests WHERE mech_id=%s AND status='Completed' {mech_date_clause}",
                    tuple(mech_params))
        completed = cur.fetchone()[0]

        cur.execute(f"SELECT COUNT(*) FROM service_requests WHERE mech_id=%s AND status='Rejected' {mech_date_clause}",
                    tuple(mech_params))
        rejected = cur.fetchone()[0]

        cur.execute(f"SELECT COUNT(*) FROM service_requests WHERE mech_id=%s AND status='Approved' {mech_date_clause}",
                    tuple(mech_params))
        approved = cur.fetchone()[0]

        cur.execute(f"SELECT COUNT(*) FROM service_requests WHERE mech_id=%s AND status='Cancelled' {mech_date_clause}",
                    tuple(mech_params))
        cancelled = cur.fetchone()[0]

        cur.execute(f"""
            SELECT IFNULL(SUM(completed_total), 0) + IFNULL(SUM(cancelled_fee), 0) AS total_revenue
            FROM (
                SELECT 
                    CASE 
                        WHEN status = 'Completed' AND payment_status = 'Paid' THEN total_charge 
                        ELSE 0 
                    END AS completed_total,
                    CASE 
                        WHEN status = 'Cancelled' AND cancellation_fee IS NOT NULL THEN cancellation_fee 
                        ELSE 0 
                    END AS cancelled_fee
                FROM service_requests
                WHERE shop_id = %s {date_clause}
            ) AS combined_revenue
        """, tuple(base_params))
        total_revenue = float(cur.fetchone()[0])

        mechanic_stats[str(m_id)] = {
            "name": m_name,
            "total": total,
            "completed": completed,
            "rejected": rejected,
            "approved": approved,
            "cancelled": cancelled,
            "revenue": total_revenue
        }

    mechanic_stats["all"] = {
        "name": "Overall Performance",
        "total": service_count,
        "completed": completed_requests,
        "rejected": rejected_count,
        "cancelled": cancelled_count,
        "revenue": total_revenue
    }

    return {
        "service_count": service_count,
        "completed_requests": completed_requests,
        "inprogress_requests": inprogress_requests,
        "rejected_count": rejected_count,
        "cancelled_count": cancelled_count,
        "pending_count": pending_count,
        "total_revenue": total_revenue,
        "mechanic_count": mechanic_count,
        "mechanic_stats": mechanic_stats
    }

# --- Determine date range based on filter input ---
today = datetime.date.today()
start_date = None
end_date = None

if period == "today":
    start_date = datetime.datetime.combine(today, datetime.time.min).strftime('%Y-%m-%d %H:%M:%S')
    end_date = datetime.datetime.combine(today, datetime.time.max).strftime('%Y-%m-%d %H:%M:%S')
elif period == "week":
    start_date = (today - datetime.timedelta(days=today.weekday())).strftime('%Y-%m-%d')
    end_date = today.strftime('%Y-%m-%d')
elif period == "month":
    start_date = today.replace(day=1).strftime('%Y-%m-%d')
    end_date = today.strftime('%Y-%m-%d')
elif start_date_str and end_date_str:
    start_date = start_date_str
    end_date = end_date_str

metrics = get_filtered_data(id, start_date, end_date)
mechanic_stats = metrics["mechanic_stats"]

initial_mechanic_id = mechanic_id_str if mechanic_id_str in mechanic_stats else "all"

mechanic_stats_json = json.dumps(mechanic_stats)

print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Mechanic Dashboard</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" />
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet" />
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <link href="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/css/select2.min.css" rel="stylesheet" />

  <style>
    body {{ min-height: 100vh; overflow-x: hidden; }}
    .sidebar {{ color: #050a30; min-height: 100vh; }}
    .sidebar .nav-link {{ color: #050a30; }}
    .sidebar .nav-link:hover, .sidebar .nav-link.active {{
      background-color: #2e8bc0; color: white;
    }}
    .content-section {{ display: none; }}
    .content-section.active {{ display: block; }}
    .welcome-box {{
      background: linear-gradient(to right, #2e8bc0, #0c2d48);
      color: white; padding: 30px; border-radius: 12px; margin-bottom: 30px;
    }}
    .info-card {{
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
      border: none; border-left: 5px solid #2e8bc0;
      width:300px;
    }}
    .info-title {{ font-size: 18px; color: #2e8bc0; }}
    .info-value {{ font-size: 28px; font-weight: bold; color: #050a30; }}
    .shop-img {{ width: 100%; height: 200px; object-fit: cover; border-radius: 8px; }}
    @media (max-width: 768px) {{
      #sidebarMenu {{
        position: fixed;
        top: 56px;
        left: -250px;
        width: 250px;
        height: 100%;
        background-color: #b1d4e0;
        z-index: 1050;
        transition: left 0.3s ease-in-out;
      }}
      #sidebarMenu.show-sidebar {{ left: 0; }}
      body.sidebar-open {{ overflow: hidden; }}
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
.custom-filter-btn {{
  background: linear-gradient(to right, #2e8bc0, #0c2d48);
  color: white;
  border: none;
  transition: all 0.3s ease;
  font-weight: bold;
}}
.custom-filter-btn:hover {{
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}}
.filter-container {{
    max-width: 700px; 
    margin: 0 auto; 
    margin-left:0px;
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
        <a href="owner.py?id={id}" class="text-white text-decoration-none">
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
        <nav class="col-md-3 col-lg-2 sidebar d-md-block p-0" id="sidebarMenu" style="background-color:#b1d4e0">
          <h5 class="text-center py-3">{shop_name}</h5>
          <ul class="nav flex-column">
            <li class="nav-item">
              <a class="nav-link active" href="mech.py?id={id}">
                <i class="bi bi-speedometer2 me-2"></i>Dashboard
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" data-bs-toggle="collapse" href="#serviceSubmenu" role="button" aria-expanded="false" aria-controls="serviceSubmenu">
                <i class="bi bi-wrench-adjustable"></i> Services
              </a>
              <div class="collapse" id="serviceSubmenu">
                <ul class="nav flex-column ms-3">
                  <li class="nav-item"><a class="nav-link" href="add_service.py?id={id}"><i class="bi bi-bag-plus-fill"></i> Add services</a></li>
                  <li class="nav-item"><a class="nav-link" href="view_services.py?id={id}"><i class="bi bi-eye"></i> View services</a></li>
                </ul>
              </div>
            </li>
            <li class="nav-item">
              <a class="nav-link" data-bs-toggle="collapse" href="#employeeSubmenu" role="button" aria-expanded="false" aria-controls="employeeSubmenu">
                <i class="bi bi-tools me-2"></i>Employees
              </a>
              <div class="collapse" id="employeeSubmenu">
                <ul class="nav flex-column ms-3">
                  <li class="nav-item"><a class="nav-link" href="add.py?id={id}"><i class="bi bi-person-plus me-2"></i>Add Mechanic</a></li>
                  <li class="nav-item"><a class="nav-link" href="view.py?id={id}"><i class="bi bi-people me-2"></i>View Mechanics</a></li>
                </ul>
              </div>
            </li>
            <li class="nav-item">
              <a class="nav-link" data-bs-toggle="collapse" href="#requestSubmenu" role="button" aria-expanded="false" aria-controls="requestSubmenu">
                <span><i class="bi bi-envelope me-2"></i>Requests</span>
              </a>
              <div class="collapse" id="requestSubmenu">
                <ul class="nav flex-column ms-3">
                  <li><a href="pending.py?id={id}" class="nav-link"><i class="bi bi-card-list"></i> Pending</a></li>
                  <li><a href="current.py?id={id}" class="nav-link"><i class="bi bi-journal-check"></i> Process</a></li>
                  <li><a href="completed.py?id={id}" class="nav-link"><i class="bi bi-card-checklist"></i> Completed</a></li>
                  <li><a href="rejected_service.py?id={id}" class="nav-link"><i class="bi bi-x-square"></i> Rejected</a></li>
                  <li><a href="cancelled_service.py?id={id}" class="nav-link"><i class="bi bi-x-octagon"></i></i>cancelled</a></li>
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
    <div class="welcome-box">
      <h2>Welcome back, {owner_name}!</h2>
      <p>🚗 This is your dashboard overview. Stay on top of services, employees, requests, and earnings. Let’s keep the engines running! 🔧</p>
    </div>

   <div class="card p-3 mb-4 filter-container">
    <h5 class="mb-3">Filter Dashboard Data</h5>
    <form method="get" action="mech.py" class="d-flex flex-wrap align-items-end" id="filterForm">
        <input type="hidden" name="id" value="{id}">
        <input type="hidden" name="mechanic" id="mechanicHidden" value="{initial_mechanic_id}">
        <div class="flex-fill me-2 mb-2">
            <label for="start_date" class="form-label">From Date</label>
            <input type="date" class="form-control" name="start_date" id="start_date" value="{start_date if start_date else ''}">
        </div>
        <div class="flex-fill me-2 mb-2">
            <label for="end_date" class="form-label">To Date</label>
            <input type="date" class="form-control" name="end_date" id="end_date" value="{end_date if end_date else ''}">
        </div>
        <div class="flex-fill me-2 mb-2">
            <label for="period" class="form-label">Quick Filter</label>
            <select class="form-select" name="period" id="period">
                <option value="">Custom Range</option>
                <option value="today" {"selected" if period == "today" else ""}>Today</option>
                <option value="week" {"selected" if period == "week" else ""}>This Week</option>
                <option value="month" {"selected" if period == "month" else ""}>This Month</option>
            </select>
        </div>
        <div class="flex-fill mb-2">
            <button type="submit" class="btn custom-filter-btn w-100">Apply Filter</button>
        </div>
    </form>
</div>
""")

print(f"""
    <div class="row mb-4">
      <div class="col-md-4">
        <div class="card info-card"><div class="card-body">
          <div class="info-title">Total Services Offered</div>
          <div class="info-value">{metrics["service_count"]}</div>
        </div></div>
      </div>
      <div class="col-md-4">
        <div class="card info-card"><div class="card-body">
          <div class="info-title">Total Mechanics</div>
          <div class="info-value">{metrics["mechanic_count"]}</div>
        </div></div>
      </div>

      <div class="col-md-4">
        <div class="card info-card"><div class="card-body">
          <div class="info-title">Completed Requests</div>
          <div class="info-value">{metrics["completed_requests"]}</div>
        </div></div>
      </div>
      </div>

    <div class="row mb-4">
      <div class="col-md-4">
        <div class="card info-card"><div class="card-body">
          <div class="info-title">Ongoing Requests</div>
          <div class="info-value">{metrics["inprogress_requests"]}</div>
        </div></div>
      </div>

  <div class="col-md-4">
    <div class="card info-card"><div class="card-body">
      <div class="info-title">Rejected Requests</div>
      <div class="info-value">{metrics["rejected_count"]}</div>
    </div></div>
  </div>
  <div class="col-md-4">
    <div class="card info-card"><div class="card-body">
      <div class="info-title">Cancelled Requests</div>
      <div class="info-value">{metrics["cancelled_count"]}</div>
    </div></div>
  </div>
  <br>
  <div class="row mb-4">
  <div class="col-md-4">
    <div class="card info-card"><div class="card-body">
      <div class="info-title">Pending Requests</div>
      <div class="info-value">{metrics["pending_count"]}</div>
    </div></div></div>
  </div>
</div>

    <div class="row mb-4">
      <div class="col-md-12">
        <div class="card info-card"><div class="card-body" style="background-color:#97D5E0">
          <div class="info-title">Total Revenue</div>
          <div class="info-value">₹{metrics["total_revenue"]:.2f}</div>
        </div></div>
      </div>
    </div>


<div class="card p-3 mb-4" style="width:500px;margin-top:-150px;margin-left:500px;">
  <h5 class="mb-3">Employee Performance Summary</h5>

  <div class="mb-3">
    <label for="mechanicSelect" class="form-label">Select Mechanic</label>
    <select id="mechanicSelect" class="form-select">
      <option disabled>Select a mechanic</option>
""")

print(f'<option value="all" {"selected" if initial_mechanic_id == "all" else ""}>Overall Performance</option>')
for m_id, m_data in mechanic_stats.items():
    if m_id == "all":
        continue
    print(
        f'<option value="{m_id}" {"selected" if initial_mechanic_id == m_id else ""}>{html.escape(m_data["name"])}</option>')

print(f"""
    </select>
  </div>

  <canvas id="employeeChart" height="120"></canvas>
</div>
""")

print(f"""
    <div class="card p-3">
      <h4 class="mb-3">Workshop Info</h4>
      <div class="row">
        <div class="col-md-4">
          <img src="images/{shop_img}" class="shop-img" alt="Workshop Image">
        </div>
        <div class="col-md-8">
          <p><strong>Name:</strong> {shop_name}</p>
          <p><strong>Email:</strong> {email}</p>
          <p><strong>Phone:</strong> {phone}</p>
          <p><strong>Address:</strong> {address}</p>
          <p><strong>City:</strong> {city}</p>
        </div>
      </div>
    </div>
  </div>
</main>

<script>
const toggleBtn = document.getElementById('toggleSidebar');
  const sidebar = document.getElementById('sidebarMenu');
  const overlay = document.getElementById('sidebarOverlay');

  toggleBtn.addEventListener('click', () => {{
    sidebar.classList.toggle('show-sidebar');
    overlay.style.display = sidebar.classList.contains('show-sidebar') ? 'block' : 'none';
  }});

  overlay.addEventListener('click', () => {{
    sidebar.classList.remove('show-sidebar');
    overlay.style.display = 'none';
  }});

   const mechanicStats = {mechanic_stats_json};
   const initialMechanicId = "{initial_mechanic_id}";

  const employeeCtx = document.getElementById('employeeChart').getContext('2d');
  const employeeChart = new Chart(employeeCtx, {{
    type: 'bar',
    data: {{
      labels: ['Total Assigned', 'Completed', 'Rejected', 'Cancelled'],
      datasets: [{{
        label: 'Mechanic Performance',
        data: [0, 0, 0, 0],
        backgroundColor: ['#2e8bc0', '#145DA0', '#FF4C4C', '#999999']
      }}]
    }},
    options: {{
     responsive: true,
      scales: {{
        y: {{
          beginAtZero: true
        }}
      }}
    }}
  }});

    function updateChart(mechanicId) {{
        const stats = mechanicStats[mechanicId];
        employeeChart.data.datasets[0].data = [
            stats.total,
            stats.completed,
            stats.rejected,
            stats.cancelled
        ];
        employeeChart.update();
    }}

    updateChart(initialMechanicId);

    document.getElementById('mechanicSelect').addEventListener('change', function () {{
        const mechanicId = this.value;
        updateChart(mechanicId);
        document.getElementById('mechanicHidden').value = mechanicId;
    }});

    const periodSelect = document.getElementById('period');
    const startDateInput = document.getElementById('start_date');
    const endDateInput = document.getElementById('end_date');

    periodSelect.addEventListener('change', function() {{
        const selectedValue = this.value;
        if (selectedValue !== '') {{
            startDateInput.value = '';
            endDateInput.value = '';
        }}
    }});
</script>
<script src="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/select2.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js"></script>

</body>
</html>
""")