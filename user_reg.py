#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html\r\n\r\n")

import pymysql, cgi, cgitb
cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

form = cgi.FieldStorage()

# Check if this is a registration submission
if "name" in form:
    name = form.getvalue("name")
    gender = form.getvalue("gender")
    email = form.getvalue("email")
    phone = form.getvalue("phone")
    address = form.getvalue("address")
    pincode = form.getvalue("pincode")
    password = form.getvalue("password")
    confirmpass = form.getvalue("confirmpass")

    if password != confirmpass:
        print("<script>alert('Passwords do not match');</script>")
    else:
        try:
            query = "INSERT INTO users (name, gender, email, phone, address, pincode, password, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(query, (name, gender, email, phone, address, pincode, password, 'Registered'))
            con.commit()
            print("<script>alert('Registration successful');window.location.href = 'user_reg.py';</script>")
        except Exception as e:
            print(f"<script>alert('Error: {str(e)}');</script>")

print("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>User Registration</title>
  
  <!-- Bootstrap CSS CDN -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">

  
  <style>
 
    /* Navbar Styles */
    .navbar-custom {
        background-color: #ffffff;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        padding: 0.5rem 1rem;
        margin-bottom: 20px;
    }
    .navbar-brand {
        font-weight: 700;
        font-size: 1.5rem;
        color: #4a148c;
    }
    .navbar-brand:hover {
        color: #6a1b9a;
        text-decoration: none;
    }
    .nav-link {
        color: #4a148c;
        font-weight: 500;
    }
    .nav-link:hover {
        color: #6a1b9a;
    }

    /* Existing styles */
    body {
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      padding: 20px;
      flex-direction: column; /* To place navbar on top */
    }
    .registration-form {
      background: white;
      padding: 30px;
      border-radius: 15px;
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
      max-width: 700px;
      width: 100%;
    }
    .form-title {
      color: #4a148c;
      font-weight: 700;
      text-align: center;
      margin-bottom: 25px;
    }
    .btn-primary {
      background-color: #6a1b9a;
      border: none;
    }
    .btn-primary:hover {
      background-color: #4a148c;
    }
  
  .imlink{
  color:orange;
  }

    
    .registration-form {
      background: white;
      padding: 30px;
      border-radius: 15px;
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
      max-width: 700px;
      width: 100%;
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
.important{
color:orange;
}

  </style>
</head>
<body>
<nav class="navbar navbar-expand-lg fixed-top">
      <div class="container-fluid">
        <a class="navbar-brand" href="home.py">
          <i class="fas fa-car-crash me-2"></i>RoadNova
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" href="home.py">Home</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

  <form class="registration-form" id="regForm" onsubmit="return validateForm()" action="user_reg.py" method="post" >
    <h2 class="form-title">User Registration</h2>

    <div class="row g-3">
      <div class="col-md-6">
        <label for="fullname" class="form-label">Full Name</label>
        <input type="text" class="form-control" id="name" name="name"  />
      </div>

      <div class="col-md-6">
        <label class="form-label d-block">Gender</label>
        <div class="form-check form-check-inline">
          <input class="form-check-input" type="radio" name="gender" id="genderMale" value="Male" />
          <label class="form-check-label" for="genderMale">Male</label>
        </div>
        <div class="form-check form-check-inline">
          <input class="form-check-input" type="radio" name="gender" id="genderFemale" value="Female" />
          <label class="form-check-label" for="genderFemale">Female</label>
        </div>
        <div class="form-check form-check-inline">
          <input class="form-check-input" type="radio" name="gender" id="genderOther" value="Other" />
          <label class="form-check-label" for="genderOther">Other</label>
        </div>
      </div>

      <div class="col-md-6">
        <label for="email" class="form-label">Email Address</label>
        <input type="email" class="form-control" id="email" name="email" placeholder="name@example.com" />
      </div>

      <div class="col-md-6">
        <label for="phone" class="form-label">Phone Number</label>
        <input type="tel" class="form-control" id="phone" name="phone" placeholder="10-digit phone number" maxlength="10" />
      </div>

      <div class="col-md-6">
        <label for="address" class="form-label">Address</label>
        <textarea class="form-control" id="address" name="address" rows="2" placeholder="Your address"></textarea>
      </div>

      <div class="col-md-6">
        <label for="pincode" class="form-label">Pincode</label>
        <input type="text" class="form-control" id="pincode" name="pincode" maxlength="6" placeholder="6-digit pincode" />
      </div>

     <div class="col-md-6 position-relative">
  <label for="password" class="form-label">Password</label>
  <div class="input-group">
    <input type="password" class="form-control" id="password" name="password" placeholder="At least 6 characters">
    <span class="input-group-text">
      <i class="bi bi-eye-slash" id="togglePassword" style="cursor: pointer;"></i>
    </span>
  </div>
</div>

<div class="col-md-6 position-relative">
  <label for="confirmpass" class="form-label">Confirm Password</label>
  <div class="input-group">
    <input type="password" class="form-control" id="confirmpass" name="confirmpass" placeholder="Confirm your password">
    <span class="input-group-text">
      <i class="bi bi-eye-slash" id="toggleConfirmPass" style="cursor: pointer;"></i>
    </span>
  </div>
</div>


    <div class="form-check my-3">
      <input type="checkbox" class="form-check-input" id="terms" />
      <label class="form-check-label" for="terms">I agree to the <a href="#" class="important" data-bs-toggle="modal" data-bs-target="#termsModal">Terms & Privacy Policy</a></label>
    </div>

    <button type="submit" class="btn btn-primary w-100">Register</button>
   <div class="terms"> <p class="link">Already have an account?<a href="#" class="important"  data-bs-toggle="modal" data-bs-target="#userLoginModal">Login</a></p>
  </form>
""")

print("""
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
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>

        </div>
      </div>
    </div>
  </div>
""")
print("""
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

""")
print("""
<script>
 
function validateForm(){
      const name = document.getElementById("name").value.trim();
      const genderOptions = document.getElementsByName("gender");
      const email = document.getElementById("email").value.trim();
      const phone = document.getElementById("phone").value.trim();
      const address = document.getElementById("address").value.trim();
      const pincode = document.getElementById("pincode").value.trim();
      const password = document.getElementById("password").value.trim();
      const confirmpass= document.getElementById("confirmpass").value.trim();
      const terms = document.getElementById("terms").checked;
      if (name === "" || !/^[a-zA-Z\s]+$/.test(name)) {
        alert("Please enter a valid full name (letters only).");
        return false;
      }

      let genderSelected = false;
      for (let i = 0; i < genderOptions.length; i++) {
        if (genderOptions[i].checked) {
          genderSelected = true;
          break;
        }
      }
      if (!genderSelected) {
        alert("Please select a gender.");
        return false;
      }

      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(email)) {
        alert("Please enter a valid email address.");
        return false;
      }

              if (!/^[6-9]\d{9}$/.test(phone)) {
          alert("Please enter a valid Indian phone number starting with 6, 7, 8, or 9.");
          return false;
        }


      if (address === "") {
        alert("Please enter your address.");
        return false;
      }

      if (!/^\d{6}$/.test(pincode)) {
        alert("Please enter a valid 6-digit pincode.");
        return false;
      }
      if(password.length < 6 || !/[A-Z]/.test(password[0]) || !/\d/.test(password) || !/[!@#$%^&*()_+\-=\]{};':"\\|,.<>?]/.test(password)) {
                 alert("Password must be at least 6 characters, start with a capital letter, and include at least one digit and one special symbol.");
                  return false;
                }
      
      if (password!==confirmpass) {
        alert("password and confirm password should be same.");
        return false;
      }

      if (!terms) {
        alert("You must agree to the Terms and Conditions.");
        return false;
      }
    return true;
}
const togglePassword = document.getElementById("togglePassword");
  const password = document.getElementById("password");

  togglePassword.addEventListener("click", function () {
    const type = password.getAttribute("type") === "password" ? "text" : "password";
    password.setAttribute("type", type);
    this.classList.toggle("bi-eye");
    this.classList.toggle("bi-eye-slash");
  });

  const toggleConfirmPass = document.getElementById("toggleConfirmPass");
  const confirmPass = document.getElementById("confirmpass");

  toggleConfirmPass.addEventListener("click", function () {
    const type = confirmPass.getAttribute("type") === "password" ? "text" : "password";
    confirmPass.setAttribute("type", type);
    this.classList.toggle("bi-eye");
    this.classList.toggle("bi-eye-slash");
  });
</script>
""")
print("""
  <!-- Bootstrap JS Bundle -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>

""")
