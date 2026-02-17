#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe

print("Content-type: text/html\r\n\r\n")

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Test Navbar</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">RoadNova</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item">
          <a class="nav-link" href="#">Home</a>
        </li>
      </ul>
      <h2><a href="mailto:sruthisudhakarn2005@gmail.com">send mail</a></h2>
      
      
      

    </div>
  </div>
</nav>

</body>
</html>
""")
#<td>
 #           <button class="btn btn-sm btn-outline-info" data-bs-toggle="modal" data-bs-target="#customerModal{req_id}">
  #            👤 View
       #     </button>
        #  </td>
        print("""
         <!-- Customer Modal -->
        <div class="modal fade" id="customerModal{req_id}" tabindex="-1">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header bg-info text-white">
                <h5 class="modal-title">Customer Details</h5>
                <button class="btn-close" data-bs-dismiss="modal"></button>
              </div>
              <div class="modal-body">
                <p><strong>Name:</strong> {uname}</p>
                <p><strong>Email:</strong> {uemail}</p>
                <p><strong>Phone:</strong> {uphone}</p>
                <p><strong>Gender:</strong> {ugender}</p>
                <p><strong>Address:</strong> {uaddr}</p>
              </div>
              <div class="modal-footer">
                <button class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>

        """)




#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Content-Type: text/html\r\n\r\n")
import datetime
import pymysql, cgi, cgitb
cgitb.enable()
today = datetime.date.today()

# Connect to DB
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

# Get form data
form = cgi.FieldStorage()
start_date = form.getvalue("start_date")
end_date = form.getvalue("end_date")
user_id = form.getvalue("user_id")
q = "SELECT * FROM users WHERE user_id=%s"
cur.execute(q, (user_id,))
res = cur.fetchall()
cur.execute("SELECT COUNT(*) FROM notifications WHERE user_id=%s AND status='unseen'", (user_id,))
notification_count = cur.fetchone()[0]
# HTML header
print("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Completed Requests</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">
  <style>
    .card-title { font-weight: bold; color: #198754; }
    .modal-header { background-color: #0d6efd; color: white; }
    .badge-completed { background-color: #198754; }
    body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .navbar-custom { background-color: azure; }
    .mainhead { font-weight: 500; }
    .sidebar { position: fixed; top: 74px; left: -250px; width: 250px; height: 100%; background-color: rgb(253, 248, 248); padding-top: 30px; transition: all 0.3s ease; z-index: 1000; }
    .sidebar.show { left: 0; }
    .sidebar .nav-link { color: #0b0b0b; padding: 15px 20px; }
    .sidebar .nav-link:hover, .sidebar .nav-link.active { background-color: #e2cccc; color: rgb(250, 4, 4); }
    .overlay { top: 0; left: 0; height: 100%; width: 100%; background-color: rgba(0, 0, 0, 0.5); z-index: 990; display: none; }
    .overlay.show { display: block; }
    .main-content { padding: 20px; margin-left: 0; margin-top: 90px; transition: margin-left 0.3s ease; }
    @media (min-width: 768px) { .sidebar { left: 0; } .main-content { margin-left: 250px; } .overlay { display: none !important; } #sidebarToggleBtn { display: none; } }
    .submenu { background-color: #f5f5f5; border-left: 2px solid #ccc; }
    .submenu .nav-link { padding-left: 30px; font-size: 0.95rem; }
    .profile-btn { background: linear-gradient(to right, #ff4500, #ff6347); color: white; border: none; border-radius: 25px; padding: 8px 18px; font-weight: 500; box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: all 0.3s ease; }
    .profile-btn:hover { background: #d62900; color: #fff; transform: scale(1.05); box-shadow: 0 6px 12px rgba(0,0,0,0.15); }
    .container { margin-top: 20px; margin-left: auto; margin-right: auto; max-width: 1200px; width: 95%; }.notification-btn {
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}
.bi-star-fill {
  color: gold !important;
}

  </style>
</head>
<body>
""")

# Navbar and Sidebar
for i in res:
    name = i[1]
    print(f"""
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
""")

print("""
<div class="main-content">
  <div class="container">
    <h2 class="mb-4 text-center text-success">Completed Requests</h2>
""")
filter_conditions = "WHERE sr.user_id = %s AND sr.status = 'Completed'"
params = [user_id]

if start_date and end_date:
    filter_conditions += " AND DATE(sr.completed_date) BETWEEN %s AND %s"
    params.extend([start_date, end_date])
