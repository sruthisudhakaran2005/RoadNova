#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe

print("Content-Type: text/html\r\n\r\n")

import pymysql, cgi, cgitb

cgitb.enable()

import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

form = cgi.FieldStorage()
user_id = form.getvalue("user_id")
cur.execute("SELECT COUNT(*) FROM notifications WHERE user_id=%s AND status='unseen'", (user_id,))
notification_count = cur.fetchone()[0]
if not user_id:
    print("<h2>User ID not provided!</h2>")
    con.close()
    exit()

q = "SELECT * FROM users WHERE user_id=%s"
cur.execute(q, (user_id,))
res = cur.fetchall()

if not res:
    print(f"<h2>No user found with ID: {user_id}</h2>")
    con.close()
    exit()

print("""
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Current Bookings | RoadNova </title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .navbar-custom {
      background-color: azure;
    }

    .logo {
      border-radius: 50%;
      height: 60px;
      margin-right: 10px;
    }

    .mainhead {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      font-weight: 500;
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

    .help:hover {
      color: rgb(255, 106, 0);
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
      position: fixed;
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
      background: linear-gradient(to right, #ff4500, #ff6347); /* red-orange gradient */
      color: white;
      border: none;
      border-radius: 25px;
      padding: 8px 18px;
      font-weight: 500;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
      transition: all 0.3s ease;
    }

    .profile-btn:hover {
      background: #d62900; /* darker red-orange on hover */
      color: #fff;
      transform: scale(1.05);
      box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }

    .container {
      margin-top: 100px;
      margin-left: auto;
      margin-right: auto;
      max-width: 800px;
      width: 80%;
    }
    .notification-btn {
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}
  </style>
</head>
<body>
<div class="overlay" id="overlay"></div>
""")

for i in res:
    name = i[1]
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
            <span style="position: absolute; top: 0px; right: 8px; font-weight: bold; font-size: 17px; color: white;">
              {notification_count if notification_count > 0 else ""}
            </span>
          </button>
          </a>
          <a href="user_profile.py?user_id={user_id}"><button class="btn profile-btn">
            <i class="bi bi-person-circle"></i> Profile
          </button></a>
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
    """)

print("""
<div class="container">
  <h2 class="mb-4 text-center" style="color:#ff8300">On Going Service</h2>
""")
query = """
SELECT sr.request_id, sr.problem_type, sr.request_date,
       ms.shop_name, ms.shop_address, ms.phone, ms.shop_image , sr.status
FROM service_requests sr
LEFT JOIN mechanicshops ms ON sr.shop_id = ms.id
WHERE sr.user_id = %s AND sr.status = 'Pending'
"""

cur.execute(query, (user_id,))
res = cur.fetchall()

query = """
SELECT sr.request_id, sr.problem_type, sr.request_date, sr.price,
       ms.shop_name, ms.shop_address, ms.phone, ms.shop_image, m.name, sr.shop_id, sr.payment_status,
       sr.extra_charge, sr.extra_charge_status, sr.status
