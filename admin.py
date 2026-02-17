#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
form = cgi.FieldStorage()


print("""
      <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Admin Dashboard</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" />
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet" />

  <style>
    body {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    .sidebar {
      min-height: 100vh;
      max-height:auto;
    }

    .sidebar .nav-link {
      color: #710019;
    }

    .sidebar .nav-link.active,
    .sidebar .nav-link:hover {
      background-color:#f7bec0;
      color:black;
    }

    .card {
      margin-bottom: 20px;
    }

    .content-section {
      display: none;
    }

    .active-section {
      display: block;
    }

    @media (max-width: 768px) {
      .sidebar {
        position: fixed;
        top: 56px;
        left: -200px;
        width: 200px!important;
        z-index: 1031;
        transition: left 0.3s ease-in-out;
      }

      .sidebar.show {
        left: 0;
      }
      .content-section {
  display: none;
}


      .overlay {
        display: none;
        position: fixed;
        top: 56px;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: 1030;
      }

      .overlay.show {
        display: block;
      }
    }

   table {
  width: 100%!important;
  overflow-x: auto;
}


    .sidebar.show + #mainContent {
      margin-left: 0;
    }
   
   
    .label{
    margin-left:0px;}

@media (min-width: 768px) {
  #mainContent {
    margin-left: 250px; 
    margin-top:-740px;
    padding: 80px 20px 20px 20px;
  }
}

@media (max-width: 768px) {
  #mainContent {
    margin-left: 0;
  }
}

@media (max-width: 768px) {
  form label {
    margin-left: 0 !important;
    font-size: medium !important;
    display: block;
    margin-bottom: 10px;
  }
  form select {
    width:200px!important;
    max-width: none !important;
  }
}
.navbar-brand{
color:#c85250!important;
}

 }
    .header {
      text-align: center;
      margin-bottom: 40px;
    }
    .header h1 {
      font-size: 2.8rem;
      font-weight: 900;
      margin-bottom: 8px;
      color: #222;
      letter-spacing: 1px;
    }
    .header p {
      font-size: 1.2rem;
      font-weight: 600;
      color: #555;
      margin-top: 0;
    }
    .card {
      border-radius: 15px;
      padding: 30px 25px;
      margin-bottom: 30px;
      box-shadow: 0 8px 20px rgba(0,0,0,0.1);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      cursor: default;
      background: white;
    }
    .card:hover {
      box-shadow: 0 12px 30px rgba(0,0,0,0.15);
      transform: translateY(-6px);
    }
   
    .stats {
  display: flex;
  flex-wrap: nowrap;
  justify-content: center;
  gap: 22px;
  overflow-x: auto;
  padding-bottom: 10px;
}

.stat-box {
  min-width: 200px;
  flex: 0 0 auto;
  padding: 25px 20px;
  border-radius: 15px;
  text-align: center;
  font-weight: 700;
  font-size: 1.6rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 6px 16px rgba(0,0,0,0.1);
  color: #444;
  background: white;
}

    .stat-box:hover {
      box-shadow: 0 10px 28px rgba(0,0,0,0.2);
      transform: translateY(-4px);
    }
    .stat-box p {
      margin: 6px 0 0;
      font-size: 1rem;
      font-weight: 600;
      letter-spacing: 0.03em;
      color: #666;
    }

    /* Pastel background colors */
    .stat-users {
      background-color: #ffdede; /* pastel pink */
      color: #a33a3a;
      box-shadow: 0 6px 16px rgba(163, 58, 58, 0.3);
    }
    .stat-approved {
      background-color: #d0f0fd; /* pastel light blue */
      color: #1a567a;
      box-shadow: 0 6px 16px rgba(26, 86, 122, 0.3);
    }
    .stat-rejected {
      background-color: #fddde6; /* pastel light rose */
      color: #9b3c59;
      box-shadow: 0 6px 16px rgba(155, 60, 89, 0.3);
    }
    .stat-pending {
      background-color: #e6f7e6; /* pastel light green */
      color: #3c763d;
      box-shadow: 0 6px 16px rgba(60, 118, 61, 0.3);
    }

    /* Flex container for both charts */
    .charts-row {
      display: flex;
      justify-content: center;
      gap: 40px;
      flex-wrap: wrap;
      margin-top: 40px;
    }
    .chart-container {
      flex: 1 1 400px;
      max-width: 420px;
      background: white;
      padding: 25px 20px;
      border-radius: 15px;
      box-shadow: 0 6px 25px rgba(0,0,0,0.1);
    }
    .chart-container h3 {
      color: #222;
      font-weight: 700;
      margin-bottom: 22px;
      text-align: center;
    }
    .doughnut-wrapper {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    #doughnutChart {
      max-width: 280px !important;
    }

    @media (max-width: 900px) {
      .charts-row {
        flex-direction: column;
        align-items: center;
      }
      .chart-container {
        max-width: 90%;
      }
    }
    .mainContent{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #fff;
      margin: 0;
      padding: 20px;
      color: #333;
      }
#barChart,
#doughnutChart {
  height: 240px !important;
  max-height: 240px;
}

  </style>
</head>
<body>
""")
cur.execute("SELECT image FROM admin WHERE id=1")
result = cur.fetchone()
if result:
    profile = result[0]