elif start_date and not end_date:
    filter_conditions += " AND DATE(sr.completed_date) >= %s"
    params.append(start_date)
elif end_date and not start_date:
    filter_conditions += " AND DATE(sr.completed_date) <= %s"
    params.append(end_date)

query = f"""
SELECT sr.request_id, sr.problem_type, sr.status, sr.completed_date,
       ms.shop_name, ms.address, ms.phone,
       m.name as mechanic_name,
       sr.price, sr.extra_charge, sr.total_charge,
       p.method, p.paid_on, ms.shop_image,
       sr.shop_id, r.rating
FROM service_requests sr
LEFT JOIN mechanicshops ms ON sr.shop_id = ms.id
LEFT JOIN mechanics m ON sr.mech_id = m.mech_id
LEFT JOIN payments p ON p.service_id = sr.request_id
LEFT JOIN reviews r ON r.request_id = sr.request_id AND r.user_id = sr.user_id
{filter_conditions}
ORDER BY sr.request_date DESC
"""

cur.execute(query, tuple(params))
results = cur.fetchall()


if results:
    print(f"""
    <div class="card shadow-sm mb-4" style="width:500px;margin-left:670px;">
      <div class="card-body">
        <form method="post" action="completed_booking.py" class="row g-3 align-items-end">
          <input type="hidden" name="user_id" value="{user_id}">
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
    <table class="table table-striped table-hover align-middle">
      <thead class="table-success">
        <tr>
          <th>S.No</th>
          <th>Problem</th>
          <th>Completed Date</th>
          <th>Shop Name</th>
          <th>Assigned Mechanic</th>
          <th>Shop Details</th>
          <th>Service Charge</th>
          <th>Payment</th>
          <th>Add Review</th>
        </tr>
      </thead>
      <tbody>
    """)

    serial = 1
    for row in results:
        (req_id, problem, status, completed_date,
         shop_name, shop_address, shop_contact,
         mechanic, price, extra_charge, total_charge,
         payment_method, paid_on, shop_image, shop_id, rating) = row

        modal_id = f"billModal{req_id}"

        print(f"""
        <tr>
          <td>{serial}</td>
          <td>{problem}</td>
          <td>{completed_date.strftime('%d-%m-%Y') if completed_date else "N/A"}</td>
          <td>{shop_name}</td>
          <td>{mechanic if mechanic else 'N/A'}</td>
          <td>
            <button class="btn btn-primary btn-sm" data-bs-toggle="modal" data-bs-target="#{modal_id}"> View Details </button>
          </td>
          <td>₹{total_charge if total_charge is not None else (price or 0) + (extra_charge or 0)}</td>
          <td>
            <button class="btn btn-success btn-sm" data-bs-toggle="modal" data-bs-target="#paymentmodal{modal_id}">View Bill </button>
          </td>
          <td>
            <button class="btn btn-warning btn-sm" data-bs-toggle="modal" data-bs-target="#reviewModal{req_id}">
              Add Review
            </button>
          </td>
        </tr>
        """)
        serial += 1

    print("""
      </tbody>
    </table>
    """)

    for row in results:
        (req_id, problem, status, completed_date,
         shop_name, shop_address, shop_contact,
         mechanic, price, extra_charge, total_charge,
         payment_method, paid_on, shop_image, shop_id, rating) = row

        modal_id = f"billModal{req_id}"
        formatted_date = completed_date.strftime('%d-%m-%Y') if completed_date else "N/A"
        paid_on_str = paid_on.strftime('%d %B %Y') if paid_on else "N/A"
        price = price or 0
        extra_charge = extra_charge or 0
        total = total_charge if total_charge is not None else price + extra_charge

        print(f"""
        <div class="modal fade" id="{modal_id}" tabindex="-1" aria-labelledby="{modal_id}Label" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="{modal_id}Label">Shop Details</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <p><strong>Problem:</strong> {problem}</p>
                <p><strong>Shop:</strong> {shop_name}</p>
                <p><strong>Address:</strong> {shop_address}</p>
                <p><strong>Phone:</strong> {shop_contact}</p>
                <p><strong>Mechanic:</strong> {mechanic if mechanic else 'N/A'}</p>
                <p><strong>Date:</strong> {formatted_date}</p>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>

        <div class="modal fade" id="paymentmodal{modal_id}" tabindex="-1" aria-labelledby="paymentmodal{modal_id}Label" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="paymentmodal{modal_id}Label">Payment Details</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <p><strong>Service Charge:</strong> ₹{price}</p>
                <p><strong>Extra Charges:</strong> ₹{extra_charge}</p>
                <p><strong>Total:</strong> ₹{total}</p>
                <p><strong>Payment Method:</strong> {payment_method or 'N/A'}</p>
                <p><strong>Paid On:</strong> {paid_on_str}</p>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>

        <div class="modal fade" id="reviewModal{req_id}" tabindex="-1" aria-labelledby="reviewModalLabel{req_id}" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <form method="post" action="submit_review.py" onsubmit="return validateReviewForm({req_id});">
                <div class="modal-header">
                  <h5 class="modal-title" id="reviewModalLabel{req_id}">Add Review for {shop_name}</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body text-center">
                  <img src="./images/{shop_image}" alt="Shop Image" class="img-fluid rounded mb-3" style="max-height: 150px;">
                  <h5>{shop_name}</h5>
                  <p>{shop_address}</p>

                  <label for="rating{req_id}" class="form-label">Your Rating:</label>
                  <div id="starRating{req_id}" class="mb-3"></div>
                  <input type="hidden" name="rating" id="ratingInput{req_id}" value="{rating or 0}" required>

                  <label for="review{req_id}" class="form-label">Your Review:</label>
                  <textarea class="form-control" name="review" id="review{req_id}" rows="3" placeholder="Write your review here..."></textarea>

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
        """)
