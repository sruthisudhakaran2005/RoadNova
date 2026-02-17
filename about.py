#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
print("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>About Us | RoadNova</title>

 
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <style>
    * {
      box-sizing: border-box;
      margin: 0; padding: 0;
    }

    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      line-height: 1.6;
      color: #333;
      background: #f9f9f9;
     padding-top: 70px;
    }

    /* Navbar height adjustment */
.navbar {
  background-color: rgb(237, 238, 240);
  padding-top: 0.3rem;
  padding-bottom: 0.3rem;
}

/* Logo smaller */
.logo {
  border-radius: 50%;
  height: 50px;
  width: 50px;
}

/* Main heading smaller */
.mainhead {
  font-size: 1rem;
  margin-left: 10px;
  color: rgb(14, 3, 0);
  font-weight: bold;
}

 .form-container{
      width:400px;
      margin-left: 50px;

    }

@media (max-width: 768px) {
  body {
    padding-top: 90px;
}
}

    .container {
      max-width: 1100px;
      margin: auto;
      padding: 20px;
    }

    h1, h2 {
      color: #007bff;
      margin-bottom: 15px;
    }

    p {
      margin-bottom: 15px;
      font-size: 1.1rem;
    }

    .about-section {
      display: flex;
      flex-wrap: wrap;
      gap: 40px;
      align-items: center;
      margin-top: 40px;
    }

    .about-text {
      flex: 1 1 500px;
    }

    .about-text p {
      text-align: justify;
    }

    .about-image {
      flex: 1 1 400px;
      overflow: hidden;
      border-radius: 10px;
      box-shadow: 0 6px 15px rgba(0,0,0,0.1);
    }

    .about-image img {
      width: 100%;
      height: auto;
      display: block;
      transition: transform 0.6s ease;
    }

    .about-image:hover img {
      transform: scale(1.05);
    }

    .fade-in {
      opacity: 0;
      transform: translateY(30px);
      transition: opacity 1s ease-out, transform 1s ease-out;
    }

    .fade-in.visible {
      opacity: 1;
      transform: translateY(0);
    }

    @media (max-width: 900px) {
      .about-section {
        flex-direction: column;
      }
      .about-image, .about-text {
        flex: 1 1 100%;
      }
    }

    /* ✅ Navbar styling (same as home page) */
    .navbar {
      background-color: rgb(237, 238, 240);
    }

   

  
    .nav-link,
    .dropdown-toggle {
      color: rgb(255, 57, 8) !important;
      font-weight: 500;
      font-size: large;
    }

    .nav-link:hover,
    .dropdown-item:hover {
      color: rgb(3, 20, 40) !important;
    }

    .dropdown-menu {
      background-color: rgb(253, 254, 255);
      border: none;
    }

    .dropdown-item {
      font-size: large;
      color: darkslateblue;
    }

    @media (max-width: 768px) {
      .mainhead {
        margin-left: 0;
        margin-top: 10px;
        text-align: center;
      }

      .navbar-brand {
        display: flex;
        align-items: center;
      }
    }

    footer {
      background-color: #333;
      color: #fff;
      padding: 40px 20px;
      margin-top: 60px;
      font-size: 0.95rem;
    }

    .footer-container {
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      max-width: 1100px;
      margin: auto;
    }

    .footer-column {
      flex: 1 1 250px;
      margin: 20px 0;
    }

    .footer-column h3 {
      margin-bottom: 15px;
      color: #f9a825;
    }

    .footer-column a {
      display: block;
      color: #ccc;
      text-decoration: none;
      margin-bottom: 10px;
      transition: color 0.3s ease;
    }

    .footer-column a:hover {
      color: #f9a825;
    }

    .footer-bottom {
      text-align: center;
      margin-top: 30px;
      border-top: 1px solid #555;
      padding-top: 20px;
      font-size: 0.85rem;
      color: #aaa;
    }

    @media (max-width: 768px) {
      .footer-container {
        flex-direction: column;
        align-items: center;
        text-align: center;
      }
      .footer-column {
        margin-bottom: 30px;
      }
    }
    .btn{
    width:180px;
   
   }
   .important{
  margin-left:150px;
   color:burlywood; 
}
.imlink{
  color:burlywood
}
.imlink:hover{
  color:#c62828;
  
}
.important:hover{
  color:#c62828;

}
.btn-close{
  margin-left: 400px;
  margin-top: 30px;
}

