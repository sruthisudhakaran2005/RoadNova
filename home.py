#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
form = cgi.FieldStorage()
print("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>homepage|RoadNova</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        
        }
    

@media (max-width: 768px) {
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

/* Adjust body top padding */
body {
  padding-top: 70px;
}
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

    .banner {
      width: 100%;
      height: auto;
      object-fit: cover;
    }
    .cta-section button:hover {
  background: #c62828;
}

   
   .btn{
    width:180px;
    background-color: #f29e37;
   }
   @media (max-width: 768px) {
  .offcanvas-end {
    width: 200px !important;
  }
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
    .form-container{
      width:400px;
      margin-left: 50px;

    }
    
      @keyframes pulse {
    0% {
      transform: scale(1);
    }
    50% {
      transform: scale(1.1);
    }
    100% {
      transform: scale(1);
    }
  }
 .service-image {
      width: 100%;
      height: auto;
      object-fit: cover;
    }

    .service-card {
      color: white;
      padding: 20px;
      height: 220px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    }

    .service-section {
      margin-top: -90px;
      z-index: 10;
      position: relative;
    }

    @media (max-width: 767.98px) {
      .service-section {
        margin-top: 0;
        padding-top: 20px;
      }

      .service-card {
        margin-bottom: 20px;
      }
    }
  @keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateX(50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes bounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}

button {
  transition: transform 0.3s ease;
}

button:hover {
  transform: scale(1.2); 
}

.media-crop {
  width: 300px;
  height: 400px;
  overflow: hidden;
  position: relative;
}

/* Image fills container */
.media-crop img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.animate-slide-zoom {
    animation: slideZoom 2.5s ease-out infinite forwards;
}

@keyframes slideZoom {
  0% {
    transform: translateX(100px) scale(0.5); 
    opacity: 0;
  }
  100% {
    transform: translateX(0) scale(1);       
    opacity: 1;
  }
}

footer a {
  color: #ffffff;
  text-decoration: none;
  transition: color 0.3s ease;
}

footer a:hover {
  color: #f9a825 !important;
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
.scroll-wrapper {
  overflow: hidden;
  position: relative;
  width: 100%;
}

.auto-scroll-container {
  display: flex;
  width: max-content;
  animation: scroll-left 30s linear infinite;
}

.scroll-wrapper:hover .auto-scroll-container {
  animation-play-state: paused;
}

.service-card-custom {
  flex: 0 0 auto;
  width: 280px;
  margin-right: 20px;
  background: #f8f9fa;
  border-radius: 12px;
  padding: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
  transition: transform 0.3s ease;
}

.service-card-custom:hover {
  transform: scale(1.05);
}

.service-card-custom img {
  width: 100%;
  height: 180px;
  object-fit: cover;
  border-radius: 8px;
}

.service-card-custom h4 {
  margin-top: 10px;
  font-size: 1.2em;
  color: #333;
}

.service-card-custom p {
  font-size: 0.95em;
  color: #555;
}

/* Smooth infinite loop */
@keyframes scroll-left {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-50%);
  }
}



.btn-close{
  margin-left: 400px;
  margin-top: 30px;
}

.dropdown-toggle{
  border:none;
}
@media (max-width: 768px) {
  .navbar-toggler {
    border: none !important;
    outline: none !important;
    box-shadow: none !important;
  }
}


.modal-header {
  border: none !important;
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




@keyframes zoomInReset {
  0% {
    opacity: 0;
    transform: scale(0.8);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}

#resetModal .modal-body {
  padding: 30px 40px;
}

#resetModal .form-label {
  font-weight: bold;
  color: #333;
  margin-left: 0px;
}
#resetModal .modal-content {
  background: #f1f8e9; /* Light green background */
  border-radius: 15px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
  animation: zoomInReset 0.5s ease;
}

#resetModal .form-control {
  border-radius: 10px;
  padding: 12px;
  font-size: 1rem;
}

#resetModal .btn-primary {
  background: #28a745;
  border: none;
  border-radius: 10px;
  padding: 12px 30px;
  font-size: 1rem;
  font-weight: 600;
}

#resetModal .btn-primary:hover {
  background: #218838;
}

#resetMessage {
  margin-top: 10px;
  font-weight: bold;
}
#resetModal .btn-primary {
  background: #00796b; /* Teal color */
  border: none;
  border-radius: 10px;
  padding: 12px 30px;
  font-size: 1rem;
  font-weight: 600;
  transition: background 0.3s ease;
}

