#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')
print("content-type:text/html \r\n\r\n")

import pymysql, cgi, cgitb, os

cgitb.enable()
form = cgi.FieldStorage()
id = form.getvalue("id")

# Fetch mechanic shop info
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
cur.execute("SELECT * FROM mechanicshops WHERE id=%s", (id,))
shop_data = cur.fetchall()
for i in shop_data:
    profile_img = i[9]
    shop_name = i[10]

print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <title>On going service | RoadNova</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" />
      <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet" />
      <style>
             .sidebar {
        color: #050a30 !important;
        min-height: 100vh;
        width: 250px;
        background-color: #b1d4e0;
      }

      .sidebar .nav-link {
        color: #050a30 !important;
        font-weight: 500;
      }

      .sidebar .nav-link:hover,
      .sidebar .nav-link.active {
        background-color: #2e8bc0 !important;
        color: #ffffff !important;
      }

        .form-container {
          max-width: 600px;
          background: #ffffff;
          padding: 30px;
          margin: auto;
          border-radius: 10px;
          box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h2 {
          text-align: center;
          margin-bottom: 25px;
        }
        label {
          display: block;
          margin-top: 15px;
          font-weight: bold;
        }
        input[type="text"],
        input[type="email"],
        input[type="tel"],
        input[type="number"],
        input[type="date"],
        select,
        textarea {
          width: 100%;
          padding: 10px;
          margin-top: 5px;
          border: 1px solid #ccc;
          border-radius: 5px;
          box-sizing: border-box;
        }
        input[type="submit"] {
          background-color: #28a745;
          color: white;
          padding: 12px;
          margin-top: 20px;
          border: none;
          width: 100%;
          border-radius: 5px;
          cursor: pointer;
          font-size: 16px;
        }
        input[type="submit"]:hover {
          background-color: #218838;
        }
        @media (max-width: 600px) {
          .form-container {
            padding: 20px;
          }
          h2 {
            font-size: 22px;
          }
        }
        @media (max-width: 768px) {
            .sidebar {
              position: fixed;
              top: 56px;
              left: -250px;
              width: 250px;
              z-index: 1051;
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
              z-index: 1050;
            }
            .overlay.show {
              display: block;
            }
            main {
              margin-left: 0 !important;
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
    <body>
    """)
print(f"""
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
                  <li class="nav-item"><a class="nav-link" href="add_service.py?id={id}" onclick="showSection('addservice')"><i class="bi bi-bag-plus-fill"></i> Add services</a></li>
                  <li class="nav-item"><a class="nav-link" href="view_services.py?id={id}" onclick="showSection('services')"><i class="bi bi-eye"></i> View services</a></li>
                </ul>
              </div>
            </li>
            <li class="nav-item">
              <a class="nav-link" data-bs-toggle="collapse" href="#employeeSubmenu" role="button" aria-expanded="false" aria-controls="employeeSubmenu">
                <i class="bi bi-tools me-2"></i>Employees
              </a>
              <div class="collapse" id="employeeSubmenu">
                <ul class="nav flex-column ms-3">
                  <li class="nav-item"><a class="nav-link" href="add.py?id={id}" onclick="showSection('addMechanic')"><i class="bi bi-person-plus me-2"></i>Add Mechanic</a></li>
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
    <div class="container py-4">
        <div class="table-responsive">
          <table class="table table-striped table-hover table-bordered align-middle">
            <thead class="table-dark">
              <tr>
                <th>S.NO</th>
                <th>Booked On</th>
                <th>Issue</th>
                <th>Assisting Mechanic</th>
                <th>Service Charge</th>
                <th>Payment Status</th>
                <th>Additional Charge</th>
                <th>Extra Charge Status</th>
                <th>Customer Info</th>
                <th>Total Charge</th>
                <th>Payment Details</th>
                <th>Actions</th>
                <th>Status</th>
                <th>Cancel Service</th>
              </tr>
            </thead>
            <tbody>
    """)
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
cur.execute("""
  SELECT
    r.request_id, r.problem_type, r.location, r.request_date, r.status,
    r.price, r.payment_status, u.name, u.phone, u.email, u.address,
    m.name, r.extra_charge, r.extra_charge_status,
    r.refund, r.refund_date
  FROM service_requests r
  JOIN users u ON r.user_id = u.user_id
  JOIN mechanics m ON r.mech_id = m.mech_id
  WHERE r.shop_id = %s 
    AND (
      r.status = 'Approved' 
      OR (r.status = 'Cancelled' AND r.refund IS NOT NULL AND r.refund_status IS NULL)
    )
""", (id,))
rows = cur.fetchall()

sn = 1

for row in rows:
    request_id, problem_type, location, request_date, status, price, payment_status, cust_name, phone, email, address, mech_name, ex_charge, ex_charge_status, refund , refund_date = row

    ex_charge = ex_charge or 0
    total_charge = price + ex_charge

    # Logic for Extra Charge Status
    extra_charge_display = ""
    if ex_charge_status == 'Pending':
        extra_charge_display = '<span class="badge bg-warning">Pending</span>'
    elif ex_charge_status == 'On Hand':
        extra_charge_display = f"""
            <form method="post" action="update_extra_charge_status.py?shop_id={id}">
                <input type="hidden" name="request_id" value="{request_id}">
                <button type="submit" class="btn btn-success btn-sm">Received</button>
            </form>
        """
    elif ex_charge_status == 'Paid':
        extra_charge_display = '<span class="badge bg-success">Paid</span>'
    else:
        extra_charge_display = 'N/A'

    cur.execute("SELECT method, paid_on FROM payments WHERE service_id=%s AND type='first'", (request_id,))
    payment = cur.fetchone()

    # Initialize with default values
    method = "N/A"
    paid_on = None
    if payment:
        method = payment[0]
        paid_on = payment[1]

    # Fetch EXTRA charge payment info
    extra_charge_method = "N/A"
    extra_charge_paid_on = None
    if ex_charge_status == 'Paid':
        cur.execute("SELECT method, paid_on FROM payments WHERE service_id=%s AND type='second'", (request_id,))
        extra_payment = cur.fetchone()
        if extra_payment:
            extra_charge_method = extra_payment[0]
            extra_charge_paid_on = extra_payment[1]

    # Determine correct status badge
    if payment_status.lower() == "paid":
        payment_status_display = '<span class="badge bg-success">Paid</span>'
    else:
        payment_status_display = '<span class="badge bg-warning">Pending</span>'

    # Logic for Cash payments and 'Receive Payment' button
    payment_info_display = ""
    if method.lower() == 'cash' and payment_status.lower() == 'on hand':
        payment_info_display = f"""
            <form method="post" action="update_payment.py?shop_id={id}">
                <input type="hidden" name="request_id" value="{request_id}">
                <p><strong>Method:</strong> Cash</p>
                <button type="submit" class="btn btn-success btn-sm">Receive Payment</button>
            </form>
        """
    elif method.lower() == 'cash' and payment_status.lower() == 'paid':
        paid_on_display = paid_on.strftime('%d-%b-%Y %I:%M %p') if isinstance(paid_on, datetime) else 'N/A'
        payment_info_display = f"""
            <p><strong>Method:</strong> Cash</p>
            <p><strong>Paid On:</strong> {paid_on_display}</p>
            <p><strong>Status:</strong> <span class="badge bg-success">Paid</span></p>
        """
    else:
        paid_on_display = paid_on.strftime('%d-%b-%Y %I:%M %p') if isinstance(paid_on, datetime) else 'N/A'
        payment_info_display = f"""
            <p><strong>Method:</strong> {method}</p>
            <p><strong>Paid On:</strong> {paid_on_display}</p>
            <p><strong>Status:</strong> {payment_status_display}</p>
        """

    # Add extra payment info to the modal content
    if extra_charge_method != 'N/A':
        payment_info_display += f"""
        <hr>
        <h6>Extra Charge Payment</h6>
        <p><strong>Method:</strong> {extra_charge_method}</p>
        <p><strong>Paid On:</strong> {extra_charge_paid_on.strftime('%d-%b-%Y %I:%M %p') if isinstance(extra_charge_paid_on, datetime) else 'N/A'}</p>
        <p><strong>Status:</strong> <span class="badge bg-success">Paid</span></p>
        """
    # If extra charge is 'On Hand', display the "Receive" button
    if ex_charge_status == 'On Hand':
        payment_info_display += f"""
            <hr>
            <h6>Extra Charge Payment</h6>
            <form method="post" action="update_extra_charge_status.py?shop_id={id}">
                <input type="hidden" name="request_id" value="{request_id}">
                <p><strong>Status:</strong> <span class="badge bg-warning">On Hand</span></p>
                <button type="submit" class="btn btn-success btn-sm">Receive Payment</button>
            </form>
        """

    print(f"""
      <tr>
        <td>{sn}</td>
        <td>{request_date.strftime('%d-%b-%Y %I:%M %p')}</td>
        <td>{problem_type}</td>
        <td>{mech_name}</td>
        <td>{price}</td>
        <td><span class="badge bg-{'success' if payment_status.lower() == 'paid' else 'warning'}">{payment_status}</span></td>
        <td>
          {ex_charge}
          {f'''
            <br>
            <button class="btn btn-warning btn-sm mt-1" data-bs-toggle="modal" data-bs-target="#extraChargeModal{request_id}">
              Add Extra Charge
            </button>
          ''' if ex_charge == 0 else ""}
        </td>
        <td>{extra_charge_display}</td>
        <td>
          <button class="btn btn-info btn-sm" data-bs-toggle="modal" data-bs-target="#custModal{request_id}">View Details</button>
        </td>
        <td>{total_charge}</td>
        <td> <button type="button" class="btn btn-primary btn-sm" data-bs-toggle="modal" data-bs-target="#payModal{request_id}">
          View Payment
        </button></td>
        <td>
          <a href="update_request_status.py?request_id={request_id}&status=Completed&shop_id={id}" class="btn btn-success btn-sm">Mark as Completed</a>
        </td>
       
    
          <td>
            {status}
            {""
             if status.lower() == "approved" else f'''
            <form method="post" action="refund_now.py">
            <input type="hidden" name="shop_id" value="{id}">
            <input type="hidden" name="request_id" value="{request_id}">
            <input type="hidden" name="amount" values="{refund}">
            <input type="hidden" name="name" value="{cust_name}">
             <input type="hidden" name="email" value="{email}">
              <input type="hidden" name="service_charge" value="{price}">
               <input type="hidden" name="extra_charge" value="{ex_charge}">
                <input type="hidden" name="total_charge" value="{total_charge}">
              <button type="submit" class="btn btn-sm btn-danger mt-1">Refund Now</button>
            </form>
            '''}
          </td>
           <td><button type="button" class="btn btn-danger btn-sm" data-bs-toggle="modal" data-bs-target="#cancelModal{request_id}">
          Cancel
        </button></td>

         
        
      </tr>

      <div class="modal fade" id="payModal{request_id}" tabindex="-1">
        <div class="modal-dialog modal-sm modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header bg-primary text-white">
              <h5 class="modal-title">Payment Details</h5>
              <button class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
              <div class="modal-body">
            <ul class="list-group list-group-flush">
              <li class="list-group-item"><strong>Service Charge:</strong> ₹{price}</li>
              <li class="list-group-item"><strong>Extra Charge:</strong> ₹{ex_charge}</li>
              <li class="list-group-item"><strong>Total Charge:</strong> ₹{total_charge}</li>
              <li class="list-group-item">
                {payment_info_display}
              </li>
            </ul>
          </div>
            </div>
            <div class="modal-footer">
              <button class="btn btn-secondary btn-sm" data-bs-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div>

      <div class="modal fade" id="custModal{request_id}" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Customer Details</h5>
              <button class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
              <p><strong>Name:</strong> {cust_name}</p>
              <p><strong>Phone:</strong> {phone}</p>
              <p><strong>Email:</strong> {email}</p>
              <p><strong>Location:</strong> {location}</p>
              <p><strong>Status:</strong> {status}</p>
            </div>
            <div class="modal-footer">
              <button class="btn btn-secondary btn-sm" data-bs-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div>

      <div class="modal fade" id="extraChargeModal{request_id}" tabindex="-1" aria-labelledby="extraChargeModalLabel{request_id}" aria-hidden="true">
        <div class="modal-dialog">
          <form method="post" action="update_extra_charge.py?id={id}">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="extraChargeModalLabel{request_id}">Add Extra Charge</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <input type="hidden" name="request_id" value="{request_id}">
                <input type="hidden" name="email" value="{email}">
                <input type="hidden" name="name" value="{cust_name}">
                <div class="mb-3">
                  <label for="extraCharge{request_id}" class="form-label">Extra Charge Amount (₹)</label>
                  <input type="number" step="0.01" min="0" class="form-control" id="extraCharge{request_id}" name="extra_charge" required>
                </div>
                <div class="mb-3">
                  <label for="extraNote{request_id}" class="form-label">Note to Customer</label>
                  <textarea class="form-control" id="extraNote{request_id}" name="extra_note" rows="3" placeholder="Enter note..."></textarea>
                </div>
              </div>
              <div class="modal-footer">
                <button type="submit" class="btn btn-primary">Save</button>
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
              </div>
            </div>
          </form>
        </div>
      </div>

      <div class="modal fade" id="cancelModal{request_id}" tabindex="-1">
        <div class="modal-dialog">
          <form method="post" action="cancel_request.py?shop_id={id}">
            <div class="modal-content">
              <div class="modal-header bg-danger text-white">
                <h5 class="modal-title">Cancel Service</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
              </div>
              <div class="modal-body">
                <input type="hidden" name="request_id" value="{request_id}">
                <input type="hidden" name="email" value="{email}">
                <input type="hidden" name="customer_name" value="{cust_name}">
                <input type="hidden" name="paid_amount" value="{total_charge}">
                <p> Are you sure you want to cancel this service request?</p>
                <p><strong>Note:</strong> Only <span class="text-danger">75%</span> of the paid amount will be refunded to the customer.</p>
              </div>
              <div class="modal-footer">
                <button type="submit" class="btn btn-danger">Cancel & Refund</button>
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    """)
    sn += 1

if not rows:
    print("<tr><td colspan='14' class='text-center'>No approved requests found.</td></tr>")

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