else:
    profile = "default.jpg"



print("""
  <nav class="navbar navbar-dark bg-white fixed-top"style="box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
    <div class="container-fluid">

      <button class="btn btn-outline-dark d-md-none me-2" type="button" onclick="toggleSidebar()" style="color:5F9EA0">
        <i class="bi bi-list"></i>
      </button>
      <span class="navbar-brand mb-0 h1">RoadNova</span>
     <div class="d-flex align-items-center ms-auto">
      <img src="images/%s" alt="Admin Profile" class="rounded-circle" style="width:40px; height:40px; object-fit:cover;"/>
    </div>

    </div>
  </nav>
"""%( profile))
print("""
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
               <li><a href="new_requests.py" class="nav-link "  ><i class="bi bi-person me-2"></i>New Requests</a></li>
                <li><a href="approved.py" class="nav-link "  ><i class="bi bi-person me-2"></i>Approved shops</a></li>
                 <li><a href="rejected.py" class="nav-link " ><i class="bi bi-person me-2"></i>Rejected shops</a></li>
                 <li><a href="blocked.py" class="nav-link " ><i class="bi bi-person me-2"></i>Blocked shops</a></li>
            </ul>
          </div>
        </li>
        <li class="nav-item">
          <a class="nav-link d-flex justify-content-between align-items-center" href="all_requests.py">
           <span> <i class="bi-envelope"></i>Service Requests</span>
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
   <div class="overlay" id="sidebarOverlay"></div>
   <div class="container-fluid">
  <div class="row">
  <main id="mainContent" class="col-md-9 col-lg-10 main maincontent">

""")

cur.execute("SELECT COUNT(*) FROM users")
user_count = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM mechanicshops WHERE status='Approved'")
approved_count = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM mechanicshops WHERE status='Rejected'")
rejected_count = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM mechanicshops WHERE status='Pending'")
pending_count = cur.fetchone()[0]

# Service Status Stats
cur.execute("SELECT COUNT(*) FROM service_requests WHERE status='Pending'")
service_pending = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM service_requests WHERE status='Completed'")
service_completed = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM service_requests WHERE status='Cancelled'")
service_cancelled = cur.fetchone()[0]
cur.execute("SELECT COUNT(*) FROM service_requests WHERE status='Rejected'")
service_rejected = cur.fetchone()[0]
cur.execute("""
    SELECT DATE(request_date) AS day,
           SUM(CASE 
                   WHEN status = 'Completed' THEN total_charge
                   WHEN status = 'Cancelled' THEN cancellation_fee 
                   ELSE 0 
               END) AS total_revenue
    FROM service_requests
    WHERE status IN ('Completed', 'Cancelled')
    GROUP BY day
    ORDER BY day DESC
    LIMIT 7
""")

revenue_data = cur.fetchall()

# Format for JS
dates = [str(row[0]) for row in revenue_data][::-1]  # reverse for chronological order
revenues = [float(row[1]) for row in revenue_data][::-1]
con.close()

print(f"""
  
<div class="header">
    <h1>🔧 Admin Dashboard</h1>
    <p>Welcome back, Admin! Here’s a quick  overview of the system.</p>
  </div>

  
<div class="card">
  <div class="stats">
    <div class="stat-box stat-users">
      <h2>{user_count}</h2>
      <p>Total Users</p>
    </div>
    <div class="stat-box stat-approved">
      <h2>{approved_count}</h2>
      <p>Approved Shops</p>
    </div>
    <div class="stat-box stat-rejected">
      <h2>{rejected_count}</h2>
      <p>Rejected Shops</p>
    </div>
    <div class="stat-box stat-pending">
      <h2>{pending_count}</h2>
      <p>Pending Shops</p>
    </div>
  </div>
</div>



  <div class="charts-row">
       <div class="card chart-container">
      <h3>💰 Revenue (Last 7 Days)</h3>
      <canvas id="barChart"></canvas>
    </div>


    <div class="card chart-container">
      <h3>🛠️ Service Request Status</h3>
      <div class="doughnut-wrapper">
        <canvas id="doughnutChart"></canvas>
      </div>
    </div>
  </div>
""")


