#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
cgitb.enable()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>User Registration</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet" />
  <style>
    body {
      background: linear-gradient(135deg, #dee1f0 0%, #d6c0eb 100%);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 20px;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    .navbar-custom {
      background-color: rgb(242, 234, 223);
    }

    .mainhead {
      font-weight: 500;
    }

    .container-custom {
      margin-top: 100px;
      background: #fff;
      border-radius: 15px;
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
      overflow: hidden;
      width: 100%;
      max-width: 1100px;
    }

    .form-image {
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 15px 0 0 15px;
    }

    @media (max-width: 768px) {
      .form-image {
        border-radius: 15px 15px 0 0;
        height: 250px;
      }
    }

    .form-section-container {
      padding: 30px 25px;
    }

    h2 {
      font-weight: 700;
      text-align: center;
      margin-bottom: 30px;
      color: #4a148c;
      letter-spacing: 1.5px;
    }

    label {
      font-weight: 600;
      color: #4a148c;
    }

    .form-section {
      margin-bottom: 30px;
      padding-bottom: 15px;
      border-bottom: 1px solid #e0e0e0;
    }

    textarea.form-control {
      resize: vertical;
    }

    .btn-primary {
      background: #6a1b9a;
      border: none;
      width: 140px;
      font-weight: 600;
    }

    .btn-primary:hover {
      background: #4a148c;
    }

    .btn-outline-danger {
      width: 140px;
      font-weight: 600;
    }

    .form-check-label {
      font-weight: 500;
      color: #333;
    }

    .terms {
      text-align: center;
      margin-top: 20px;
    }

    .important {
      text-decoration: none;
    }
    @media (max-width: 768px) {
  .form-image {
    width: 100%;
    height: auto;
  }

  .container-custom {
    border-radius: 15px;
  }
}
.overlay-text {
  position: absolute;
  top: 500px;
  left: 540px;
  color: #ffffff;
  font-size: 1rem;
  font-weight: bold;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
  z-index: 1;
}

@media (max-width: 768px) {
  .overlay-text {
    font-size: large;
    top: 380px;
    left: 270px;
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


  </style>
</head>
<body>

  <!-- Navbar -->
  <nav class="navbar navbar-expand-lg navbar-custom fixed-top py-2">
    <div class="container-fluid d-flex align-items-center justify-content-center">
      <h3 class="mainhead mb-0">On Road Vehicle Breakdown Assistance</h3>
    </div>
  </nav>

  <!-- Form Layout -->
  <div class="container-custom row mx-2">
    <!-- Left Side Image -->
    <div class="col-md-6 p-0">
      <img src="/roadassist/images/img16.jpg" alt="Assistance Image" class="form-image" >
       <div class="overlay-text">Register Now</div>
    </div>

    <!-- Right Side Form -->
    <div class="col-md-6 form-section-container">
      <h2>User Registration</h2>
      <form name="form"  method="post" onsubmit="return validation(event)" action="reg.py" target="user">
        <!-- Personal Details -->
        <div class="form-section">
          <h5 class="mb-4">Personal Details</h5>
          <div class="row g-3">
            <div class="col-md-6">
              <label for="name" class="form-label">Full Name</label>
              <input type="text" id="name" class="form-control" name="name" />
            </div>
            <div class="col-md-6">
              <label class="form-label d-block">Gender</label>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" id="genderMale" name="gender" value="Male" />
                <label class="form-check-label" for="genderMale">Male</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" id="genderFemale" name="gender" value="Female" />
                <label class="form-check-label" for="genderFemale">Female</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" id="genderOther" name="gender" value="Other" />
                <label class="form-check-label" for="genderOther">Other</label>
              </div>
            </div>
            <div class="col-md-6">
              <label for="email" class="form-label">Email Address</label>
              <input type="email" id="email" class="form-control" name="email" />
            </div>
            <div class="col-md-6">
              <label for="phone" class="form-label">Phone Number</label>
              <input type="tel" id="phone" class="form-control" name="phone" maxlength="10" />
            </div>
            <div class="col-md-6">
              <label for="address" class="form-label">Address</label>
              <textarea id="address" class="form-control" rows="2" name="address"></textarea>
            </div>
            <div class="col-md-6">
              <label for="pincode" class="form-label">Pincode</label>
              <input type="text" id="pincode" class="form-control" name="pincode" />
            </div>
             <div class="col-md-6">
              <label for="password" class="form-label">Password:</label>
              <input type="password" id="password" class="form-control" name="password" />
            </div>
             <div class="col-md-6">
              <label for="password" class="form-label">Confirm Password:</label>
              <input type="password" id="confirmpass" class="form-control" name="confirmpass" />
            </div>

          </div>
        </div>



        <!-- Terms & Submit -->
        <div class="form-check mb-3">
          <input class="form-check-input" type="checkbox" id="terms" name="check" />
          <label class="form-check-label" for="terms"> I agree to the Terms and Conditions </label>
        </div>

        <div class="d-flex justify-content-center gap-3">
          <button type="submit" class="btn btn-primary" name="submit">Register</button>
        <button type="reset" class="btn btn-outline-danger" name="reset">Cancel</button>
        </div>

        <div class="terms"> <p class="link">Already have an account?<a href="#" class="important"  data-bs-toggle="modal" data-bs-target="#userLoginModal">Login</a></p>
          <a href="#" class="important" data-bs-toggle="modal" data-bs-target="#termsModal">Terms & Privacy Policy</a>
        </div>
         <iframe name="user" style="display:none;"></iframe>
      </form>
    </div>
  </div>

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
        <form name="userlogin" id="userlogin" class="p-2" method="post" onsubmit="return user(event)">
          <div class="mb-3">
            <label for="email" class="form-label">Email:</label>
            <input type="text" class="form-control" id="usermail" name="usermail">
          </div>
          <div class="mb-3">
            <label for="userPassword" class="form-label">Password:</label>
            <input type="password" class="form-control" id="userPassword" name="userpass">
          </div>
          <p class="important"><div>
            <p class="important"><a href="#" class="imlink" data-bs-toggle="modal" data-bs-target="#resetModal">Forgot password/Username?</a></p>
          </div>
          <button type="submit" class="btn btn-primary" name="login">Login</button>
          <p class="lm mt-3">Don't have an account? <a href="./userreg.html" class="imlink">Register</a></p>
        </form>
      </div>
    </div>
  </div>
</div>

<div class="modal fade" id="resetModal" tabindex="-1" aria-labelledby="resetModalLabel" aria-hidden="true" >
  <div class="modal-dialog">
    <div class="modal-content">

    <div class="modal-header">
  <div class="text-center w-100">
    <i class="fas fa-unlock-alt fa-2x mb-2"></i>
    <h5 class="modal-title">Reset Password / Username</h5>
  </div>
  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
</div>


      <!-- Modal Body -->
      <div class="modal-body">
        <form id="resetForm" method="post" novalidate>
          <div class="mb-3">
            <label for="resetEmail" class="form-label">Email address</label>
            <input type="email" class="form-control" id="resetEmail" name="resetEmail"  required>
            <div class="invalid-feedback">Please enter a valid email.</div>
          </div>

          <div id="resetMessage" class="text-success d-none">Your New Password And Username will be send to you email</div>

          <button type="submit" class="btn btn-primary " name="submit" style="width:200px;margin-left: 130px;">Submit</button>
        </form>
      </div>

    </div>
  </div>
</div>



  <!-- Terms Modal -->
  <div class="modal fade" id="termsModal" tabindex="-1" aria-labelledby="termsModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-scrollable">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="termsModalLabel">Terms & Privacy Policy</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div style="max-width: 800px; margin: auto; font-family: Arial, sans-serif;">
          <h2>Terms & Policy for User Registration</h2>
          <p>By registering for our On-Road Vehicle Breakdown Assistance service, you agree to the following terms and conditions:</p>

          <h3>1. User Eligibility</h3>
          <p>You must be at least 18 years of age and possess a valid driver’s license and a registered vehicle to use our services.</p>

          <h3>2. Service Availability</h3>
          <p>Our services are available 24/7 in covered regions. Coverage areas may vary and are subject to change without notice.</p>

          <h3>3. User Responsibilities</h3>
          <ul>
            <li>Provide accurate vehicle and contact information.</li>
            <li>Ensure you are in a safe location while waiting for assistance.</li>
            <li>Do not misuse the service or provide false requests.</li>
          </ul>

          <h3>4. Data Usage & Privacy</h3>
          <p>Your personal information (name, phone number, location, vehicle details) will be used only to provide and improve the service, in accordance with our <a href="#">Privacy Policy</a>.</p>

          <h3>5. Liability Disclaimer</h3>
          <p>We strive to respond promptly, but we are not liable for delays or third-party actions. Service is provided “as is” without warranties.</p>

          <h3>6. Payment & Charges</h3>
          <p>Some services may be chargeable. Charges will be communicated before service is dispatched. Users are responsible for ensuring payment upon completion.</p>

          <h3>7. Termination</h3>
          <p>We reserve the right to suspend or terminate your access for violation of terms or misuse of services.</p>


        </div>

          <p><strong>Last updated: August 9, 2025</strong></p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>

        </div>
      </div>
    </div>
  </div>


  <script>
    function validation(event) {
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

      if (!/^\d{10}$/.test(phone)) {
        alert("Please enter a valid 10-digit phone number.");
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
       if (password=== "") {
        alert("Enter strong password.");
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
   return false;
      }

      if (!/^\d{6}$/.test(pincode)) {
        alert("Please enter a valid 6-digit pincode.");
        return false;
      }
       if (password=== "") {
        alert("Enter strong password.");
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


  </script>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

""")
form = cgi.FieldStorage()
Name = form.getvalue("name")
Gender = form.getvalue("gender")
Email = form.getvalue("email")
Phone = form.getvalue("phone")
Address = form.getvalue("address")
Pincode = form.getvalue("pincode")
Password = form.getvalue("password")
Submit = form.getvalue("submit")

if Submit is not None:
    q = """ insert into users(name,gender,email,phone,address,pincode,password,status) 
    values('%s','%s','%s','%s','%s','%s','%s','Registered')""" % (
    Name, Gender, Email, Phone, Address, Pincode, Password)
    cur.execute(q)
    con.commit()

    print("""
        <script>
        alert("Registration successful!");
        </script> 
        """)
