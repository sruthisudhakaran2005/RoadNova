#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
import sys
import datetime
import pymysql
import cgi
import cgitb
import datetime

# Enable CGI tracing for detailed errors
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')
print("Content-Type: text/html\r\n\r\n")

# Connect to DB
try:
    con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
    cur = con.cursor()
except pymysql.MySQLError as e:
    print(f"<p>Database connection failed: {e}</p>")
    sys.exit()

# Get form data
form = cgi.FieldStorage()
user_id = form.getvalue("user_id")

if not user_id:
    print("<div class='alert alert-danger'>User ID is missing.</div>")
    cur.close()
    con.close()
    sys.exit()

# Fetch user details and notification count
cur.execute("SELECT name FROM users WHERE user_id=%s", (user_id,))
user_res = cur.fetchone()
name = user_res[0] if user_res else "User"

cur.execute("SELECT COUNT(*) FROM notifications WHERE user_id=%s AND status='unseen'", (user_id,))
notification_count = cur.fetchone()[0]

# Fetch all completed service requests for the user, grouped by shop
query = """
SELECT sr.request_id, sr.shop_id, sr.problem_type, sr.request_date, sr.mech_id,
       sr.price, sr.extra_charge, sr.total_charge, sr.completed_date
FROM service_requests sr
WHERE sr.user_id = %s AND sr.status = 'Completed'
ORDER BY sr.shop_id, sr.completed_date DESC
"""
cur.execute(query, (user_id,))
completed_requests = cur.fetchall()
modals_html = ""
# Group requests by shop_id
shops_requests = {}
for req in completed_requests:
    shop_id = req[1]
    if shop_id not in shops_requests:
        shops_requests[shop_id] = []
    shops_requests[shop_id].append(req)