else:
    print("""
    <div class="alert alert-info text-center" role="alert">
      No completed requests found.
    </div>
    """)

print("""
  </div>
</div>
<script>
  const sidebar = document.getElementById('sidebar');
  const toggleBtn = document.getElementById('sidebarToggleBtn');
  toggleBtn.addEventListener('click', () => { sidebar.classList.toggle('show'); });
  function toggleSubMenu(id) {
    const submenu = document.getElementById(id);
    submenu.classList.toggle('d-none');
  }
  function createStarRating(id) {
    const starContainer = document.getElementById('starRating' + id);
    const ratingInput = document.getElementById('ratingInput' + id);

    for(let i = 1; i <= 5; i++) {
      const star = document.createElement('i');
      star.classList.add('bi', 'bi-star');
      star.style.fontSize = '1.5rem';
      star.style.cursor = 'pointer';
      star.dataset.value = i;
      star.addEventListener('mouseenter', () => {
        highlightStars(starContainer, i);
      });
      star.addEventListener('mouseleave', () => {
        highlightStars(starContainer, ratingInput.value);
      });
      star.addEventListener('click', () => {
        ratingInput.value = i;
        highlightStars(starContainer, i);
      });

      starContainer.appendChild(star);
    }

    highlightStars(starContainer, ratingInput.value);
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
    const review = document.getElementById('review' + id).value.trim();
    if(rating < 1 ) {
      alert('Please add star rating .');
      return false;
    }
    return true;
  }
  // Initialize star ratings on page load for all review modals
  window.addEventListener('DOMContentLoaded', () => {
    const modals = document.querySelectorAll('[id^="reviewModal"]');
    modals.forEach(modal => {
      const id = modal.id.replace('reviewModal', '');
      createStarRating(id);
    });
  });
</script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")

cur.close()
con.close()

# !C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Content-Type: text/html\r\n\r\n")
import datetime
import pymysql, cgi, cgitb

cgitb.enable()
today = datetime.date.today()

# Connect to DB
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

# Get form data
form = cgi.FieldStorage()
start_date = form.getvalue("start_date")
end_date = form.getvalue("end_date")
user_id = form.getvalue("user_id")
q = "SELECT * FROM users WHERE user_id=%s"
cur.execute(q, (user_id,))
res = cur.fetchall()
cur.execute("SELECT COUNT(*) FROM notifications WHERE user_id=%s AND status='unseen'", (user_id,))
notification_count = cur.fetchone()[0]

# HTML header
print("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Completed Requests</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">
  <style>
    .card-title { font-weight: bold; color: #198754; }
    .modal-header { background-color: #0d6efd; color: white; }
    .badge-completed { background-color: #198754; }
    body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .navbar-custom { background-color: azure; }
    .mainhead { font-weight: 500; }
    .sidebar { position: fixed; top: 74px; left: -250px; width: 250px; height: 100%; background-color: rgb(253, 248, 248); padding-top: 30px; transition: all 0.3s ease; z-index: 1000; }
    .sidebar.show { left: 0; }
    .sidebar .nav-link { color: #0b0b0b; padding: 15px 20px; }
    .sidebar .nav-link:hover, .sidebar .nav-link.active { background-color: #e2cccc; color: rgb(250, 4, 4); }
    .overlay { top: 0; left: 0; height: 100%; width: 100%; background-color: rgba(0, 0, 0, 0.5); z-index: 990; display: none; }
    .overlay.show { display: block; }
    .main-content { padding: 20px; margin-left: 0; margin-top: 90px; transition: margin-left 0.3s ease; }
    @media (min-width: 768px) { .sidebar { left: 0; } .main-content { margin-left: 250px; } .overlay { display: none !important; } #sidebarToggleBtn { display: none; } }
    .submenu { background-color: #f5f5f5; border-left: 2px solid #ccc; }
    .submenu .nav-link { padding-left: 30px; font-size: 0.95rem; }
    .profile-btn { background: linear-gradient(to right, #ff4500, #ff6347); color: white; border: none; border-radius: 25px; padding: 8px 18px; font-weight: 500; box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: all 0.3s ease; }
    .profile-btn:hover { background: #d62900; color: #fff; transform: scale(1.05); box-shadow: 0 6px 12px rgba(0,0,0,0.15); }
    .container { margin-top: 20px; margin-left: auto; margin-right: auto; max-width: 1200px; width: 95%; }.notification-btn {
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}
.bi-star-fill {
  color: gold !important;
}

  </style>
</head>
<body>
""")