FROM service_requests sr
LEFT JOIN mechanicshops ms ON sr.shop_id = ms.id
LEFT JOIN mechanics m ON sr.mech_id = m.mech_id
WHERE sr.user_id = %s AND sr.status = 'Approved'
"""

cur.execute(query, (user_id,))
results = cur.fetchall()
if res:
    for i in res:
        shop_img = i[6]
        req_id = i[0]
        problem = i[1]
        date = i[2]
        shop_name = i[3]
        shop_address = i[4]
        phone = i[5]
        status = i[7]

        print(f"""
                <div class="card mb-4 shadow-sm">
          <div class="row g-0">
            <div class="col-md-4">
              <img src="/roadassist/images/{shop_img}" class="img-fluid rounded-start h-100 w-auto" style="object-fit: cover;" alt="{shop_name}">
            </div>

            <div class="col-md-8">
              <div class="card-body">
                <h5 class="card-title text-success mb-2">🔧 Problem: {problem}</h5>




                <p class="card-text mb-1"><strong>Date:</strong> {date.strftime('%d-%b-%Y %I:%M %p')}</p>
                <p class="card-text mb-1"><strong>Shop:</strong> {shop_name}</p>
                <p class="card-text mb-1"><strong>Address:</strong> {shop_address}</p>
                <p class="card-text mb-1"><strong>Contact:</strong> {phone}</p>
                <p class="card-text mb-1"><strong>Status:<p style="color:red;margin-left:55px;margin-top:-29px;">{status}</p></strong></p>


                <div class="mb-6">
                <div class="d-flex flex-wrap  align-items-center">
                  <a href="https://www.google.com/maps/search/?api=1&query={shop_address.replace(' ', '+')}" target="_blank" class="btn btn-outline-primary btn-sm">
                    <i class="bi bi-geo-alt-fill"></i> View on Map
                  </a>
                    <form method="post" action="cancel_service.py" class="d-inline" onsubmit="return confirm('Are you sure you want to cancel this booking?');">
                      <input type="hidden" name="request_id" value="{req_id}">
                      <button type="submit" class="btn btn-danger btn-sm" style="margin-left:10px;">
                        <i class="bi bi-x-circle"></i> Cancel
                      </button>

                    </form>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        """)

if results:
    if results:
        for i in results:
            shop_img = i[7]
            req_id = i[0]
            problem = i[1]
            date = i[2]
            shop_name = i[4]
            shop_address = i[5]
            phone = i[6]
            mech_name = i[8]
            status_approved = i[13]
            shop_id = i[9]

            price = i[3] or 0
            pay_status = i[10] or 'Not Paid'

            extra_charge = i[11] or 0
            extra_charge_status = i[12] or 'Not Paid'

            # Fetch payment details for the current request
            q = "SELECT method, type FROM payments WHERE service_id=%s"
            cur.execute(q, (req_id,))
            payment_res = cur.fetchall()

            # Initialize payment variables
            method_first_payment = None
            method_extra_charge = None

            if payment_res:
                for payment in payment_res:
                    if payment[1] == 'first':
                        method_first_payment = payment[0]
                    elif payment[1] == 'second':
                        method_extra_charge = payment[0]

            payment_status_display = pay_status
            extra_status_display = extra_charge_status

            # Determine the amount to pay
            amount_to_pay = 0
            if payment_status_display != 'Paid' and extra_status_display != 'Paid':
                amount_to_pay = price + extra_charge
            elif payment_status_display != 'Paid':
                amount_to_pay = price
            elif extra_status_display != 'Paid':
                amount_to_pay = extra_charge

            print(f"""
            <div class="card mb-4 shadow-sm">
              <div class="row g-0">
                <div class="col-md-4">
                  <img src="/roadassist/images/{shop_img}" class="img-fluid rounded-start h-100 w-100" style="object-fit: cover;" alt="{shop_name}">
                </div>

                <div class="col-md-5">
                  <div class="card-body">
                    <h5 class="card-title text-success mb-2">🔧 Problem: {problem}</h5>
                    <p class="card-text mb-1"><strong>Date:</strong> {date.strftime('%d-%b-%Y %I:%M %p')}</p>
                    <p class="card-text mb-1"><strong>Shop:</strong> {shop_name}</p>
                    <p class="card-text mb-1"><strong>Address:</strong> {shop_address}</p>
                    <p class="card-text mb-1"><strong>Contact:</strong> {phone}</p>
                    <div class="mb-3">
                      <a href="https://www.google.com/maps/search/?api=1&query={shop_address.replace(' ', '+')}" target="_blank" class="btn btn-outline-primary btn-sm">
                        <i class="bi bi-geo-alt-fill"></i> View on Map
                      </a>
                      <form method="post" action="cancel_service.py" class="d-inline" onsubmit="return confirm('Are you sure you want to cancel this booking?Note: 25% of the service charge will be deducted as a cancellation fee.You will receive a 75% refund of the service charge.
                      ');">
                        <input type="hidden" name="request_id" value="{req_id}">
                        <button type="submit" class="btn btn-danger btn-sm ms-2">
                          <i class="bi bi-x-circle"></i> Cancel
                        </button>
                      </form>
                    </div>
                  </div>
                </div>

                <div class="col-md-3 d-flex align-items-center">
                  <div class="card-body">
                  <p class="card-text mb-2"><strong>Status:<p style="color:green;margin-top:-32px;margin-left:55px;">{status_approved}</p></strong></p>
                    <p class="card-text mb-2"><strong>Mechanic:</strong> {mech_name if mech_name else 'Not Assigned'}</p>
                   <p class="card-text mb-2">
                      <strong>Service Charge:</strong> ₹{price if price > 0 else 'charge will apply according to your service'}<br>
                      {"<strong>Extra Charge:</strong> ₹" + str(extra_charge) + "<br>" if extra_charge > 0 else ""}
                    </p>

                    <h6 style="color:green;">
                      {payment_status_display} 
                      {" | Extra " + extra_status_display if extra_charge > 0 and extra_status_display != 'Paid' else ""}
                    </h6>

                    {f'''
                        <button type="button" class="btn btn-warning w-100" data-bs-toggle="modal" data-bs-target="#paymentModal{req_id}">
                          <i class="bi bi-credit-card"></i> Pay Now
                        </button>
                    ''' if amount_to_pay > 0 else f'''
                        <button type="button" class="btn btn-success w-100" disabled>
                          <i class="bi bi-check-circle"></i> All Paid
                        </button>
                    '''}
                  </div>

                  <div class="modal fade" id="paymentModal{req_id}" tabindex="-1" aria-labelledby="paymentModalLabel{req_id}" aria-hidden="true">
                    <div class="modal-dialog">
                      <form method="post" action="process_payment.py?user_id={user_id}" onsubmit="return validatePaymentForm('{req_id}')">
                        <div class="modal-content">
                          <div class="modal-header">
                            <h5 class="modal-title" id="paymentModalLabel{req_id}">Payment for Service </h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                          </div>
                          <div class="modal-body">
            """)

            if amount_to_pay > 0:
                print(f"""
                    <p><strong>Amount:</strong> ₹{amount_to_pay}</p>
                """)
                # Conditionally show the note only for the service charge
                if pay_status != 'Paid' and pay_status != 'On Hand':
                    print("""
                    <p class="text-danger"><small>Note: Additional charges may apply based on service complexity.</small></p>
                    """)
            else:
                print("""
                    <p class="text-success"><strong>All charges paid. No pending payment.</strong></p>
                """)

            print(f"""
                            <input type="hidden" name="request_id" value="{req_id}">
                            <input type="hidden" name="amount" value="{amount_to_pay}">
                            <input type="hidden" name="shop_id" value="{shop_id}">
                            <div class="mb-3">
                              <label for="paymentMethod{req_id}" class="form-label">Select Payment Method</label>
                              <select class="form-select" id="paymentMethod{req_id}" name="payment_method" required onchange="toggleFields('{req_id}')">
                                <option value="">-- Choose --</option>
                                <option value="UPI">UPI</option>
                                <option value="Credit Card">Credit Card</option>
                                <option value="Cash">Cash</option>
                              </select>
                            </div>

                            <div id="upiField{req_id}" class="d-none">
                              <label for="upiId{req_id}" class="form-label">Enter UPI ID</label>
                              <input type="text" class="form-control" id="upiId{req_id}" name="upi_id" placeholder="e.g. user@upi">
                            </div>

                            <div id="creditCardFields{req_id}" class="d-none">
                              <label for="cardNumber{req_id}" class="form-label">Card Number</label>
                              <input type="text" class="form-control mb-2" id="cardNumber{req_id}" name="card_number" placeholder="XXXX XXXX XXXX XXXX" maxlength="19">

                              <label for="expiry{req_id}" class="form-label">Expiry Date</label>
                              <input type="month" class="form-control mb-2" id="expiry{req_id}" name="expiry">

                              <label for="cvv{req_id}" class="form-label">CVV</label>
                              <input type="password" class="form-control" id="cvv{req_id}" name="cvv" maxlength="3">
                            </div>
                          </div>
                          <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
            """)

            if amount_to_pay > 0:
                print('<button type="submit" class="btn btn-success">Confirm Payment</button>')
            else:
                print('<button type="button" class="btn btn-success" disabled>Paid</button>')

            print("""
                          </div>
                        </div>
                      </form>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            """)

print("""
</div>