# Start HTML output (everything before the table)
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Completed Booking | RoadNova</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">
  <style>
    .card-title {{ font-weight: bold; color: #198754; }}
    .modal-header {{ background-color: #0d6efd; color: white; }}
    .badge-completed {{ background-color: #198754; }}
    body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }}
    .navbar-custom {{ background-color: azure; }}
    .mainhead {{ font-weight: 500; }}
    .sidebar {{ position: fixed; top: 74px; left: -250px; width: 250px; height: 100%; background-color: rgb(253, 248, 248); padding-top: 30px; transition: all 0.3s ease; z-index: 1000; }}
    .sidebar.show {{ left: 0; }}
    .sidebar .nav-link {{ color: #0b0b0b; padding: 15px 20px; }}
    .sidebar .nav-link:hover, .sidebar .nav-link.active {{ background-color: #e2cccc; color: rgb(250, 4, 4); }}
    .overlay {{ top: 0; left: 0; height: 100%; width: 100%; background-color: rgba(0, 0, 0, 0.5); z-index: 990; display: none; }}
    .overlay.show {{ display: block; }}
    .main-content {{ padding: 20px; margin-left: 0; margin-top: 90px; transition: margin-left 0.3s ease; }}
    @media (min-width: 768px) {{ .sidebar {{ left: 0; }} .main-content {{ margin-left: 250px; }} .overlay {{ display: none !important; }} #sidebarToggleBtn {{ display: none; }} }}
    .submenu {{ background-color: #f5f5f5; border-left: 2px solid #ccc; }}
    .submenu .nav-link {{ padding-left: 30px; font-size: 0.95rem; }}
    .profile-btn {{ background: linear-gradient(to right, #ff4500, #ff6347); color: white; border: none; border-radius: 25px; padding: 8px 18px; font-weight: 500; box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: all 0.3s ease; }}
    .profile-btn:hover {{ background: #d62900; color: #fff; transform: scale(1.05); box-shadow: 0 6px 12px rgba(0,0,0,0.15); }}
    .container {{ margin-top: 20px; margin-left: auto; margin-right: auto; max-width: 1200px; width: 95%; }}
    .notification-btn {{ position: relative; width: 40px; height: 40px; border-radius: 50%; padding: 0; display: flex; align-items: center; justify-content: center; }}
    .bi-star-fill {{ color: gold !important; }}
  </style>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-custom fixed-top py-2">
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

<div class="sidebar" id="sidebar">
  <ul class="nav flex-column">
    <li class="nav-item"><a href="user.py?user_id={user_id}" class="nav-link">Home</a></li>
    <li class="nav-item">
      <a href="#" class="nav-link" onclick="toggleSubMenu('bookingSubMenu'); return false;">Booking <i class="bi bi-caret-down-fill"></i></a>
      <ul id="bookingSubMenu" class="nav flex-column ms-3 submenu d-none">
         <li><a href="approved_booking.py?user_id={user_id}" class="nav-link">On Going</a></li>
         <li><a href="completed_booking.py?user_id={user_id}" class="nav-link">Completed</a></li>
         <li><a href="cancelled_booking.py?user_id={user_id}" class="nav-link">Cancelled</a></li>
         <li><a href="rejected_booking.py?user_id={user_id}" class="nav-link">Rejected</a></li>
      </ul>
    </li>
    <li class="nav-item"><a href="shops.py?user_id={user_id}" class="nav-link">Mechanic shops</a></li>
    <li class="nav-item"><a href="home.py" class="nav-link">Logout</a></li>
  </ul>
</div>

<div class="main-content">
  <div class="container">
    <h2 class="mb-4 text-center text-success">Completed Requests</h2>
""")

# Check if there are any completed requests
if shops_requests:
    print("""
    <table class="table table-striped table-hover align-middle">
      <thead class="table-success">
        <tr>
          <th>S.No</th>
          <th>Shop Name</th>
          <th>Shop Address</th>
          <th>Rating</th>
          <th>My Services</th>
        </tr>
      </thead>
      <tbody>
    """)

    modals_html = ""
    serial = 1
    # Iterate through each shop
    for shop_id, requests in shops_requests.items():
        # Fetch shop details
        cur.execute("SELECT shop_name, address, shop_image, owner_email, phone FROM mechanicshops WHERE id=%s",
                    (shop_id,))
        shop_details = cur.fetchone()
        shop_name, shop_address, shop_image, shop_email, shop_phone = shop_details if shop_details else (
        "N/A", "N/A", "default.jpg", "N/A", "N/A")

        # Calculate average rating for the shop
        cur.execute("SELECT AVG(rating) FROM reviews WHERE shop_id=%s", (shop_id,))
        avg_rating = cur.fetchone()[0]
        avg_rating = round(avg_rating) if avg_rating else 0
        stars_html = "&#9733;" * avg_rating + "&#9734;" * (5 - avg_rating)

        # Print table row for the current shop
        print(f"""
        <tr>
          <td>{serial}</td>
          <td>{shop_name}</td>
          <td>{shop_address}</td>
          <td>{stars_html}</td>
          <td>
            <button class="btn btn-warning btn-sm" data-bs-toggle="modal" data-bs-target="#servicesModal{shop_id}">View Services</button>
          </td>
        </tr>
        """)

        # Build the shop details modal


        # Build the services modal for the current shop
        services_table_rows = ""
        request_serial = 1
        for req_id, _, issue, booked_on, mech_id, service_charge, extra_charge, total_charge, _ in requests:
            # Fetch mechanic name
            mech_name = "N/A"
            if mech_id:
                cur.execute("SELECT name FROM mechanics WHERE mech_id=%s", (mech_id,))
                mech_res = cur.fetchone()
                if mech_res:
                    mech_name = mech_res[0]

            # Fetch payment details
            # Fetch all payment details for the service request
            cur.execute("SELECT amount, method, paid_on, type FROM payments WHERE service_id=%s", (req_id,))
            payments = cur.fetchall()

            # Build HTML list of payments
            if payments:
                payment_list_html = ""
                for amount, method, paid_on, ptype in payments:
                    paid_on_formatted = paid_on.strftime('%d-%m-%Y %I:%M %p') if paid_on else "N/A"
                    payment_list_html += f"""
                        <li>
                            <strong>Type:</strong> {ptype.capitalize()}<br>
                            <strong>Amount:</strong> ₹{amount}<br>
                            <strong>Method:</strong> {method}<br>
                            <strong>Paid On:</strong> {paid_on_formatted}
                        </li><hr>
                    """
            else:
                payment_list_html = "<li>No payment records found.</li>"

            # Fetch rating for this specific request
            rating_text = "Add Rating"
            rating_button_color = "btn-warning"
            initial_rating = 0
            initial_review = ""
            cur.execute("SELECT rating, review_text FROM reviews WHERE request_id=%s AND user_id=%s", (req_id, user_id))
            rating_res = cur.fetchone()
            if rating_res:
                initial_rating = rating_res[0] or 0
                initial_review = rating_res[1] or ""
                rating_text = "&#9733;" * round(initial_rating) + "&#9734;" * (5 - round(initial_rating))
                rating_button_color = "btn-success"
            formatted_date = booked_on.strftime('%d-%m-%Y %I:%M %p')
            services_table_rows += f"""
            <tr>
              <td>{request_serial}</td>
              <td>{formatted_date}</td>
              <td>{issue}</td>
              <td>{mech_name}</td>
              <td>
                <button class="btn btn-sm btn-info" data-bs-toggle="modal" data-bs-target="#paymentModal{req_id}">View Bill</button>
              </td>
              <td>
                <button class="btn {rating_button_color} btn-sm" data-bs-toggle="modal" data-bs-target="#reviewModal{req_id}">
                  {rating_text}
                </button>
              </td>
            </tr>
            """

            # Build payment modal
            modals_html += f"""
            <div class="modal fade" id="paymentModal{req_id}" tabindex="-1" aria-labelledby="paymentModal{req_id}Label" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="paymentModal{req_id}Label">Payment Details</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                                      <div class="modal-body">
                        <p><strong>Service Charge:</strong> ₹{service_charge}</p>
                        <p><strong>Extra Charges:</strong> ₹{extra_charge}</p>
                        <p><strong>Total:</strong> ₹{total_charge}</p>
                        <p><strong>Payments:</strong></p>
                        <ul>
                            {payment_list_html}
                        </ul>
                    </div>

                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="modal">Close</button>
                  </div>
                </div>
              </div>
            </div>
            """

            # Build review modal
            modals_html += f"""
            <div class="modal fade" id="reviewModal{req_id}" tabindex="-1" aria-labelledby="reviewModalLabel{req_id}" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                  <form method="post" action="submit_review.py" onsubmit="return validateReviewForm({req_id});">
                    <div class="modal-header">
                      <h5 class="modal-title" id="reviewModalLabel{req_id}">Rate this Service</h5>
                      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body text-center">
                      <img src="./images/{shop_image}" alt="Shop Image" class="img-fluid rounded mb-3" style="max-height: 150px;">
                      <h5>{shop_name}</h5>
                      <p>{shop_address}</p>
                      <label for="rating{req_id}" class="form-label">Your Rating:</label>
                      <div id="starRating{req_id}" class="mb-3"></div>
                      <input type="hidden" name="rating" id="ratingInput{req_id}" value="{initial_rating}" required>
                      <label for="review{req_id}" class="form-label">Your Review:</label>
                      <textarea class="form-control" name="review" id="review{req_id}" rows="3" placeholder="Write your review here...">{initial_review}</textarea>
                      <input type="hidden" name="request_id" value="{req_id}">
                      <input type="hidden" name="user_id" value="{user_id}">
                      <input type="hidden" name="shop_id" value="{shop_id}">
                    </div>
                    <div class="modal-footer">
                      <button type="submit" class="btn btn-primary btn-sm">Submit Review</button>
                      <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="modal">Close</button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
            """
            request_serial += 1

        # Add the services modal for the current shop to modals_html
        modals_html += f"""
        <div class="modal fade" id="servicesModal{shop_id}" tabindex="-1" aria-labelledby="servicesModal{shop_id}Label" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered modal-lg">
            <div class="modal-content">
              <div class="modal-header bg-success text-white">
                <h5 class="modal-title" id="servicesModal{shop_id}Label">Services at {shop_name}</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <table class="table table-bordered table-striped">
                  <thead class="table-light">
                    <tr>
                      <th>S.No</th>
                      <th>Booked On</th>
                      <th>Issue</th>
                      <th>Assisted By</th>
                      <th>Bill</th>
                      <th>Rating</th>
                    </tr>
                  </thead>
                  <tbody>
                    {services_table_rows}
                  </tbody>
                </table>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>
        """
        serial += 1

    print("""
          </tbody>
        </table>
    """)
else:
    print("""
    <div class="alert alert-info text-center" role="alert">
      No completed requests found.
    </div>
    """)

# Print all modals at the end of the main content
print(modals_html)

# End the HTML document
print("""
  </div>
</div>
<script>
  function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('overlay');
    sidebar.classList.toggle('show');
    overlay.classList.toggle('show');
  }

  function toggleSubMenu(id) {
    const submenu = document.getElementById(id);
    submenu.classList.toggle('d-none');
  }

  function createStarRating(id, initialRating) {
    const starContainer = document.getElementById('starRating' + id);
    const ratingInput = document.getElementById('ratingInput' + id);
    if (!starContainer || !ratingInput) return;

    starContainer.innerHTML = '';
    for(let i = 1; i <= 5; i++) {
      const star = document.createElement('i');
      star.classList.add('bi', 'bi-star');
      star.style.fontSize = '1.5rem';
      star.style.cursor = 'pointer';
      star.dataset.value = i;
      star.addEventListener('click', () => {
        ratingInput.value = i;
        highlightStars(starContainer, i);
      });
      starContainer.appendChild(star);
    }
    highlightStars(starContainer, initialRating);
  }

  function highlightStars(container, rating) {
    const stars = container.querySelectorAll('i');
    stars.forEach((star, index) => {
      if(index < rating) {
        star.classList.remove('bi-star');
        star.classList.add('bi-star-fill');
      } else {
        star.classList.remove('bi-star-fill');
        star.classList.add('bi-star');
      }
    });
  }

  function validateReviewForm(id) {
    const rating = document.getElementById('ratingInput' + id).value;
    if(rating < 1) {
      alert('Please provide a star rating.');
      return false;
    }
    return true;
  }

  window.addEventListener('DOMContentLoaded', () => {
    const modals = document.querySelectorAll('[id^="reviewModal"]');
    modals.forEach(modal => {
      modal.addEventListener('shown.bs.modal', function () {
        const id = this.id.replace('reviewModal', '');
        const ratingInput = document.getElementById('ratingInput' + id);
        createStarRating(id, ratingInput ? ratingInput.value : 0);
      });
    });
  });

  document.getElementById('sidebarToggleBtn').addEventListener('click', toggleSidebar);
  const overlay = document.createElement('div');
  overlay.id = 'overlay';
  overlay.classList.add('overlay');
  document.body.appendChild(overlay);
  overlay.addEventListener('click', toggleSidebar);

</script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")

cur.close()
con.close()