# Navbar and Sidebar
for i in res:
    name = i[1]
    print(f"""
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
""")

print("""
<div class="main-content">
  <div class="container">
    <h2 class="mb-4 text-center text-success">Completed Requests</h2>
""")
q = """select * from service_requests where user_id=%s """ % (user_id)
cur.execute(q)
cur.execute(q)
res = cur.fetchall()
if res:
    print("""
     <table class="table table-striped table-hover align-middle">
      <thead class="table-success">
        <tr>
          <th>S.No</th>
          <th>Shop Name</th>
          <th>Shop Details</th>
          <th>Rating</th>
          <th>My Services</th>
        </tr>
      </thead>
      <tbody>
    """)
    for idx, i in enumerate(res, 1):
        req_id = i[1]
        shop_id = i[2]
        issue = i[3]
        booked_on = i[4]
        mech_id = i[6]
        service_charge = i[7]
        extra_charge = i[14]
        payment_status = i[19]
        total_charge = i[16]
        completed_date = i[13]

        # Fetch average rating
        stars_html = "&#9734;" * 5  # Default
        cur.execute("SELECT AVG(rating) FROM reviews WHERE shop_id=%s", (shop_id,))
        avg_rating_row = cur.fetchone()
        if avg_rating_row and avg_rating_row[0] is not None:
            avg_rating = round(avg_rating_row[0])
            stars_html = "&#9733;" * avg_rating + "&#9734;" * (5 - avg_rating)

        # Get shop details
        cur.execute("SELECT * FROM mechanicshops WHERE id=%s", (shop_id,))
        shop_data = cur.fetchone()
        if shop_data:
            shop_name = shop_data[10]
            shop_address = shop_data[11]
            shop_image = shop_data[12]
            shop_email = shop_data[17]
            shop_phone = shop_data[4]

        # Get payment details
        cur.execute("SELECT * FROM payments WHERE service_id=%s", (req_id,))
        payment = cur.fetchone()
        if payment:
            method = payment[5]
            date = payment[6]
        else:
            method = "N/A"
            date = "N/A"

        # Get mechanic name
        if mech_id:
            cur.execute("SELECT name FROM mechanics WHERE mech_id=%s", (mech_id,))
            mech = cur.fetchone()
            mech_name = mech[0] if mech else "Unknown"
        else:
            mech_name = "Unknown"

        # ✅ Now print HTML inside the loop
        print(f"""
        <tr>
          <td>{idx}</td>
          <td>{shop_name}</td>
          <td><button class="btn btn-primary btn-sm" data-bs-toggle="modal" data-bs-target="#{shop_id}"> View Details </button></td>
          <td>{stars_html}</td>
          <td><button class="btn btn-warning btn-sm" data-bs-toggle="modal" data-bs-target="#myserviceModal{shop_id}"> View services </button></td>
        </tr>
        <div class="modal fade" id="{shop_id}" tabindex="-1" aria-labelledby="{shop_id}Label" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h5 class="modal-title" id="{shop_id}Label">Shop Details</h5>
                      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                     <img src="./images/{shop_image}" alt="Shop Image" class="img-fluid rounded mb-3" style="max-height: 150px;">
                      <p><strong>Shop:</strong> {shop_name}</p>
                      <p><strong>Address:</strong> {shop_address}</p>
                      <p><strong>Phone:</strong> {shop_phone}</p>
                       <p><strong>Email:</strong> {shop_email}</p>
                    </div>
                    <div class="modal-footer">
                      <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="modal">Close</button>
                    </div>
                  </div>
                </div>
              </div>
               <div class="modal fade" id="myserviceModal{shop_id}" tabindex="-1" aria-labelledby="myserviceModal{shop_id}Label" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered modal-lg">
            <div class="modal-content">
              <div class="modal-header bg-success text-white">
                <h5 class="modal-title" id="myserviceModal{shop_id}Label">Service Summary</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">

                <table class="table table-bordered table-striped">
                  <thead class="table-light">
                    <tr>
                      <th>S.NO</th>
                      <th>Booked On</th>
                      <th>Issue</th>
                      <th>Assisted By</th>
                      <th>Bill Details</th>
                      <th>Rate shop</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>1</td>
                      <td>{booked_on}</td>
                      <td>{issue}</td>
                      <td>{mech_name}</td>
                      <td> <button class="btn btn-success btn-sm" data-bs-toggle="modal" data-bs-target="#paymentmodal{req_id}">View Bill </button></td>
                      <td> <button class="btn btn-warning btn-sm" data-bs-toggle="modal" data-bs-target="#reviewModal{req_id}">
                          Add Review
                        </button></td>
                    </tr>
                  </tbody>
                </table>

              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>
        <div class="modal fade" id="paymentmodal{req_id}" tabindex="-1" aria-labelledby="paymentmodal{req_id}Label" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="paymentmodal{req_id}Label">Payment Details</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <p><strong>Service Charge:</strong> ₹{service_charge}</p>
                <p><strong>Extra Charges:</strong> ₹{extra_charge}</p>
                <p><strong>Total:</strong> ₹{total_charge}</p>
                <p><strong>Payment Method:</strong> {method or 'N/A'}</p>
                <p><strong>Paid On:</strong>{date}</p>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>
        <div class="modal fade" id="reviewModal{req_id}" tabindex="-1" aria-labelledby="reviewModalLabel{req_id}" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <form method="post" action="submit_review.py" onsubmit="return validateReviewForm({req_id});">
                <div class="modal-header">
                  <h5 class="modal-title" id="reviewModalLabel{req_id}">Add Review for {shop_name}</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body text-center">
                  <img src="./images/{shop_image}" alt="Shop Image" class="img-fluid rounded mb-3" style="max-height: 150px;">
                  <h5>{shop_name}</h5>
                  <p>{shop_address}</p>

                  <label for="rating{req_id}" class="form-label">Your Rating:</label>
                  <div id="starRating{req_id}" class="mb-3"></div>
                  <input type="hidden" name="rating" id="ratingInput{req_id}" value="{stars_html or 0}" required>

                  <label for="review{req_id}" class="form-label">Your Review:</label>
                  <textarea class="form-control" name="review" id="review{req_id}" rows="3" placeholder="Write your review here..."></textarea>

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


        """)
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