print("""
    </main>
  </div>
</div>
""")

print(f"""
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

 <script >
  function showSection(id) {{
    const sections = document.querySelectorAll('.content-section');
    sections.forEach(section => section.classList.remove('active-section'));
    const target = document.getElementById(id);
    if (target) {{
      target.classList.add('active-section');
    }}

    const sidebar = document.getElementById('sidebarMenu');
    const overlay = document.getElementById('sidebarOverlay');
    if (window.innerWidth <= 768) {{
      sidebar.classList.remove('show');
      overlay.classList.remove('show');
    }}
    
    document.querySelectorAll('.nav-link').forEach(link => link.classList.remove('active'));
    const activeLink = Array.from(document.querySelectorAll('.nav-link')).find(link => link.getAttribute('onclick')?.includes(id));
    if (activeLink) {{
      activeLink.classList.add('active');
    }}
  }}

  function toggleSidebar() {{
    const sidebar = document.getElementById('sidebarMenu');
    const overlay = document.getElementById('sidebarOverlay');
    sidebar.classList.toggle('show');
    overlay.classList.toggle('show');
  }}

  function hideSidebar() {{
    const sidebar = document.getElementById('sidebarMenu');
    const overlay = document.getElementById('sidebarOverlay');
    sidebar.classList.remove('show');
    overlay.classList.remove('show');
  }}
  const ctx = document.getElementById('barChart').getContext('2d');
new Chart(ctx, {{
  type: 'bar',
  data: {{
    labels: {dates},
    datasets: [{{
      label: 'Revenue (₹)',
      data: {revenues},
      backgroundColor: 'rgba(34, 150, 243, 0.7)',
      borderColor: 'rgba(34, 150, 243, 1)',
      borderWidth: 1,
      borderRadius: 5,
      hoverBackgroundColor: 'rgba(34, 150, 243, 0.9)'
    }}]
  }},
  options: {{
    scales: {{
      y: {{
        beginAtZero: true,
        title: {{
          display: true,
          text: 'Revenue in ₹'
        }},
        grid: {{
          color: 'rgba(0,0,0,0.1)'
        }}
      }},
      x: {{
        title: {{
          display: true,
          text: 'Date'
        }}
      }}
    }},
    plugins: {{
      legend: {{
        display: true,
        position: 'top'
      }},
      tooltip: {{
        backgroundColor: '#222',
        titleColor: '#fff',
        bodyColor: '#fff',
        cornerRadius: 4
      }}
    }}
  }}
}});

  
    const doughnutCtx = document.getElementById('doughnutChart').getContext('2d');
    new Chart(doughnutCtx, {{
        type: 'doughnut',
        data: {{
            labels: ['Pending', 'Completed', 'Cancelled', 'Rejected'],
            datasets: [{{
                label: 'Total',
                data: [{service_pending}, {service_completed}, {service_cancelled}, {service_rejected}],
                backgroundColor: [
                    'rgba(255, 205, 86, 0.8)',
                    'rgba(75, 192, 192, 0.8)',
                    'rgba(255, 99, 132, 0.8)',
                     'rgba(255, 50, 132, 0.8)'
                ],
                borderColor: [
                    'rgba(255, 205, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(255, 99, 132, 1)',
                     'rgba(255, 50, 132, 1)'
                ],
                borderWidth: 2
            }}]
        }},
        options: {{
            responsive: true,
            animation: {{
                animateRotate: true,
                animateScale: true,
                duration: 1500,
                easing: 'easeOutBounce'
            }},
            plugins: {{
                legend: {{
                    position: 'bottom',
                    labels: {{
                      color: '#333',
                      font: {{
                        weight: 'bold'
                      }}
                    }}
                }},
                tooltip: {{
                  backgroundColor: '#222',
                  titleColor: '#fff',
                  bodyColor: '#fff',
                  cornerRadius: 6
                }}
            }}
        }}
    }});
  
</script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>

""")