#resetModal .btn-primary:hover {
  background: #004d40;
}
@keyframes zoomInReset {
  0% {
    opacity: 0;
    transform: scale(0.85);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}
.roadnova:hover{
color:#EE4B2B;
}


  </style>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
  <div class="container-fluid">
    <a class="navbar-brand d-flex align-items-center" href="#">
       <i class="fas fa-car-crash me-2"></i>
      <span class="mainhead ms-2">RoadNova</span>
    </a>

    <button class="navbar-toggler d-lg-none" type="button" data-bs-toggle="offcanvas" data-bs-target="#mobileMenu" aria-controls="mobileMenu">
      <span class="navbar-toggler-icon"></span>
          </button>

    <div class="collapse navbar-collapse d-none d-lg-flex justify-content-end" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item"><a class="nav-link" href="home.py">Home</a></li>
          <li class="nav-item"><a class="nav-link" href="#service">Services</a></li>
          <li class="nav-item"><a class="nav-link" href="about.py">About</a></li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="loginDropdownDesktop" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Login
          </a>
          <ul class="dropdown-menu" aria-labelledby="loginDropdownDesktop">
            <li><a class="dropdown-item" href="#" data-bs-toggle="modal" data-bs-target="#userLoginModal">User</a></li>
            <li><a class="dropdown-item" href="#" data-bs-toggle="modal" data-bs-target="#mechanicLoginModal">Mechanic</a></li>
            <li><a class="dropdown-item" href="#" data-bs-toggle="modal" data-bs-target="#adminLoginModal">Admin</a></li>
            </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="registerDropdownDesktop" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Register
          </a>
          <ul class="dropdown-menu" aria-labelledby="registerDropdownDesktop">
            <li><a class="dropdown-item" href="user_reg.py">User</a></li>
            <li><a class="dropdown-item" href="mechreg.py" >Mechanic</a></li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link" href="#contact">Contact</a></li>
      </ul>
    </div>

    <div class="offcanvas offcanvas-end d-lg-none" tabindex="-1" id="mobileMenu" aria-labelledby="mobileMenuLabel" style="width:200px;">
      <div class="offcanvas-header">
        <h5 class="offcanvas-title" id="mobileMenuLabel"> Links</h5>
        <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
      </div>
      <div class="offcanvas-body">
        <ul class="navbar-nav">
          <li class="nav-item"><a class="nav-link" href="home.py">Home</a></li>
          <li class="nav-item"><a class="nav-link" href="about.py">About</a></li>
            <li class="nav-item"><a class="nav-link" href="#service">Services</a></li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="loginDropdownMobile" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Login
            </a>
            <ul class="dropdown-menu" aria-labelledby="loginDropdownMobile">
              <li><a class="dropdown-item" href="#" data-bs-toggle="modal" data-bs-target="#userLoginModal">User</a></li>
              <li><a class="dropdown-item" href="#" data-bs-toggle="modal" data-bs-target="#mechanicLoginModal">Mechanic</a></li>
              <li><a class="dropdown-item" href="#" data-bs-toggle="modal" data-bs-target="#adminLoginModal">Admin</a></li>
              </ul>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="registerDropdownMobile" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Register
            </a>
            <ul class="dropdown-menu" aria-labelledby="registerDropdownMobile">
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
        <form name="form2" method="post"action="user_login.py" target="user" enctype="multipart/form-data">
        <h4>Login As User</h4>
          <div class="mb-3">
                <label for="usermail"  class="form-label">Email:</label>
                <input type="email"id="usermail" class="form-control" name="usermail">
                </div>
                <div class="mb-3">
                <label for="password"  class="form-label">Password</label>
                <input type="password" id="password" class="form-control" name="password"> 
                 </div>   
                 <p class="important"><a href="forgot_password.py" class="imlink">Forgot password</a></p>                   
              <button type="submit" class=" btn btn-primary " name="submit">Login</button>
              
              <p class="lm mt-3">Don't have an account? <a href="user_reg.py" class="imlink">Register</a></p>
              <iframe name="user" style="display:none;"></iframe>
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
        <h4>Login As Admin</h4>
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


    



      

<section style="background: url('/roadassist/images/img4.webp') center/cover no-repeat; padding: 100px 20px; text-align: center; color: white;" class="main-section">
  <h1 style="font-size: 3em;" class="roadnova">24/7 Vehicle Breakdown Assistance</h1>
  <h1 style="font-size: 3em;" class="roadnova">RoadNova</h1>
  <p style="font-size: 1.2em;">Stranded? We’re just a call away. Reliable. Fast. Nationwide.</p>
  <a class="btn"  onclick="showAlertAndRedirect()" style="padding: 15px 30px; background-color: #ff5722; color: white; font-weight: bold; text-decoration: none; border-radius: 5px;display:inline-block; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.2)'" onmouseout="this.style.transform='scale(1)'">Get Help Now</a>
    <form method="post" name="form" class="d-flex justify-content-center" style="margin-top: 40px;" action="search_shop.py">
    <input 
      type="text" 
      name="sname" 
      placeholder="Search using location" 
      class="rounded-pill" 
      style="
        width: 300px; 
        padding: 12px 20px; 
        border: none; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        font-size: 1.1em; 
        outline: none;
        transition: box-shadow 0.3s ease;
        color: #333;
      "
      onfocus="this.style.boxShadow='0 0 8px 3px #ff5722'"
      onblur="this.style.boxShadow='0 4px 6px rgba(0,0,0,0.3)'"
    />
    <button 
      type="submit" 
      class="search-button" 
      name="search"
      style="
        margin-left: 10px;
        background-color: #ff5722;
        border: none;
        padding: 12px 18px;
        border-radius: 50%;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        transition: background-color 0.3s ease, transform 0.3s ease;
      "
      onmouseover="this.style.backgroundColor='#e64a19'; this.style.transform='scale(1.1)'"
      onmouseout="this.style.backgroundColor='#ff5722'; this.style.transform='scale(1)'"
    >
      <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="white" class="bi bi-search" viewBox="0 0 16 16">
        <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"/>
      </svg>
    </button>
  </form>
</section>
""")
location = form.getvalue("sname")
shops = []

if location:
    query = "SELECT * FROM mechanicshops WHERE shop_address LIKE %s AND status='Approved'"
    cur.execute(query, ("%" + location + "%",))
    shops = cur.fetchall() # This will be either a list of results or an empty list if no match is found

    if shops:
        for shop in shops:
            shop_id = shop[0]
            shop_name = shop[10]
            shop_address = shop[11]
            shop_contact = shop[4]
            shop_image = shop[12]
            shop_hours = shop[14]



print("""
<section style="padding: 60px 20px; text-align: center;" id="service">
  <h3 class="head">Our Services</h3>

  <div class="scroll-wrapper">
    <div class="auto-scroll-container">
      <!-- First Set -->
      <div class="service-card-custom">
        <img src="/roadassist/images/towing.jpg" alt="Towing Service" >
        <h4>Towing</h4>
        <p>Emergency towing services anywhere, anytime.</p>
      </div>
      <div class="service-card-custom">
        <img src="/roadassist/images/jumbstart.jpg" alt="Battery Jumpstart" >
        <h4>Battery Jumpstart</h4>
        <p>Dead battery? We'll revive it on the spot.</p>
      </div>
      <div class="service-card-custom">
        <img src="/roadassist/images/fuel.jpg" alt="Fuel Delivery">
        <h4>Fuel Delivery</h4>
        <p>Run out of fuel? We’ll bring it to you quickly.</p>
      </div>
      <div class="service-card-custom">
        <img src="/roadassist/images/flattire.jpg" alt="Flat Tire" >
        <h4>Flat Tire Assistance</h4>
        <p>Flat tire? We’ll repair or replace it instantly.</p>
      </div>
     
      <div class="service-card-custom">
        <img src="/roadassist/images/lock.jpg" alt="Lockout Help" >
        <h4>Lockout Help</h4>
        <p>Locked out? We help you get back in fast.</p>
      </div>

      <!-- Duplicate Set -->
      <div class="service-card-custom">
        <img src="/roadassist/images/towing.jpg" alt="Towing Service" >
        <h4>Towing</h4>
        <p>Emergency towing services anywhere, anytime.</p>
      </div>
      <div class="service-card-custom" >
        <img src="/roadassist/images/jumbstart.jpg" alt="Battery Jumpstart">
        <h4>Battery Jumpstart</h4>
        <p>Dead battery? We'll revive it on the spot.</p>
      </div>
      <div class="service-card-custom">
        <img src="/roadassist/images/fuel.jpg" alt="Fuel Delivery" >
        <h4>Fuel Delivery</h4>
        <p>Run out of fuel? We’ll bring it to you quickly.</p>
      </div>
      <div class="service-card-custom">
        <img src="/roadassist/images/flattire.jpg" alt="Flat Tire">
        <h4>Flat Tire Assistance</h4>
        <p>Flat tire? We’ll repair or replace it instantly.</p>
      </div>
     
      <div class="service-card-custom">
        <img src="/roadassist/images/lock.jpg" alt="Lockout Help">
        <h4>Lockout Help</h4>
        <p>Locked out? We help you get back in fast.</p>
      </div>
    </div>
  </div>
</section>

<div class="container p-0">
    <img src="/roadassist/images/img5.avif" alt="Car Breakdown" class="service-image">
  </div>

  <div class="container service-section">
    <div class="row text-center justify-content-center">

      <div class="col-md-4 mb-3">
        <div class="service-card bg-primary">
          <h5>Air Filter Change</h5>
          <p>Improve engine performance and fuel efficiency with a quick air filter replacement—done at your location, fast and hassle-free.</p>
        </div>
      </div>

      <div class="col-md-4 mb-3">
        <div class="service-card bg-purple" style="background-color: #6f42c1;">
          <h5>Battery-water</h5>
          <p>Ensure smooth starts and extend battery life with a quick top-up—convenient, on-site battery water service.</p>
        </div>
      </div>

      <div class="col-md-4 mb-3">
        <div class="service-card bg-danger" style="background-color: #8c4c4c;">
          <h5>AC Filter Cleaning</h5>
          <p>Professional cleaning of your car’s AC filter removes dust, pollen, and odors, improving airflow and ensuring fresh air inside your vehicle.</p>
        </div>
      </div>

    </div>
  </div>

  <div class="modal fade" id="termsModal" tabindex="-1" aria-labelledby="termsModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="termsModalLabel">Terms & Privacy Policy</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">

        <h6>1. Terms of Service</h6>
        <ul>
          <li>Our assistance is subject to availability and coverage area.</li>
          <li>You must provide accurate information when requesting help.</li>
          <li>We reserve the right to refuse service in certain cases (e.g. abuse or unsafe conditions).</li>
          <li>We are not liable for delays due to traffic, weather, or force majeure events.</li>
        </ul>

        <h6>2. Privacy Policy</h6>
        <p>We collect personal information such as:</p>
        <ul>
          <li>Your name, phone number, and location when you request help</li>
          <li>Issue details </li>
        </ul>
        <p>We use this data to:</p>
        <ul>
          <li>Dispatch roadside assistance</li>
          <li>Contact you during the process</li>
          <li>Improve our service quality</li>
        </ul>

        <h6>3. Data Protection</h6>
        <ul>
          <li>Your data is stored securely and never sold.</li>
          <li>We may share info with partners only for service delivery or legal compliance.</li>
        </ul>

       <h6>4. Cancellation and Refund Policy</h6>
        <ul>
          <li>25% of the total amount paid will be deducted as a cancellation fee.</li>
          <li>75% of the total amount paid will be refunded to you..</li>
        </ul>
        <h6>5. User Rights</h6>
        <p>You may request to view, modify, or delete your personal data by contacting <a href="mailto:support@RoadNova.com">support@RoadNova.com</a>.</p>

        <p class="text-muted">Last updated: August 9, 2025</p>

      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
<section id="about" style="background-color: #e9ecef; padding: 60px 20px;">
  <div class="container">
    <h2 class="text-center mb-4">About Us</h2>
    <div class="row align-items-center">
     
      <div class="col-md-6 mb-4 mb-md-0 animate-left">
        <p style="font-size: 1.1em;">
          At <strong>RoadNova</strong>, we believe that no one should be stranded due to a vehicle problem.
          We offer 24/7 support, including towing, battery jumpstarts, tire replacements, and emergency fuel delivery.
          <br><br>
          Our certified professionals ensure quick, safe, and affordable assistance, wherever you are.
        </p>
      </div>

   
      <div class="col-md-6 animate-right">
        <img src="/roadassist/images/aboutus.jpg" alt="About Us" class="img-fluid rounded shadow" />
      </div>
    </div>
  </div>
</section>




<section style="background-color:white; padding: 50px 20px;">
  <div class="container">
    <h2 class="text-center mb-5">Why Choose Us?</h2>
    <div class="row align-items-center">
     
      <div class="col-md-6">
        <div class="media-crop animate-slide-zoom">
       <img src="/roadassist/images/cartoon.jpg" alt="img" height="250px">
        </div>
      </div>
       <div class="col-md-6">
        <ul style="list-style: none; padding: 0; font-size: 2.1em;">
          <li>✔️ 24/7 Nationwide Assistance</li>
          <li>✔️ Trusted & Verified Professionals</li>
          <li>✔️ Affordable Transparent Pricing</li>
          <li>✔️ Quick Response Time</li>
        </ul>
          </div>
    </div>
  </div>
</section>



</section>
<footer class="bg-dark text-white pt-5 pb-4">
  <div class="container text-md-left">
    <div class="row text-md-left">

      <!-- Logo & Description -->
      <div class="col-md-3 col-lg-3 col-xl-3 mx-auto mt-3">
        <h5 class="text-uppercase mb-4 font-weight-bold">
           <i class="fas fa-car-crash me-2"></i>
          RoadNova
        </h5>
        <p>
          Reliable vehicle breakdown support at your fingertips. Available 24/7 to keep you moving safely.
        </p>
      </div>

      <!-- Navigation Links -->
      <div class="col-md-2 col-lg-2 col-xl-2 mx-auto mt-3">
        <h5 class="text-uppercase mb-4 font-weight-bold">Quick Links</h5>
        <p><a href="./home.html" class="text-white text-decoration-none">Home</a></p>
        <p><a href="about.html" class="text-white text-decoration-none">About</a></p>
        <p><a href="#contact" class="text-white text-decoration-none">Contact</a></p>
        <p><a href="#" data-bs-toggle="modal" data-bs-target="#userLoginModal" class="text-white text-decoration-none">Login</a></p>
      </div>

      <div class="col-md-4 col-lg-3 col-xl-3 mx-auto mt-3" id="contact">
        <h5 class="text-uppercase mb-4 font-weight-bold">Contact</h5>
        <p><i class="fas fa-envelope me-2"></i>support@RoadNova.com</p>
        <p><i class="fas fa-phone me-2"></i>+91 98765 43210</p>
        <p><i class="fas fa-clock me-2"></i>24/7 Support</p>
      </div>

      <!-- Social Media -->
      <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mt-3">
        <h5 class="text-uppercase mb-4 font-weight-bold">Follow Us</h5>
        <a href="#" class="text-white me-4"><i class="fab fa-facebook-f"></i></a>
        <a href="#" class="text-white me-4"><i class="fab fa-twitter"></i></a>
        <a href="#" class="text-white me-4"><i class="fab fa-instagram"></i></a>
        <a href="#" class="text-white me-4"><i class="fab fa-linkedin-in"></i></a>
      </div>

    </div>

    <hr class="mb-4">

    
    <div class="row align-items-center">
      <div class="col-md-7 col-lg-8">
        <p class="text-center text-md-start"> 
         <a href="#" data-bs-toggle="modal" data-bs-target="#termsModal">Terms & Privacy Policy</a>
        </p>
        <p class="text-center text-md-start">
          &copy; <span class="year"></span> <strong>RoadNova</strong>. All rights reserved.
        </p>
      </div>
    </div>
  </div>
</footer>


<div class="modal fade" id="searchResultsModal" tabindex="-1" aria-labelledby="searchResultsModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-xl modal-dialog-centered modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="searchResultsModalLabel">Search Results</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body" id="searchResultsBody">
        </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>


<script>
document.querySelectorAll('.year').forEach(el=>{el.textContent=new Date().getFullYear();});
 function user(event) {
    event.preventDefault();
    const useremail = document.getElementById("useremail").value.trim();
    const userpass = document.getElementById("userPassword").value.trim();

    if (useremail === "") {
        alert("Please enter your email.");
        return false;
    }
    if (userpass === "") {
        alert("Please enter your password.");
        return false;
    }

    // Since the form is submitted to home.py, you can let it proceed
    // The Python script will handle the redirection.
    document.getElementById("userlogin").submit();
    return true;
}
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
  
  function user(event){
    const username = document.getElementById("username").value.trim();
    const pass= document.getElementById("userPassword").value.trim();
    if (username ===""){
    alert("enter username");
    return false;
    }
    if (pass ===""){
    alert("enter your password");
    return false;
    }
    return true;
    
    }
     document.getElementById("otpForm").addEventListener("submit", function() {
    alert("Form is being submitted!");
  });
  
   
</script>




 
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
    crossorigin="anonymous"></script>
</body>
</html>

""")

