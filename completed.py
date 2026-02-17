#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type: text/html\r\n\r\n")
import datetime
import pymysql, cgi, cgitb
cgitb.enable()
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
today = datetime.date.today()
# Database connection and form input
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
form = cgi.FieldStorage()
shop_id = form.getvalue("id")
start_date = form.getvalue("start_date")
end_date = form.getvalue("end_date")
# Fetch shop details
q = """SELECT * FROM mechanicshops WHERE id=%s"""
cur.execute(q, (shop_id,))
res = cur.fetchall()
con.close()

# Start HTML
print("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Completed Requests | RoadNova</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" />
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet" />
  <style>
    .sidebar {
      color: #050a30!important;
      min-height: 100vh;
      width: 250px!important;
      background-color: #b1d4e0!important;
    }
    .sidebar .nav-link {
      color: #050a30!important;
    }
    .sidebar .nav-link:hover,
    .sidebar .nav-link.active {
      background-color: #2e8bc0!important;
      color: white;
    }
    @media (max-width: 768px) {
      .sidebar {
        position: fixed;
        top: 56px;
        left: -250px;
        transition: left 0.3s ease-in-out;
      }
      .sidebar.show {
        left: 0;
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
    .filter-card {
  width: 500px;
  margin-left: 670px;
}

@media (max-width: 768px) {
  .filter-card {
    margin-left: 0;
    margin-right: 0;
    width: 100%;
  }
}
@media (max-width: 768px) {
  .sidebar {
    position: fixed;
    top: 56px;
    left: -250px;
    width: 250px;
    height: calc(100vh - 56px);
    transition: left 0.3s ease-in-out;
    z-index: 1050; /* Added */
  }

  .sidebar.show {
    left: 0;
  }

  .overlay {
    display: none;
    position: fixed;
    top: 56px;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1049; /* Slightly less than sidebar */
  }

  .overlay.show {
    display: block;
  }
}
.profile-button {
  background-color: #2e8bc0;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 50px; /* This creates the capsule shape */
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
.profile-button:hover {
  background-color: #1a6a9b;
}
.profile-button a {
  color: white;
  text-decoration: none;
}

  </style>
</head>
""")

# Loop to print shop-specific header
for i in res:
    profile_img = i[9]
    shop_name = i[10]
    print(f"""
    <body>
     <nav class="navbar navbar-dark bg-white shadow-sm">
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
          <nav class="col-md-3 col-lg-2 sidebar d-md-block p-0" id="sidebarMenu">
            <h5 class="text-center py-3">{shop_name}</h5>
            <ul class="nav flex-column">
              <li class="nav-item"><a class="nav-link active" href="mech.py?id={shop_id}"><i class="bi bi-speedometer2 me-2"></i>Dashboard</a></li>
              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="collapse" href="#serviceSubmenu" role="button" aria-expanded="false" aria-controls="serviceSubmenu">
                  <i class="bi bi-wrench-adjustable"></i> Services
                </a>
                <div class="collapse" id="serviceSubmenu">
                  <ul class="nav flex-column ms-3">
                    <li class="nav-item"><a class="nav-link" href="add_service.py?id={shop_id}"><i class="bi bi-bag-plus-fill"></i> Add services</a></li>
                    <li class="nav-item"><a class="nav-link" href="view_services.py?id={shop_id}"><i class="bi bi-eye"></i> View services</a></li>
                  </ul>
                </div>
              </li>
              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="collapse" href="#employeeSubmenu" role="button" aria-expanded="false" aria-controls="employeeSubmenu">
                  <i class="bi bi-tools me-2"></i>Employees
                </a>
                <div class="collapse" id="employeeSubmenu">
                  <ul class="nav flex-column ms-3">
                    <li class="nav-item"><a class="nav-link" href="add.py?id={shop_id}"><i class="bi bi-person-plus me-2"></i>Add Mechanic</a></li>
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
              <li class="nav-item"><a class="nav-link" href="home.py"><i class="bi bi-box-arrow-right me-2"></i>Logout</a></li>
            </ul>
          </nav>
           <div id="sidebarOverlay" style="display:none; position: fixed; top: 0; left: 0; width:100%; height:100%; background: rgba(0,0,0,0.5); z-index:1049;"></div>

          <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-4">
    """)

print(f"""
<div class="container py-4">
<h2 style="color:green;text-align:center">Completed Requests</h2>
<div class="card shadow-sm mb-4 filter-card">

  <div class="card-body">
    <form method="get" action="completed.py" class="row g-3 align-items-end">
      <input type="hidden" name="id" value="{shop_id}">
      <div class="col-md-4">
        <label for="start_date" class="form-label"><i class="bi bi-calendar-range-fill me-2"></i>Start Date</label>
        <input type="date" class="form-control" name="start_date" id="start_date" value="{start_date if start_date else ''}">
      </div>
      <div class="col-md-4">
        <label for="end_date" class="form-label"><i class="bi bi-calendar-range me-2"></i>End Date</label>
        <input type="date" class="form-control" name="end_date" id="end_date" value="{end_date if end_date else ''}">
      </div>
      <div class="col-md-4 d-flex align-items-end">
        <button type="submit" class="btn btn-success w-100"><i class="bi bi-funnel-fill me-2"></i>Apply Filter</button>
      </div>
    </form>
  </div>
</div>
""")

print("""


  <div class="table-responsive">
    <table class="table table-striped table-hover table-bordered align-middle">
      <thead class="table-dark">
        <tr>
          <th>S.NO</th>
          <th>Problem</th>
          <th>Completed Date</th>
          <th>Name of mechanic</th>
          <th>Name of customer</th>
          <th>Payment Details</th>
          <th>Customer Details</th>
          <th>Rating</th>
          <th>Review</th>
        </tr>
      </thead>
      <tbody>
""")

# Fetch completed requests
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

query = """
  SELECT
    r.request_id, r.problem_type, r.request_date, r.status, r.price, r.extra_charge, r.total_charge,
    u.name, u.phone, u.email, u.address,
    m.name AS mechanic_name, MAX(re.rating) AS rating, MAX(re.review_text) AS review_text
  FROM
    service_requests r
    JOIN users u ON r.user_id = u.user_id
    JOIN mechanics m ON r.mech_id = m.mech_id
    LEFT JOIN reviews re ON re.request_id = r.request_id
  WHERE
    r.shop_id = %s AND r.status = 'Completed'
"""
params = [shop_id]

if start_date and not end_date:
    query += " AND DATE(r.request_date) BETWEEN %s AND %s"
    params.extend([start_date, today])

elif end_date and not start_date:
    query += " AND DATE(r.request_date) <= %s"
    params.append(end_date)

elif start_date and end_date:
    query += " AND DATE(r.request_date) BETWEEN %s AND %s"
    params.extend([start_date, end_date])

# Add the GROUP BY clause
query += """
  GROUP BY
    r.request_id, r.problem_type, r.request_date, r.status, r.price, r.extra_charge, r.total_charge,
    u.name, u.phone, u.email, u.address,
    m.name
"""

cur.execute(query, tuple(params))
rows = cur.fetchall()




sn = 1
for req_id, prob, req_date, status, price, extra_charge, total_charge, name, phone, email, addr, mech_name, rating, review_text in rows:
    # Modal IDs
    payment_modal_id = f"paymentModal{req_id}"
    modal_id = f"customerModal{req_id}"
    review_modal_id = f"reviewModal{req_id}"

    cur.execute("SELECT amount, method, paid_on, type FROM payments WHERE service_id = %s", (req_id,))
    payments = cur.fetchall()

    pay_status = "Paid" if payments else "Unpaid"

    payment_list_html = ""

    if payments:
        for p_amount, p_method, p_paid_on, p_type in payments:
            p_paid_on_formatted = p_paid_on.strftime('%d/%m/%Y %I:%M %p') if p_paid_on else "N/A"
            payment_list_html += f"""
                <li class="list-group-item">
                    <strong>Type:</strong> {p_type.capitalize()}<br>
                    <strong>Amount:</strong> ₹{p_amount}<br>
                    <strong>Method:</strong> {p_method}<br>
                    <strong>Paid On:</strong> {p_paid_on_formatted}
                </li>
                <hr>
            """
    else:
        payment_list_html = "<li class='list-group-item'>No payment records found.</li>"

    star_rating_html = ""
    # Check if the rating is not None and is a number
    if rating is not None:
        # Loop from 1 to 5 to create the stars
        for star in range(1, 6):
            # If the current star number is less than or equal to the rating, show a filled star
            if star <= rating:
                star_rating_html += '<i class="bi bi-star-fill text-warning"></i>'
            # Otherwise, show an empty star
            else:
                star_rating_html += '<i class="bi bi-star text-warning"></i>'
    else:
        # If there is no rating, display a message
        star_rating_html = "Not Rated"
    review_cell_html = ""
    if review_text:
        review_cell_html = f"""
               <button type="button" class="btn btn-dark btn-sm" data-bs-toggle="modal" data-bs-target="#{review_modal_id}">
                 View Review
               </button>
           """
    else:
        review_cell_html = "No Review"
    # Row in table
    print(f"""
    <tr>
      <td>{sn}</td>
      <td>{prob}</td>
      <td>{req_date.strftime('%d-%m-%Y')}</td>
      <td>{mech_name}</td>
      <td>{name}</td>
      <td>
        <button type="button" class="btn btn-primary btn-sm" data-bs-toggle="modal" data-bs-target="#{payment_modal_id}">
          View Payment
        </button>
      </td>
      <td>
        <button type="button" class="btn btn-info btn-sm" data-bs-toggle="modal" data-bs-target="#{modal_id}">
          View Customer
        </button>
      </td>
      <td>{star_rating_html}</td>
     <td>{review_cell_html}</td>
    </tr>

    <!-- Payment Modal -->
    <div class="modal fade" id="{payment_modal_id}" tabindex="-1" aria-labelledby="{payment_modal_id}Label" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content shadow-lg">
          <div class="modal-header bg-primary text-white">
            <h5 class="modal-title" id="{payment_modal_id}Label">
              <i class="bi bi-credit-card-2-front-fill me-2"></i>Payment Details
            </h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <ul class="list-group list-group-flush">
              <li class="list-group-item"><strong>Service Charge:</strong> ₹{price}</li>
              <li class="list-group-item"><strong>Extra Charge:</strong> ₹{extra_charge}</li>
              <li class="list-group-item"><strong>Total Charge:</strong> ₹{total_charge}</li>
              {payment_list_html}
              <li class="list-group-item"><strong>Status:</strong> 
                <span class="badge bg-{'success' if pay_status == 'Paid' else 'warning'}">{pay_status}</span>
              </li>
            </ul>
          </div>
          <div class="modal-footer">
            <button class="btn btn-outline-secondary btn-sm" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Customer Modal -->
    <div class="modal fade" id="{modal_id}" tabindex="-1" aria-labelledby="{modal_id}Label" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="{modal_id}Label">Customer Details</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Phone:</strong> {phone}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Address:</strong> {addr}</p>
            <p><strong>Status:</strong> <span class="badge bg-warning text-dark">{status}</span></p>
          </div>
          <div class="modal-footer">
            <button class="btn btn-secondary btn-sm" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
    
    <div class="modal fade" id="{review_modal_id}" tabindex="-1" aria-labelledby="{review_modal_id}Label" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content shadow-lg">
          <div class="modal-header bg-dark text-white">
            <h5 class="modal-title" id="{review_modal_id}Label">
              <i class="bi bi-chat-dots-fill me-2"></i>Customer Review
            </h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p class="lead text-center fst-italic">"{review_text}"</p>
          </div>
          <div class="modal-footer">
            <button class="btn btn-outline-secondary btn-sm" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
    """)

    sn += 1


if not rows:
    print('<tr><td colspan="7" class="text-center">No completed requests found.</td></tr>')

# Close HTML
print("""
      </tbody>
    </table>
  </div>
</div>
</main>
<script>
     const toggleBtn = document.getElementById('toggleSidebar');
  const sidebar = document.getElementById('sidebarMenu');
  const overlay = document.getElementById('sidebarOverlay');


  toggleBtn.addEventListener('click', () => {
    sidebar.classList.toggle('show');
    overlay.classList.toggle('show');
  });

  overlay.addEventListener('click', () => {
    sidebar.classList.remove('show');
    overlay.classList.remove('show');
  });
            </script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")

con.close()
