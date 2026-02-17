#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
print("Content-type: text/html\n")

import pymysql
import cgi, cgitb
cgitb.enable()

# DB Connection
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

# General Stats
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
cur.execute("""
    SELECT DATE(request_date) AS day, SUM(price) 
    FROM service_requests 
    WHERE status='Completed'
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
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Admin Dashboard</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <style>
    body {{
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #fff;
      margin: 0;
      padding: 20px;
      color: #333;
    }}
    .header {{
      text-align: center;
      margin-bottom: 40px;
    }}
    .header h1 {{
      font-size: 2.8rem;
      font-weight: 900;
      margin-bottom: 8px;
      color: #222;
      letter-spacing: 1px;
    }}
    .header p {{
      font-size: 1.2rem;
      font-weight: 600;
      color: #555;
      margin-top: 0;
    }}
    .card {{
      border-radius: 15px;
      padding: 30px 25px;
      margin-bottom: 30px;
      box-shadow: 0 8px 20px rgba(0,0,0,0.1);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      cursor: default;
      background: white;
    }}
    .card:hover {{
      box-shadow: 0 12px 30px rgba(0,0,0,0.15);
      transform: translateY(-6px);
    }}
    .stats {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 22px;
    }}
    .stat-box {{
      padding: 25px 20px;
      border-radius: 15px;
      text-align: center;
      flex: 1 1 180px;
      font-weight: 700;
      font-size: 1.6rem;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      box-shadow: 0 6px 16px rgba(0,0,0,0.1);
      color: #444;
    }}
    .stat-box:hover {{
      box-shadow: 0 10px 28px rgba(0,0,0,0.2);
      transform: translateY(-4px);
    }}
    .stat-box p {{
      margin: 6px 0 0;
      font-size: 1rem;
      font-weight: 600;
      letter-spacing: 0.03em;
      color: #666;
    }}

    /* Pastel background colors */
    .stat-users {{
      background-color: #ffdede; /* pastel pink */
      color: #a33a3a;
      box-shadow: 0 6px 16px rgba(163, 58, 58, 0.3);
    }}
    .stat-approved {{
      background-color: #d0f0fd; /* pastel light blue */
      color: #1a567a;
      box-shadow: 0 6px 16px rgba(26, 86, 122, 0.3);
    }}
    .stat-rejected {{
      background-color: #fddde6; /* pastel light rose */
      color: #9b3c59;
      box-shadow: 0 6px 16px rgba(155, 60, 89, 0.3);
    }}
    .stat-pending {{
      background-color: #e6f7e6; /* pastel light green */
      color: #3c763d;
      box-shadow: 0 6px 16px rgba(60, 118, 61, 0.3);
    }}

    /* Flex container for both charts */
    .charts-row {{
      display: flex;
      justify-content: center;
      gap: 40px;
      flex-wrap: wrap;
      margin-top: 40px;
    }}
    .chart-container {{
      flex: 1 1 400px;
      max-width: 420px;
      background: white;
      padding: 25px 20px;
      border-radius: 15px;
      box-shadow: 0 6px 25px rgba(0,0,0,0.1);
    }}
    .chart-container h3 {{
      color: #222;
      font-weight: 700;
      margin-bottom: 22px;
      text-align: center;
    }}
    .doughnut-wrapper {{
      display: flex;
      justify-content: center;
      align-items: center;
    }}
    #doughnutChart {{
      max-width: 280px !important;
    }}

    @media (max-width: 900px) {{
      .charts-row {{
        flex-direction: column;
        align-items: center;
      }}
      .chart-container {{
        max-width: 90%;
      }}
    }}

  </style>
</head>
<body>

  <div class="header">
    <h1>🔧 Admin Dashboard</h1>
    <p>Welcome back, Admin! Here’s a quick  overview of the system.</p>
  </div>

  <div class="card stats">
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

  <script>
  
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
            labels: ['Pending', 'Completed', 'Cancelled'],
            datasets: [{{
                label: 'Service Status',
                data: [{service_pending}, {service_completed}, {service_cancelled}],
                backgroundColor: [
                    'rgba(255, 205, 86, 0.8)',
                    'rgba(75, 192, 192, 0.8)',
                    'rgba(255, 99, 132, 0.8)'
                ],
                borderColor: [
                    'rgba(255, 205, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(255, 99, 132, 1)'
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

</body>
</html>
""")