print("""
  </div>
</div>
<script>
  const sidebar = document.getElementById('sidebar');
  const toggleBtn = document.getElementById('sidebarToggleBtn');
  toggleBtn.addEventListener('click', () => { sidebar.classList.toggle('show'); });
  function toggleSubMenu(id) {
    const submenu = document.getElementById(id);
    submenu.classList.toggle('d-none');
  }

  function createStarRating(id) {
    const starContainer = document.getElementById('starRating' + id);
    const ratingInput = document.getElementById('ratingInput' + id);

    if (!starContainer) return; // Exit if the container doesn't exist

    starContainer.innerHTML = '';

    for(let i = 1; i <= 5; i++) {
      const star = document.createElement('i');
      star.classList.add('bi', 'bi-star');
      star.style.fontSize = '1.5rem';
      star.style.cursor = 'pointer';
      star.dataset.value = i;
      star.addEventListener('mouseenter', () => {
        highlightStars(starContainer, i);
      });
      star.addEventListener('mouseleave', () => {
        highlightStars(starContainer, ratingInput.value);
      });
      star.addEventListener('click', () => {
        ratingInput.value = i;
        highlightStars(starContainer, i);
      });

      starContainer.appendChild(star);
    }

    highlightStars(starContainer, ratingInput.value);
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
    const review = document.querySelector('#reviewModal' + id + ' textarea[name="review"]').value.trim();
    if(rating < 1) {
      alert('Please provide  star rating .');
      return false;
    }
    return true;
  }

  window.addEventListener('DOMContentLoaded', () => {
    const modals = document.querySelectorAll('[id^="reviewModal"]');
    modals.forEach(modal => {
      modal.addEventListener('shown.bs.modal', function () {
        const id = modal.id.replace('reviewModal', '');
        createStarRating(id);
      });
    });
  });
</script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")

cur.close()
con.close()



#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Content-Type: text/html\r\n\r\n")
import datetime
import pymysql, cgi, cgitb

cgitb.enable()
today = datetime.date.today()

# Connect to DB
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

# Get form data
form = cgi.FieldStorage()
start_date = form.getvalue("start_date")
end_date = form.getvalue("end_date")
user_id = form.getvalue("user_id")
q = "SELECT * FROM users WHERE user_id=%s"
cur.execute(q, (user_id,))
res = cur.fetchall()
cur.execute("SELECT COUNT(*) FROM notifications WHERE user_id=%s AND status='unseen'", (user_id,))
notification_count = cur.fetchone()[0]

# HTML header
print("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Completed Requests</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">
  <style>
    .card-title { font-weight: bold; color: #198754; }
    .modal-header { background-color: #0d6efd; color: white; }
    .badge-completed { background-color: #198754; }
    body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .navbar-custom { background-color: azure; }
    .mainhead { font-weight: 500; }
    .sidebar { position: fixed; top: 74px; left: -250px; width: 250px; height: 100%; background-color: rgb(253, 248, 248); padding-top: 30px; transition: all 0.3s ease; z-index: 1000; }
    .sidebar.show { left: 0; }
    .sidebar .nav-link { color: #0b0b0b; padding: 15px 20px; }
    .sidebar .nav-link:hover, .sidebar .nav-link.active { background-color: #e2cccc; color: rgb(250, 4, 4); }
    .overlay { top: 0; left: 0; height: 100%; width: 100%; background-color: rgba(0, 0, 0, 0.5); z-index: 990; display: none; }
    .overlay.show { display: block; }
    .main-content { padding: 20px; margin-left: 0; margin-top: 90px; transition: margin-left 0.3s ease; }
    @media (min-width: 768px) { .sidebar { left: 0; } .main-content { margin-left: 250px; } .overlay { display: none !important; } #sidebarToggleBtn { display: none; } }
    .submenu { background-color: #f5f5f5; border-left: 2px solid #ccc; }
    .submenu .nav-link { padding-left: 30px; font-size: 0.95rem; }
    .profile-btn { background: linear-gradient(to right, #ff4500, #ff6347); color: white; border: none; border-radius: 25px; padding: 8px 18px; font-weight: 500; box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: all 0.3s ease; }
    .profile-btn:hover { background: #d62900; color: #fff; transform: scale(1.05); box-shadow: 0 6px 12px rgba(0,0,0,0.15); }
    .container { margin-top: 20px; margin-left: auto; margin-right: auto; max-width: 1200px; width: 95%; }.notification-btn {
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}
.bi-star-fill {
  color: gold !important;
}

  </style>
</head>
<body>
""")