@media (max-width: 768px) {
  .navbar-toggler {
    border: none !important;
    outline: none !important;
    box-shadow: none !important;
  }
}
@media (max-width: 768px) {
  .offcanvas-end {
    width: 200px !important;
  }
}




.modal-header {
  border: none !important;
}
#userLoginModal{
  border-radius: 30px;
}
/* General modal appearance */
.modal-content {
  border-radius: 20px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
  animation: fadeSlideIn 0.5s ease;
}

/* Modal entry animation */
@keyframes fadeSlideIn {
  0% {
    opacity: 0;
    transform: translateY(-30px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Stylish modal headers */
.modal-header {
  background: linear-gradient(to right, #007bff, #00c6ff);
  color: white;
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  justify-content: center;
  text-align: center;
  border-bottom: none;
  padding: 30px 20px;
}

.modal-header h5 {
  font-size: 1.5rem;
  font-weight: 600;
}

.modal-body {
  padding: 30px;
}

/* Input fields styling */
.modal .form-control {
  border-radius: 10px;
  border: 1px solid #ccc;
  padding: 12px;
  margin-bottom: 15px;
  font-size: 1rem;
}

/* Button styling */
.modal .btn-primary {
  background: linear-gradient(to right, #ff416c, #ff4b2b);
  border: none;
  border-radius: 10px;
  font-weight: bold;
  padding: 12px;
  width: 100%;
  transition: all 0.3s ease;
}

.modal .btn-primary:hover {
  background: linear-gradient(to right, #ff4b2b, #ff416c);
}

/* Cancel button */
.modal .btn-danger {
  border-radius: 10px;
  width: 100%;
  padding: 12px;
}

/* Forgot password link */
.important a {
  font-size: 0.9rem;
  text-decoration: underline;
  display: block;
  text-align: right;
  margin-top: -10px;
}
.attractive-h1 {
      font-size: 2.8rem;
      font-weight: 700;
      text-align: center;
      color: #007bff; /* Primary brand color */
      text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.15); /* Subtle shadow for depth */
      margin-top: 20px;
      margin-bottom: 40px;
      letter-spacing: 2px;
      position: relative;
    }

    .attractive-h1::after {
      content: '';
      display: block;
      width: 100px;
      height: 4px;
      background: linear-gradient(to right, #007bff, #00c6ff);
      margin: 10px auto 0;
      border-radius: 2px;
    }

  </style>
</head>
<body>

<!-- ✅ Navbar -->
<nav class="navbar navbar-expand-lg navbar-light fixed-top">
  <div class="container-fluid">
    <a class="navbar-brand d-flex align-items-center" href="#">
       <i class="fas fa-car-crash me-2"></i>
      <span class="mainhead ms-2">RoadNova</span>
    </a>

    <button class="navbar-toggler d-lg-none" type="button" data-bs-toggle="offcanvas" data-bs-target="#mobileMenu">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse d-none d-lg-flex justify-content-end" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item"><a class="nav-link" href="home.py">Home</a></li>
        <li class="nav-item"><a class="nav-link" href="#service">Services</a></li>
        <li class="nav-item"><a class="nav-link" href="about.py">About</a></li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="loginDropdown" role="button" data-bs-toggle="dropdown">Login</a>
          <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#" data-bs-toggle="modal" data-bs-target="#userLoginModal">User</a></li>
          <li><a class="dropdown-item" href="#" data-bs-toggle="modal" data-bs-target="#mechanicLoginModal">Mechanic</a></li>
          <li><a class="dropdown-item" href="#" data-bs-toggle="modal" data-bs-target="#adminLoginModal">Admin</a></li>
        </ul>

        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="registerDropdown" role="button" data-bs-toggle="dropdown">Register</a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="user_reg.py">User</a></li>
            <li><a class="dropdown-item" href="mechreg.py">Mechanic</a></li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link" href="#contact">Contact</a></li>
      </ul>
    </div>

    <!-- Mobile offcanvas menu -->
    <div class="offcanvas offcanvas-end d-lg-none" tabindex="-1" id="mobileMenu">
      <div class="offcanvas-header">
        <h5 class="offcanvas-title"> Links</h5>
        <button type="button" class="btn-close" data-bs-dismiss="offcanvas"></button>
      </div>
      <div class="offcanvas-body">
        <ul class="navbar-nav">
          <li class="nav-item"><a class="nav-link" href="home.py">Home</a></li>
          <li class="nav-item"><a class="nav-link" href="#service">Services</a></li>
          <li class="nav-item"><a class="nav-link" href="about.py">About</a></li>
           <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="loginDropdown" role="button" data-bs-toggle="dropdown">Login</a>
            <ul class="dropdown-menu" aria-labelledby="loginDropdown">
              <li><a class="dropdown-item" href="#" data-bs-toggle="modal" data-bs-target="#userLoginModal">User</a></li>
              <li><a class="dropdown-item" href="#" data-bs-toggle="modal" data-bs-target="#mechanicLoginModal">Mechanic</a></li>
              <li><a class="dropdown-item" href="#" data-bs-toggle="modal" data-bs-target="#adminLoginModal">Admin</a></li>
            </ul>
          </li>

          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown">Register</a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="user_reg.py">User</a></li>
              <li><a class="dropdown-item" href="mechreg.py">Mechanic</a></li>
            </ul>
          </li>
          <li class="nav-item"><a class="nav-link" href="#contact">Contact</a></li>
        </ul>
      </div>
    </div>
  </div>
</nav>

<!-- ✅ Page Content -->
<div class="container">
  <h1 class="attractive-h1 fade-in">About Us: RoadNova</h1>

  <div class="about-section">
    <div class="about-text fade-in">
      <h2>Who We Are</h2>
      <p>
        We are a dedicated roadside assistance service committed to providing swift, reliable help when your vehicle breaks down unexpectedly. Whether you’re stranded on a busy highway or a quiet neighborhood street, our expert technicians are just a call away to get you back on the road safely.
      </p>
      <p>
        With years of experience and a large network of trained professionals, we handle a wide range of vehicle emergencies, including flat tires, dead batteries, fuel delivery, lockouts, and more. Our goal is to minimize your downtime and stress by delivering timely solutions tailored to your needs.
      </p>
    </div>

    <div class="about-image fade-in">
      <img src="/roadassist/images/img9.webp" alt="Roadside Assistance Vehicle" />
    </div>
  </div>

  <div class="about-section">
    <div class="about-image fade-in">
      <img src="/roadassist/images/img8.jpg" alt="Technician Repairing Car" />
    </div>
    <div class="about-text fade-in"  id="service">
      <h2>Our Services</h2>
      <p>
        Our comprehensive breakdown assistance services include:
      </p>
      <ul>
        <li><strong>Tire Change & Repair:</strong> Quick replacement or repair of flat or damaged tires to get you rolling again.</li>
        <li><strong>Battery Jump Start & Replacement:</strong> Power up your vehicle’s battery or replace it on the spot.</li>
        <li><strong>Fuel Delivery:</strong> If you run out of fuel, we bring enough to get you to the nearest station.</li>
        <li><strong>Lockout Services:</strong> Locked your keys inside? We’ll safely get you back into your vehicle.</li>
        <li><strong>Minor Mechanical Repairs:</strong> On-the-spot fixes to keep your vehicle operational until you reach a garage.</li>
      </ul>
      <p>
        All our technicians are equipped with modern tools and follow strict safety protocols to ensure quality and security.
      </p>
    </div>
  </div>

  <div class="about-section">
    <div class="about-text fade-in">
      <h2>Why Choose Us?</h2>
      <p>
        Choosing the right roadside assistance provider can make all the difference during a stressful breakdown. Here’s why thousands trust us:
      </p>
      <ul>
        <li><strong>24/7 Availability:</strong> We’re ready whenever you need us, day or night.</li>
        <li><strong>Fast Response Times:</strong> Our strategically located service teams ensure prompt arrival.</li>
        <li><strong>Transparent Pricing:</strong> No hidden fees — you know the cost upfront.</li>
        <li><strong>Customer Satisfaction:</strong> We pride ourselves on friendly, professional service and real-time updates.</li>
        <li><strong>Wide Coverage:</strong> Whether city streets or highways, we’ve got you covered.</li>
      </ul>
    </div>

    <div class="about-image fade-in">
      <img src="/roadassist/images/img7.jpg" alt="RoadNova Team" />
    </div>
  </div>
</div>
<footer>
  <div class="footer-container">
    <div class="footer-column">
      <h3>RoadNova</h3>
      <p>  Reliable vehicle breakdown support at your fingertips. Available 24/7 to keep you moving safely.</p>
    </div>
    
    <div class="footer-column">
      <h3>Quick Links</h3>
      <a href="home.py">Home</a>
      <a href="about.py">About</a>
      <a href="#contact">Contact</a>
    </div>
    
    <div class="footer-column" id="contact">
      <h3>Contact Us</h3>
      <p>Email: support@RoadNova.com</p>
      <p>Phone: +91 98765 43210</p>
     <p><i class="fas fa-clock me-2"></i>24/7 Support</p>
     </div>
     <div class="footer-column">
      <h3>Follow Us</h3>
       <a href="#" class="text-white me-4"><i class="fab fa-facebook-f"></i></a>
        <a href="#" class="text-white me-4"><i class="fab fa-twitter"></i></a>
        <a href="#" class="text-white me-4"><i class="fab fa-instagram"></i></a>
        <a href="#" class="text-white me-4"><i class="fab fa-linkedin-in"></i></a>
     
    </div>
  </div>

  <div class="footer-bottom">
   &copy; <span class="year"></span>RoadNova. All rights reserved.
  </div>
</footer>



<div class="modal fade" id="userLoginModal" tabindex="-1" aria-labelledby="userLoginModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <button type="button" class="btn-close position-absolute end-0 m-3" data-bs-dismiss="modal" aria-label="Close"></button>
      <div class="modal-header">
        <div class="text-center w-100">
          <i class="fas fa-user-circle fa-3x mb-2"></i>
          <h5 class="modal-title">User Login</h5>
        </div>
      </div>
      <div class="modal-body">
        <form name="form2" method="post" enctype="multipart/form-data">
        <h4>Login As User</h4>
          <div class="mb-3">
                <label for="usermail"  class="form-label">Email:</label>
                <input type="email"id="usermail" class="form-control" name="usermail">
                </div>
                <div class="mb-3">
                <label for="password"  class="form-label">Password</label>
                <input type="password" id="password" class="form-control" name="password"> 
                 </div>   
                 <p class="important"><a href="forgot_password.py"  class="imlink">Forgot password</a></p>                   
              <button type="submit" class=" btn btn-primary " name="submit">Login</button>
              
              <p class="lm mt-3">Don't have an account? <a href="user_reg.py" class="imlink">Register</a></p>
            </form>
      </div>
    </div>
  </div>
</div>

<div class="modal fade" id="mechanicLoginModal" tabindex="-1" aria-labelledby="mechanicLoginModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <button type="button" class="btn-close position-absolute end-0 m-3" data-bs-dismiss="modal" aria-label="Close"></button>
      <div class="modal-header">
        <div class="text-center w-100">
          <i class="fas fa-tools fa-3x mb-2"></i>
          <h5 class="modal-title">Mechanic Login</h5>
        </div>
      </div>
      <div class="modal-body">
        <form method="post"  action="owner_login.py" target="owner"enctype="multipart/form-data" name="form3">
          <div class="mb-3">
            <label for="mechanicname" class="form-label">Email:</label>
            <input type="email" class="form-control" id="mechanicname" name="ownermail">
          </div>
          <div class="mb-3">
            <label for="mechanicpass" class="form-label">Password:</label>
            <input type="password" class="form-control" id="mechanicpass" name="mechanicpass">
          </div>
          <p class="important"><a href="forgot_shop_password.py" class="imlink">Forgot password/Username?</a></p>
          <button type="submit" class="btn btn-primary mb-2">Login</button>
          <p class="lm mt-3">Don't have an account? <a href="mechreg.py" class="imlink">Register</a></p>
          <iframe name="owner" style="display:none;"></iframe>
        </form>
      </div>
    </div>
  </div>
</div>


<div class="modal fade" id="adminLoginModal" tabindex="-1" aria-labelledby="adminLoginModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <button type="button" class="btn-close position-absolute end-0 m-3" data-bs-dismiss="modal" aria-label="Close"></button>
      <div class="modal-header">
        <div class="text-center w-100">
          <i class="fas fa-user-shield fa-3x mb-2"></i>
          <h5 class="modal-title">Admin Login</h5>
        </div>
      </div>
      <div class="modal-body">
       <form name="form1" method="post"  action="admin_login.py" target="login" enctype="multipart/form-data">
        <h4>Login As User</h4>
          <div class="mb-3">
                <label for="adminmail"  class="form-label">Email:</label>
                <input type="email"id="adminmail" class="form-control" name="adminmail">
                </div>
                <div class="mb-3">
                <label for="password"  class="form-label">Password</label>
                <input type="password" id="password" class="form-control" name="adminpass"> 
                 </div>                      
              <button type="submit" class=" btn btn-primary " name="submit">Login</button>
             <iframe name="login" style="display:none;"></iframe>
            </form>
      </div>
    </div>
  </div>
</div>






<script>
document.querySelectorAll('.year').forEach(el=>{el.textContent=new Date().getFullYear();});
  // Simple scroll-triggered fade-in animation
  function onEntry(entry) {
    entry.forEach(change => {
      if (change.isIntersecting) {
        change.target.classList.add('visible');
      }
    });
  }

  let options = { threshold: [0.1] };
  let observer = new IntersectionObserver(onEntry, options);

  document.querySelectorAll('.fade-in').forEach(element => {
    observer.observe(element);
  });
  
  document.getElementById('resetForm').addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent form from submitting

    const emailInput = document.getElementById('resetEmail');
    const resetMessage = document.getElementById('resetMessage');

    if (emailInput.value.trim() === '') {
      emailInput.classList.add('is-invalid');
    } else {
      emailInput.classList.remove('is-invalid');

      // Show success message
      resetMessage.classList.remove('d-none');
      resetMessage.classList.add('d-block');

      // Clear input field
      emailInput.value = '';

      // Wait 3 seconds, then redirect to homepage
      setTimeout(() => {
        location.href='./home.html' 
      }, 3000);
    }
  });
   
</script>
 <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
    crossorigin="anonymous"></script>

</body>
</html>

""")
form = cgi.FieldStorage()
Email = form.getvalue("usermail")
Password = form.getvalue("password")
Submit = form.getvalue("submit")

if Submit != None:
    q = """select user_id from users where email="%s" and password="%s" """ %( Email, Password)
    cur.execute(q)
    res = cur.fetchone()
    if res is not None:
        print("""
        <script>
        alert("login success!");
        location.href="user.py?user_id=%s"
        </script>
        """ % (res[0]))
    else:
        print("""
        <script>
        alert("incorrect username or password" );
        location.href="home.py"
        </script>
        """)