<script>
  const sidebar = document.getElementById('sidebar');
  const sidebarToggleBtn = document.getElementById('sidebarToggleBtn');
  const overlay = document.getElementById('overlay');

  sidebarToggleBtn.addEventListener('click', () => {
    sidebar.classList.toggle('show');
    overlay.classList.toggle('show');
  });

  overlay.addEventListener('click', () => {
    sidebar.classList.remove('show');
    overlay.classList.remove('show');
  });

  function toggleSubMenu(id) {
    const submenu = document.getElementById(id);
    submenu.classList.toggle('d-none');
  }
  function toggleFields(reqId) {{
  const method = document.getElementById('paymentMethod' + reqId).value;

  document.getElementById('upiField' + reqId).classList.add('d-none');
  document.getElementById('creditCardFields' + reqId).classList.add('d-none');

  if (method === 'UPI') {{
    document.getElementById('upiField' + reqId).classList.remove('d-none');
  }}else if (method === 'Credit Card') {{
    document.getElementById('creditCardFields' + reqId).classList.remove('d-none');
  }}
}}

function validatePaymentForm(reqId) {{
  const method = document.getElementById('paymentMethod' + reqId).value;

  if (method === 'UPI') {{
    const upi = document.getElementById('upiId' + reqId).value.trim();
    if (!upi || !upi.includes('@')) {{
      alert('Please enter a valid UPI ID.');
      return false;
    }}
  }} else if (method === 'Credit Card') {{
    const card = document.getElementById('cardNumber' + reqId).value.trim();
    const expiry = document.getElementById('expiry' + reqId).value.trim();
    const cvv = document.getElementById('cvv' + reqId).value.trim();

    if (!card || card.replace(/\s/g, '').length !== 16 || !/^\d+$/.test(card.replace(/\s/g, ''))) {{
      alert('Please enter a valid 16-digit card number.');
      return false;
    }}

    if (!expiry) {{
      alert('Please select an expiry date.');
      return false;
    }}else {{
      const today = new Date();
      const [year, month] = expiry.split('-').map(Number);
      const expiryDate = new Date(year, month, 0);

      if (expiryDate < today) {{
        alert('The card expiry date cannot be in the past.');
        return false;
      }}
    }}

    if (!cvv || cvv.length !== 3) {{
      alert('Please enter a valid 3-digit CVV.');
      return false;
    }}
}}

  return true; // allow form to submit
}}

</script>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>
""")

con.close()