# Navbar and Sidebar
for i in res:
    name = i[1]
    print(f"""
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
""")

print("""
<div class="main-content">
  <div class="container">
    <h2 class="mb-4 text-center text-success">Completed Requests</h2>
""")
q = """select * from service_requests where user_id=%s """%(user_id)
cur.execute(q)
res = cur.fetchall()
if res is not None:
    for i in res:
        req_id = i[1]
        shop_id = i[2]
        issue = i[3]
        booked_on = i[4]
        mech_id = i[6]
        service_charge = i[7]
        extra_charge = i[14]
        payment_status = i[19]
        total_charge = i[16]
        completed_date = i[13]

    print("""
     <table class="table table-striped table-hover align-middle">
      <thead class="table-success">
        <tr>
          <th>S.No</th>
          <th>Shop Name</th>
          <th>Shop Details</th>
          <th>Rating</th>
          <th>My Services</th>
        </tr>
      </thead>
      <tbody>
    """)
    stars_html = "&#9734;" * 5  # Default empty rating
    n = "SELECT AVG(rating) FROM reviews WHERE shop_id=%s"
    cur.execute(n, (shop_id,))
    avg_rating_row = cur.fetchone()

    if avg_rating_row and avg_rating_row[0] is not None:
        avg_rating = round(avg_rating_row[0])
        stars_html = "&#9733;" * avg_rating + "&#9734;" * (5 - avg_rating)
    z = """ select * from mechanicshops where id=%s """%(shop_id)
    cur.execute(z)
    r = cur.fetchall()
    for idx, x in enumerate(r, 1):
        shop_name = x[10]
        shop_address = x[11]
        shop_image = x[12]
        shop_email = x[17]
        shop_phone = x[4]
        print(f"""
        <tr>
        <td>{idx}</td>
        <td>{shop_name}</td>
        <td><button class="btn btn-primary btn-sm" data-bs-toggle="modal" data-bs-target="#{shop_id}"> View Details </button></td>
        <td>{stars_html}</td>
         <td><button class="btn btn-warning btn-sm" data-bs-toggle="modal" data-bs-target="#myserviceModal{shop_id}"> View services </button></td>
         </tr>
        """)
        print("""
            </tbody>
            </table>
            """)
        print(f"""
              <div class="modal fade" id="{shop_id}" tabindex="-1" aria-labelledby="{shop_id}Label" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h5 class="modal-title" id="{shop_id}Label">Shop Details</h5>
                      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                     <img src="./images/{shop_image}" alt="Shop Image" class="img-fluid rounded mb-3" style="max-height: 150px;">
                      <p><strong>Shop:</strong> {shop_name}</p>
                      <p><strong>Address:</strong> {shop_address}</p>
                      <p><strong>Phone:</strong> {shop_phone}</p>
                       <p><strong>Email:</strong> {shop_email}</p>
                    </div>
                    <div class="modal-footer">
                      <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="modal">Close</button>
                    </div>
                  </div>
                </div>
              </div>
              """)
        z = """select * from payments where service_id=%s"""%(req_id)
        cur.execute(z)
        a = cur.fetchall()
        if a:
            for i in a:
                method = i[5]
                date = i[6]
        else:
            method = "N/A"
            date = "N/A"
        if mech_id:
            s = "SELECT name FROM mechanics WHERE mech_id=%s"
            cur.execute(s, (mech_id,))
            mech = cur.fetchone()
            if mech is not None:
                mech_name = mech[0]
            else:
                mech_name = "Unknown"
        else:
            mech_name = "Unknown"

        print(f"""
        <div class="modal fade" id="myserviceModal{shop_id}" tabindex="-1" aria-labelledby="myserviceModal{shop_id}Label" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered modal-lg">
            <div class="modal-content">
              <div class="modal-header bg-success text-white">
                <h5 class="modal-title" id="myserviceModal{shop_id}Label">Service Summary</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">

                <table class="table table-bordered table-striped">
                  <thead class="table-light">
                    <tr>
                      <th>S.NO</th>
                      <th>Booked On</th>
                      <th>Issue</th>
                      <th>Assisted By</th>
                      <th>Bill Details</th>
                      <th>Rate shop</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>1</td>
                      <td>{booked_on}</td>
                      <td>{issue}</td>
                      <td>{mech_name}</td>
                      <td> <button class="btn btn-success btn-sm" data-bs-toggle="modal" data-bs-target="#paymentmodal{req_id}">View Bill </button></td>
                      <td> <button class="btn btn-warning btn-sm" data-bs-toggle="modal" data-bs-target="#reviewModal{req_id}">
                          Add Review
                        </button></td>
                    </tr>
                  </tbody>
                </table>

              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>
        <div class="modal fade" id="paymentmodal{req_id}" tabindex="-1" aria-labelledby="paymentmodal{req_id}Label" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="paymentmodal{req_id}Label">Payment Details</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <p><strong>Service Charge:</strong> ₹{service_charge}</p>
                <p><strong>Extra Charges:</strong> ₹{extra_charge}</p>
                <p><strong>Total:</strong> ₹{total_charge}</p>
                <p><strong>Payment Method:</strong> {method or 'N/A'}</p>
                <p><strong>Paid On:</strong>{date}</p>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>
        <div class="modal fade" id="reviewModal{req_id}" tabindex="-1" aria-labelledby="reviewModalLabel{req_id}" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <form method="post" action="submit_review.py" onsubmit="return validateReviewForm({req_id});">
                <div class="modal-header">
                  <h5 class="modal-title" id="reviewModalLabel{req_id}">Add Review for {shop_name}</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body text-center">
                  <img src="./images/{shop_image}" alt="Shop Image" class="img-fluid rounded mb-3" style="max-height: 150px;">
                  <h5>{shop_name}</h5>
                  <p>{shop_address}</p>

                  <label for="rating{req_id}" class="form-label">Your Rating:</label>
                  <div id="starRating{req_id}" class="mb-3"></div>
                  <input type="hidden" name="rating" id="ratingInput{req_id}" value="{stars_html or 0}" required>

                  <label for="review{req_id}" class="form-label">Your Review:</label>
                  <textarea class="form-control" name="review" id="review{req_id}" rows="3" placeholder="Write your review here..."></textarea>

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
        """)


