#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
form = cgi.FieldStorage()

# --- START OF FIX: Handle user_id correctly and fetch data ONCE ---
user_id_raw = form.getvalue("user_id")
if isinstance(user_id_raw, list):
    user_id = user_id_raw[0]
else:
    user_id = user_id_raw

if not user_id:
    print("<h1>Error: User ID is missing.</h1>")
    sys.exit()

cur.execute("SELECT COUNT(*) FROM notifications WHERE user_id=%s AND status='unseen'", (user_id,))
notification_count = cur.fetchone()[0]

q = "SELECT * FROM users WHERE user_id=%s"
cur.execute(q, (user_id,))
res = cur.fetchone()  # fetchone() is more appropriate for a unique user_id
if res:
    name = res[1]
else:
    print("<h1>Error: User not found.</h1>")
    sys.exit()

# --- Print the main HTML structure only ONCE before the loops ---
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>User Dashboard</title>

  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"/>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet"/>

  <style>
    body {{
      overflow-x: hidden;
    }}

    .navbar-custom {{
      background-color: azure;
    }}
    .mainhead {{
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      font-weight: 500;
    }}

    .section1 {{
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
    }}

    .section1::before {{
      content: "";
      position: absolute;
      inset: 0;
      background: inherit;
      filter: blur(4px);
      z-index: 1;
    }}

    .section1 .data {{
      position: relative;
      z-index: 2;
      padding: 20px;
    }}

    .help:hover {{
      color: rgb(255, 106, 0);
    }}

    .sidebar {{
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
    }}

    .sidebar.show {{
      left: 0;
    }}

    .sidebar .nav-link {{
      color: #0b0b0b;
      padding: 15px 20px;
    }}

    .sidebar .nav-link:hover,
    .sidebar .nav-link.active {{
      background-color: #e2cccc;
      color: rgb(250, 4, 4);
    }}

    .overlay {{
      top: 0;
      left: 0;
      height: 100%;
      width: 100%;
      background-color: rgba(0, 0, 0, 0.5);
      z-index: 990;
      display: none;
    }}

    .overlay.show {{
      display: block;
    }}

    .main-content {{
      padding: 20px;
      margin-left: 0;
      margin-top: 90px;
      transition: margin-left 0.3s ease;
    }}

    @media (min-width: 768px) {{
      .sidebar {{
        left: 0;
      }}
      .main-content {{
        margin-left: 250px;
      }}
      .overlay {{
        display: none !important;
      }}
      #sidebarToggleBtn {{
        display: none;
      }}
    }}

    .content-section {{
      display: none;
    }}

    .content-section.active {{
      display: block;
    }}

    a {{
      text-decoration: none;
      color: black;
    }}

    a:hover {{
      color: rgb(19, 19, 73);
    }}

    .search-container {{
      z-index: 1050;
      position: relative;
      margin-top: 20px;
    }}

    .rounded-pill {{
      width: 300px;
      padding: 10px 20px;
      border: 2px solid #efbad0;
      border-radius: 50px;
      outline: none;
      box-shadow: 0 4px 10px rgba(239, 8, 201, 0.2);
      font-size: 16px;
    }}

    .search-button {{
      background-color: #f8fbff;
      border: none;
      border-radius: 50%;
      margin-left: -32px;
      cursor: pointer;
    }}

    .search-button:hover {{
      background-color: #f5f7f8;
      transform: scale(1.05);
    }}

    .card-text {{
      color: black;
    }}
    .submenu {{
      background-color: #f5f5f5;
      border-left: 2px solid #ccc;
    }}

    .submenu .nav-link {{
      padding-left: 30px;
      font-size: 0.95rem;
    }}
    .profile-btn {{
      background: linear-gradient(to right, #ff4500, #ff6347);
      color: white;
      border: none;
      border-radius: 25px;
      padding: 8px 18px;
      font-weight: 500;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
      transition: all 0.3s ease;
    }}

    .profile-btn:hover {{
      background: #d62900;
      color: #fff;
      transform: scale(1.05);
      box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }}
    .notification-btn {{
      position: relative;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      padding: 0;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
  </style>
</head>
<body>

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

     <a href="user_profile.py?user_id={user_id}">
       <button class="btn profile-btn">
         <i class="bi bi-person-circle"></i> Profile
       </button>
     </a>
   </div>
  </div>
</nav>

<div class="sidebar" id="sidebar" style="box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
  <ul class="nav flex-column">
    <li class="nav-item">
      <a href="#" class="nav-link active" onclick="showSection('section-home')">Home</a>
    </li>

    <li class="nav-item">
      <a href="#" class="nav-link" onclick="toggleSubMenu('bookingSubMenu')">Booking <i class="bi bi-caret-down-fill"></i></a>
      <ul id="bookingSubMenu" class="nav flex-column ms-3 submenu d-none">
        <li><a href="approved_booking.py?user_id={user_id}" class="nav-link" >On Going</a></li>
        <li><a href="completed_booking.py?user_id={user_id}" class="nav-link" >Completed</a></li>
        <li><a href="cancelled_booking.py?user_id={user_id}" class="nav-link" >Cancelled</a></li>
        <li><a href="rejected_booking.py?user_id={user_id}" class="nav-link" >Rejected</a></li>
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

<div class="overlay" id="overlay"></div>

<div class="main-content">
  <div id="section-home" class="content-section active">
    <section class="section1">
      <div class="data">
        <h2>Welcome {name}</h2>
        <h2>How Can We Help Today? <a href="#" class="help">Get Help Now</a></h2>
        <div class="search-container mt-4">
          <form method="post" name="form" class="d-flex justify-content-center">
            <input type="hidden" name="user_id" value="{user_id}">
            <input type="text" name="sname" placeholder="Search using location" class="rounded-pill">
            <button type="submit" class="search-button" name="search">
              <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"/>
              </svg>
            </button>
          </form>
        </div>
      </div>
    </section>
""")

# --- START OF FIX: This logic block now correctly handles the search results ---
location = form.getvalue("sname")
shops = []
if location:
    query = "SELECT * FROM mechanicshops WHERE shop_address LIKE %s AND status='Approved'"
    cur.execute(query, ("%" + location + "%",))
    shops = cur.fetchall()
    if shops:
        for shop in shops:
            shop_id = shop[0]
            shop_name = shop[10]
            shop_address = shop[11]
            shop_contact = shop[4]
            shop_image = shop[12]
            shop_email = shop[17]
            status = shop[19]

            cur.execute("SELECT rating, review_text FROM reviews WHERE shop_id=%s ORDER BY created_at DESC", (shop_id,))
            review_data = cur.fetchone()

            if review_data:
                rating, review = review_data
                stars_html = "★" * int(rating) + "☆" * (5 - int(rating))
                review_html = f'<p class="card-text">{review}</p>'
            else:
                stars_html = "☆" * 5
                review_html = '<p class="text-muted mb-1">No reviews yet</p>'

            print(f"""
            <div class="card mb-3 p-3 shadow-sm" style="max-width: 700px; margin: 20px auto;">
              <div class="row g-0 align-items-center">
                <div class="col-md-4">
                  <img src="/roadassist/images/{shop_image}" class="img-fluid rounded" alt="Shop Image" style="height: 150px; object-fit: cover;">
                </div>
                <div class="col-md-8">
                  <div class="card-body">
                    <h5 class="card-title text-primary">{shop_name}</h5>
                    <h6 class="text-warning">{stars_html}</h6>
                    <p class="card-text mb-1"><strong>Address:</strong> {shop_address}</p>
                    <p class="card-text mb-1" style="color:orange"><strong>Shop is currently <u>{status}</u></strong></p>
                    <div class="mb-2">
                      <a href="https://www.google.com/maps/search/?api=1&query={shop_address.replace(' ', '+')}" target="_blank" class="btn btn-outline-primary btn-sm">
                        <i class="bi bi-geo-alt-fill"></i> View on Map
                      </a>
                    </div>
                    <p class="card-text mb-3"><strong>Available services:</strong>
                     <button type="button" class="btn btn-info" data-bs-toggle="modal" data-bs-target="#servicesModal{shop_id}">
                      View Services
                    </button>
                    </p>
                    <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#serviceModal{shop_id}">
                      <i class="bi bi-tools"></i> Request Service
                    </button>
                  </div>
                </div>
              </div>
            </div>
            """)

            cur.execute("SELECT service_name, price FROM services WHERE shop_id=%s", (shop_id,))
            services = cur.fetchall()

            service_list_html = "<ul class='list-group'>"
            for svc in services:
                service_name, price = svc
                service_list_html += f"""
                <li class="list-group-item d-flex justify-content-between align-items-center">
                  {service_name}
                  <span class="badge bg-primary rounded-pill">₹{price}</span>
                </li>
                """
            service_list_html += "</ul>"

            print(f"""
            <div class="modal fade" id="servicesModal{shop_id}" tabindex="-1" aria-labelledby="servicesModalLabel{shop_id}" aria-hidden="true">
              <div class="modal-dialog modal-xl modal-dialog-centered">
                <div class="modal-content">
                  <div class="modal-header bg-info text-white">
                    <h5 class="modal-title" id="servicesModalLabel{shop_id}">Services at {shop_name}</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <div class="container-fluid">
                      <div class="row">
                         {service_list_html if services else '<p class="text-muted">No services available for this shop.</p>'}
                      </div>
                    </div>
                  </div>
                  <div class="modal-footer">
                    <button class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                  </div>
                </div>
              </div>
            </div>
            """)

            cur.execute("SELECT service_name FROM services WHERE shop_id=%s", (shop_id,))
            service_options = cur.fetchall()
            service_options_html = ""
            for s in service_options:
                service_options_html += f"<option value='{s[0]}'>{s[0]}</option>"

            print(f"""
            <div class="modal fade" id="serviceModal{shop_id}" tabindex="-1" aria-labelledby="serviceModalLabel{shop_id}" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <form method="post" action="request_service.py" onsubmit="return service(event)">
                    <div class="modal-header">
                      <h5 class="modal-title" id="serviceModalLabel{shop_id}" style="color:black;">Request Service from {shop_name}</h5>
                      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                      <img src="./images/{shop_image}" width="250px" height="100px" alt="shop image" style="margin-left:100px">
                      <p style="color:black;"><strong>Address:</strong> {shop_address}</p>
                      <p style="color:black;"><strong>Contact:</strong> {shop_contact}</p>
    
                      <input type="hidden" name="user_id" value="{user_id}">
                      <input type="hidden" name="shop_id" value="{shop_id}">
                       <input type="hidden" name="shop_name" value="{shop_name}">
                       <input type="hidden" name="user_name" value="{name}">
                       <input type="hidden" name="email" value="{shop_email}">
                      <div class="mb-3">
                        <label for="service_name{shop_id}" class="form-label" style="color:black;">Select Service</label>
                        <select class="form-select" id="service_name{shop_id}" name="service_name" required>
                          <option value="">-- Choose a service --</option>
                          {service_options_html if service_options else '<option disabled>No services available</option>'}
                          <option value="other">other</option>
                        </select>
                      </div>
    
                      <div class="mb-3">
                        <label for="vehicle_type{shop_id}" class="form-label" style="color:black;">Vehicle Type</label>
                        <select class="form-select" id="vehicle_type{shop_id}" name="vehicle_type" required>
                          <option value="">-- Choose type of vehicle --</option>
                          <option value="Two Wheeler">Two-Wheeler</option>
                          <option value="Three Wheeler">Three-Wheeler</option>
                          <option value="Four Wheeler">Four-Wheeler</option>
                          <option value="Multi Wheeler">Multi-Wheeler</option>
                        </select>
                      </div>
    
                      <div class="mb-3">
                        <label for="vehicle_brand{shop_id}" class="form-label" style="color:black;">Brand</label>
                        <input type="text" class="form-control" id="vehicle_brand{shop_id}" name="vehicle_brand" required>
                      </div>
    
                      <div class="mb-3">
                      <label for="reg_number{shop_id}" class="form-label" style="color:black;">Registration Number</label>
                      <input type="text" class="form-control" id="registration_number_{shop_id}" name="registration_number" required>
                    </div>
    
                      <div class="mb-3">
                        <label for="user_location{shop_id}" class="form-label" style="color:black;">Your Current Location</label>
                        <input type="text" class="form-control" id="user_location{shop_id}" name="user_location" placeholder="Enter your current location" required>
                      </div>
    
                    </div>
                    <div class="modal-footer">
                      <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                      <button type="submit" class="btn btn-primary">Submit Request</button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
            """)
    else:
        print("""
        <div class="alert alert-warning text-center mt-4" role="alert">
            No mechanic shops found for your search.
        </div>
        """)
else:
    print(f"""
    <div class="container text-center position-relative my-5" style="max-width: 600px;">
      <img src="./images/car2.png" alt="car" class="img-fluid shadow-sm" style="width: 100%; height: auto;">

      <div style="
        position: absolute;
        top: 5%;
        left: 40%;
        transform: translate(-50%, -50%);
        padding: 1rem 2rem;
        border-radius: 0.5rem;
        font-size: 1.25rem;
        font-weight: 600;
        max-width: 90%;
        ">
        "Drive your dreams — the road awaits."
      </div>
    </div>
    """)

# --- END OF FIX: The closing HTML and scripts are printed once at the end ---
print("""
  </div>  
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
<script>
  const sidebar = document.getElementById('sidebar');
  const overlay = document.getElementById('overlay');
  const toggleBtn = document.getElementById('sidebarToggleBtn');

  toggleBtn.addEventListener('click', () => {
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

  function showSection(id) {
    document.querySelectorAll('.content-section').forEach(section => {
      section.classList.remove('active');
    });
    document.getElementById(id).classList.add('active');

    document.querySelectorAll('.sidebar .nav-link').forEach(link => {
      link.classList.remove('active');
    });
    event.target.classList.add('active');

    if (window.innerWidth < 768) {
      sidebar.classList.remove('show');
      overlay.classList.remove('show');
    }
  }
 // In your HTML script tag
function service(event) {
  event.preventDefault();

  // Get the form element that triggered the event
  const form = event.target;
  
  // Find the hidden input for the shop_id within this specific form
  const shopIdInput = form.querySelector('input[name="shop_id"]');
  const shopId = shopIdInput ? shopIdInput.value : '';

  // Get the registration number input using its now-unique ID
  const number = document.getElementById("registration_number_" + shopId).value;

  const pattern = /^[A-Z]{2}\d{2}[A-Z]{1,2}\d{1,4}$/;

  if (number === "") {
    alert("Please enter a vehicle registration number.");
    return false;
  }
  if (!pattern.test(number)) {
    alert("Invalid vehicle registration number. Please enter a Register Number");
    return false;
  }
  
  form.submit();
  return true;
}
</script>

</body>
</html>
""")