else:
    print("""
    <div class="alert alert-info text-center" role="alert">
      No completed requests found.
    </div>
    """)

print("""
  </div>
</div>
<script>
  const sidebar = document.getElementById('sidebar');
  const toggleBtn = document.getElementById('sidebarToggleBtn');
  toggleBtn.addEventListener('click', () => { sidebar.classList.toggle('show'); });
  function toggleSubMenu(id) {
    const submenu = document.getElementById(id);
    submenu.classList.toggle('d-none');
  }

  function createStarRating(id) {
    const starContainer = document.getElementById('starRating' + id);
    const ratingInput = document.getElementById('ratingInput' + id);

    if (!starContainer) return; // Exit if the container doesn't exist

    starContainer.innerHTML = '';

    for(let i = 1; i <= 5; i++) {
      const star = document.createElement('i');
      star.classList.add('bi', 'bi-star');
      star.style.fontSize = '1.5rem';
      star.style.cursor = 'pointer';
      star.dataset.value = i;
      star.addEventListener('mouseenter', () => {
        highlightStars(starContainer, i);
      });
      star.addEventListener('mouseleave', () => {
        highlightStars(starContainer, ratingInput.value);
      });
      star.addEventListener('click', () => {
        ratingInput.value = i;
        highlightStars(starContainer, i);
      });

      starContainer.appendChild(star);
    }

    highlightStars(starContainer, ratingInput.value);
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
    const review = document.querySelector('#reviewModal' + id + ' textarea[name="review"]').value.trim();
    if(rating < 1) {
      alert('Please provide  star rating .');
      return false;
    }
    return true;
  }

  window.addEventListener('DOMContentLoaded', () => {
    const modals = document.querySelectorAll('[id^="reviewModal"]');
    modals.forEach(modal => {
      modal.addEventListener('shown.bs.modal', function () {
        const id = modal.id.replace('reviewModal', '');
        createStarRating(id);
      });
    });
  });
</script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")

cur.close()
con.close()


# Send email
try:
    sender_email = "sruthisudhakaran2005@gmail.com"
    sender_password = "trng sjeu embt htce"
    receiver_email = email

    subject = "Your Service Request Has Been Rejected"
    body = f"""
Dear Customer,

We regret to inform you that your service request (Request ID: {request_id}) has been rejected.

You may submit a new request if needed, or contact support for more details.

Thank you for using RoadNova.

Best regards,
RoadNova Team
"""

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

except Exception as e:
    print(f"<p>Email sending failed: {e}</p>")

    # !C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe

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
           <th>Mechanics-Completed Requests</th>
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
           <td> <button class="btn btn-sm btn-outline-warning" data-bs-toggle="modal" data-bs-target="#completedModal{shop_id}">
              Total: {completed_count}-View Details
             </button>
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
               <img src="./images/{shop_image}" alt="shop image">
                <img src="./images/{owner_image}" alt="shop image" style="height:180px;margin-left:200px;">
                <div class="items1" style="margin-top:30px;">
                 <p><b>Owner Name:</b> {shop_name_safe}</p>
                 <p><b>Address:</b> {saddr_safe}</p>
                 </div>
                <div class="items2" style="margin-left:500px;margin-top:-70px;">
                 <p><b>Owner Name:</b> {owner_name_safe}</p>
                 <p><b>Email:</b> {semail_safe}</p>
                 <p><b>Phone:</b> {sphone_safe}</p>
                 <p><b>Address:</b> {saddr_safe}</p>
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

        mechanic_tasks = {mech_id: {'name': name, 'requests': []} for (mech_id, name) in
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