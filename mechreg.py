#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe

print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb,os
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
print("""
<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Mechanic Shop Registration</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" />
  <style>
    
  
    .important{
      text-decoration-line: none;
      color: #2a5494;
    }
    .terms{
      margin-left: 500px;
      color:#2a5494;
    }
     .navbar-custom {
      background-color: rgb(242, 234, 223);
    }

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
.imlink{
  color:purple;
}
.imlink:hover{
  color:rgb(243, 92, 235);
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

#mresetModal .modal-body {
  padding: 30px 40px;
}

#mresetModal .form-label {
  font-weight: bold;
  color: #333;
  margin-left: 0px;
}
#mresetModal .modal-content {
  background: #f1f8e9; /* Light green background */
  border-radius: 15px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
  animation: zoomInReset 0.5s ease;
}

#mresetModal .form-control {
  border-radius: 10px;
  padding: 12px;
  font-size: 1rem;
}

#mresetModal .btn-primary {
  background: #28a745;
  border: none;
  border-radius: 10px;
  padding: 12px 30px;
  font-size: 1rem;
  font-weight: 600;
}

#mresetModal .btn-primary:hover {
  background: #218838;
}

#mresetMessage {
  margin-top: 10px;
  font-weight: bold;
}
#mresetModal .btn-primary {
  background: #00796b; /* Teal color */
  border: none;
  border-radius: 10px;
  padding: 12px 30px;
  font-size: 1rem;
  font-weight: 600;
  transition: background 0.3s ease;
}

#mresetModal .btn-primary:hover {
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

 body {
      font-family: Arial, sans-serif;
      background-color: #f7f7f7;
      padding: 20px;
    }

    .container {
      max-width: 1000px;
      margin: auto;
      background: #fff;
      padding: 30px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }

    h2 {
      text-align: center;
      margin-bottom: 30px;
    }

    .form-sections {
      display: flex;
      gap: 20px;
      flex-wrap: wrap;
    }

    .section {
      flex: 1;
      min-width: 300px;
    }

    .form-group {
      margin-bottom: 15px;
    }

    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }

    input, select, textarea {
      width: 100%;
      padding: 8px;
      box-sizing: border-box;
      border-radius: 5px;
      border: 1px solid #ccc;
    }

    input[type="file"] {
      padding: 3px;
    }

    .buttons {
      text-align: center;
      margin-top: 30px;
    }

    button {
      padding: 10px 20px;
      margin: 0 10px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      font-size: 16px;
    }

    .register-btn {
      background-color: #28a745;
      color: white;
    }

    .cancel-btn {
      background-color: #dc3545;
      color: white;
    }

    @media (max-width: 768px) {
      .form-sections {
        flex-direction: column;
      }
    }
 #check {
  transform: scale(1.1);
  margin-right: 6px; /* Reduce spacing */
}
.important{
color:orange;

}
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


  </style>
</head>
<body >
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
  

<div class="container">
  <h2>Mechanic Shop Registration Form</h2>
  <form id="registrationForm" onsubmit="return validateForm(event)" method="post"enctype="multipart/form-data">

    <div class="form-sections">
      
      <!-- Owner Section -->
      <div class="section">
        <h3>Owner Information</h3>

        <div class="form-group">
          <label for="ownerName">Owner Name</label>
          <input type="text" id="ownerName" name="ownerName">
        </div>
        
        <div class="form-group">
          <label for="dob">Date of Birth</label>
          <input type="date" id="dob" name="dob">
        </div>
       <div class="form-group">
          <label for="ownerEmail"> Email</label>
          <input type="email" id="ownerEmail" name="ownerEmail" >
        </div>

        <div class="form-group">
          <label for="phone">Phone Number</label>
          <input type="tel" id="phone" name="phone">
        </div>

        <div class="form-group">
  <label>Gender</label><br>
  <div class="form-check form-check-inline" >
    <input class="form-check-input" type="radio" name="gender" id="genderMale" value="male">
    <label class="form-check-label" for="genderMale">Male</label>
  </div>
  <div class="form-check form-check-inline">
    <input class="form-check-input" type="radio" name="gender" id="genderFemale" value="female">
    <label class="form-check-label" for="genderFemale">Female</label>
  </div>
  <div class="form-check form-check-inline">
    <input class="form-check-input" type="radio" name="gender" id="genderOther" value="other">
    <label class="form-check-label" for="genderOther">Other</label>
  </div>
</div>


        <div class="form-group">
          <label for="address">Address</label>
          <textarea id="address" name="address" rows="2"></textarea>
        </div>

        <div class="form-group">
          <label for="adharProof">Aadhar Proof </label>
          <input type="file" id="adharProof" name="adharProof" accept="image/*,.pdf" >
        </div>

        <div class="form-group"> 
  <label for="state">State</label>
  <select id="state" name="state">
    <option value="" selected disabled>Select State</option>
    <option value="Andhra Pradesh">Andhra Pradesh</option>
    <option value="Arunachal Pradesh">Arunachal Pradesh</option>
    <option value="Assam">Assam</option>
    <option value="Bihar">Bihar</option>
    <option value="Chhattisgarh">Chhattisgarh</option>
    <option value="Goa">Goa</option>
    <option value="Gujarat">Gujarat</option>
    <option value="Haryana">Haryana</option>
    <option value="Himachal Pradesh">Himachal Pradesh</option>
    <option value="Jharkhand">Jharkhand</option>
    <option value="Karnataka">Karnataka</option>
    <option value="Kerala">Kerala</option>
    <option value="Madhya Pradesh">Madhya Pradesh</option>
    <option value="Maharashtra">Maharashtra</option>
    <option value="Manipur">Manipur</option>
    <option value="Meghalaya">Meghalaya</option>
    <option value="Mizoram">Mizoram</option>
    <option value="Nagaland">Nagaland</option>
    <option value="Odisha">Odisha</option>
    <option value="Punjab">Punjab</option>
    <option value="Rajasthan">Rajasthan</option>
    <option value="Sikkim">Sikkim</option>
    <option value="Tamil Nadu">Tamil Nadu</option>
    <option value="Telangana">Telangana</option>
    <option value="Tripura">Tripura</option>
    <option value="Uttar Pradesh">Uttar Pradesh</option>
    <option value="Uttarakhand">Uttarakhand</option>
    <option value="West Bengal">West Bengal</option>
  </select>
</div>

        
        <div class="form-group">
          <label for="city">City</label>
          <select id="city" name="city">
          <option value="" selected disabled>Select city</option>
        </select>

        </div>

        <div class="form-group">
          <label for="ownerImage">Owner Image</label>
          <input type="file" id="ownerImage" name="ownerImage" accept="image/*">
        </div>
      </div>

      <!-- Shop Section -->
      <div class="section">
        <h3>Shop Information</h3>

        <div class="form-group">
          <label for="shopName">Shop Name</label>
          <input type="text" id="shopName" name="shopName">
        </div>

        <div class="form-group">
          <label for="shopAddress">Shop Address</label>
          <textarea id="shopAddress" name="shopAddress" rows="2"></textarea>
        </div>
       

        <div class="form-group">
          <label for="shopImage">Shop Image</label>
          <input type="file" id="shopImage" name="shopImage"accept="image/*" >
        </div>

        <div class="form-group">
          <label for="licenseProof">License Proof</label>
          <input type="file" id="licenseProof" name="licenseProof"accept="image/*,.pdf" >
        </div>

        <div class="form-group">
          <label for="hours">Operating Hours</label>
          <input type="text" id="hours" name="hours" placeholder="e.g., 9AM - 6PM">
        </div>
      </div>
    </div>
   <div class="form-group d-flex align-items-center mt-3">
  <input type="checkbox" name="confirm" id="check" class="form-check-input" />
  <label for="check" class="form-check-label ms-2 mb-0">
    I agree to the 
    <a href="#" class="important" data-bs-toggle="modal" data-bs-target="#termsandpolicyModal">Terms and Conditions</a>
  </label>
</div>

    <div class="buttons">
      <button type="submit" class="register-btn" name="submit">Register</button>
      <button type="reset" class="cancel-btn">Cancel</button>
    </div>
    <p class="link">Already have an account?<a href="#" class="important"  data-bs-toggle="modal" data-bs-target="#mechanicLoginModal">Login</a></p>
        <p class="link2"><a href="#" class="terms"data-bs-toggle="modal" data-bs-target="#termsandpolicyModal">Terms & Privacy Policy</a></p>
  </form>
</div>






      
        
     

  

  <div class="modal fade" id="termsandpolicyModal" tabindex="-1" aria-labelledby="termsandpolicyModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="termsModalLabel">Terms & Privacy Policy</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">

        <h4>1. Introduction</h4>
        <p>These Terms and Conditions govern the registration  of mechanic shops in  RoadNova . By registering your shop, you agree to be bound by these Terms.</p>

        <h4>2. Registration Requirements</h4>
        <p>To register, mechanic shops must provide accurate and complete information, including shop details, business licenses, and contact information.</p>

        <h4>3. Shop Responsibilities</h4>
        <ul>
          <li>Respond promptly to breakdown requests.</li>
          <li>Ensure your staff provides professional and courteous service.</li>
          <li>Maintain high standards in all repair and support services.</li>
        </ul>

        <h4>4. Benefits</h4>
        <ul>
          <li>Access to a broader customer base through our network.</li>
          <li>Opportunities to provide breakdown assistance and grow your business.</li>
        </ul>

        <h4>5. Payment Terms</h4>
        <p>Mechanic shops are responsible for setting their own service rates. Payment terms with customers are handled independently by the shop.</p>

        <h4>6. Confidentiality and Data Protection</h4>
        <ul>
          <li>Maintain the confidentiality of customer information.</li>
          <li>Comply with all applicable data protection and privacy laws.</li>
        </ul>

        <h4>7. Termination</h4>
        <p>Either party may terminate this agreement with written notice. Termination may also occur due to violation of these Terms.</p>

        <h4>8. Liability</h4>
        <p>Mechanic shops are responsible for the quality of their services and any damages arising from their work.</p>

        <h4>9. Account Credentials</h4>
        <p>After successful verification of your shop's registration, your  password will be sent to your registered email address.</p>

        <h4>Privacy Policy for Mechanic Shop Registration</h4>

        <h4>1. Introduction</h4>
        <p>We are committed to protecting the privacy of our registered shops. This Privacy Policy explains how we collect, use, and safeguard your information.</p>

        <h4>2. Information Collection</h4>
        <ul>
          <li>We collect information provided during registration, such as shop name, licenses, owner details, and contact information.</li>
          <li>We may also collect data on how your shop interacts with our platform.</li>
        </ul>

        <h4>3. Use of Information</h4>
        <ul>
          <li>To facilitate your participation in the program.</li>
          <li>To notify you about breakdown requests, service updates, and account changes.</li>
        </ul>

        <h4>4. Data Sharing</h4>
        <p>We may share your shop's details with customers in need of assistance. We do not share your information with third parties without your consent, unless required by law.</p>

        <h4>5. Data Security</h4>
        <p>We implement reasonable security measures to protect your shops information from unauthorized access or misuse.</p>

        <h4>6. Your Rights</h4>
        <p>You have the right to request access to, correction of, or deletion of your shop's information at any time.</p>

        <h4>7. Changes to this Policy</h4>
        <p>We may update this Terms and Privacy Policy from time to time. All updates will be posted here and are effective immediately.</p>

        <p class="text-muted">Last updated: August 9, 2025</p>

      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
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

    </div>
  </div>
</div>

  <script>

 document.addEventListener("DOMContentLoaded", function () {
  const stateToCities = {
  "Andhra Pradesh": ["Amaravati", "Visakhapatnam", "Tirupati", "Vijayawada", "Guntur"],
  "Arunachal Pradesh": ["Itanagar", "Tawang", "Ziro", "Pasighat"],
  "Assam": ["Guwahati", "Dibrugarh", "Silchar", "Jorhat"],
  "Bihar": ["Patna", "Gaya", "Bhagalpur", "Muzaffarpur"],
  "Chhattisgarh": ["Raipur", "Bilaspur", "Durg", "Korba"],
  "Goa": ["Panaji", "Margao", "Vasco da Gama", "Mapusa"],
  "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot"],
  "Haryana": ["Chandigarh", "Faridabad", "Gurugram", "Panipat"],
  "Himachal Pradesh": ["Shimla", "Manali", "Dharamshala", "Solan"],
  "Jharkhand": ["Ranchi", "Jamshedpur", "Dhanbad", "Bokaro"],
  "Karnataka": ["Bengaluru", "Mysuru", "Mangaluru", "Hubli", "Chikkamagaluru", "Udupi"],
  "Kerala": ["Thiruvananthapuram", "Kochi", "Kozhikode", "Malappuram", "Palakkad", "Thrissur"],
  "Madhya Pradesh": ["Bhopal", "Indore", "Jabalpur", "Gwalior"],
  "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad"],
  "Manipur": ["Imphal", "Thoubal", "Bishnupur", "Churachandpur"],
  "Meghalaya": ["Shillong", "Tura", "Nongpoh", "Jowai"],
  "Mizoram": ["Aizawl", "Lunglei", "Champhai", "Serchhip"],
  "Nagaland": ["Kohima", "Dimapur", "Mokokchung", "Tuensang"],
  "Odisha": ["Bhubaneswar", "Cuttack", "Puri", "Rourkela"],
  "Punjab": ["Amritsar", "Ludhiana", "Jalandhar", "Patiala"],
  "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur", "Ajmer", "Bikaner"],
  "Sikkim": ["Gangtok", "Namchi", "Gyalshing", "Mangan"],
  "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Salem", "Thanjavur"],
  "Telangana": ["Hyderabad", "Warangal", "Nizamabad", "Karimnagar"],
  "Tripura": ["Agartala", "Udaipur", "Dharmanagar", "Kailasahar"],
  "Uttar Pradesh": ["Lucknow", "Kanpur", "Varanasi", "Agra", "Prayagraj"],
  "Uttarakhand": ["Dehradun", "Haridwar", "Nainital", "Rishikesh"],
  "West Bengal": ["Kolkata", "Howrah", "Durgapur", "Siliguri", "Asansol"]
};

 const stateSelect = document.getElementById("state");
  const citySelect = document.getElementById("city");

  stateSelect.addEventListener("change", function () {
    const selectedState = this.value;
    citySelect.innerHTML = '<option value="" disabled selected>Select city</option>';

    if (stateToCities[selectedState]) {
      stateToCities[selectedState].forEach(function (city) {
        const option = document.createElement("option");
        option.value = city;
        option.textContent = city;
        citySelect.appendChild(option);
      });
    }
  });
});

  function validateForm(event) {
     const name=document.getElementById("ownerName").value.trim();
     const dob=document.getElementById("dob").value.trim();
      const email = document.getElementById("ownerEmail").value.trim();
      const phone = document.getElementById("phone").value.trim();
      const genderOptions = document.getElementsByName("gender");
      const address = document.getElementById("address").value.trim();
      const adhar= document.getElementById("adharProof").value.trim();
      const state = document.getElementById("state").value.trim();
      const city= document.getElementById("city").value.trim();
      const image= document.getElementById("ownerImage").value.trim();
      const shop= document.getElementById("shopName").value.trim();
      const saddress= document.getElementById("shopAddress").value.trim();
      const simage= document.getElementById("shopImage").value.trim();
      const license= document.getElementById("licenseProof").value.trim();
      const hours= document.getElementById("hours").value.trim();
      const check = document.getElementById("check").checked;

      if (name === "" || !/^[a-zA-Z\s]+$/.test(name)) {
        alert("Please enter a valid full name (letters only).");
        return false;
      }
       if (dob === "") {
        alert("Please select your date of birth.");
        return false;
      }

      const birthDate = new Date(dob);
      const today = new Date();
      let age = today.getFullYear() - birthDate.getFullYear();
      if (today < new Date(today.getFullYear(), birthDate.getMonth(), birthDate.getDate())) {
        age--;
      }

      if (age < 18) {
        alert("You must be at least 18 years old to register.");
        return false;
      }
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(email)) {
        alert("Please enter a valid email address.");
        return false;
      }
       if (!/^[6-9]\d{9}$/.test(phone)) {
  alert("Please enter a valid 10-digit Indian mobile number starting with 6, 7, 8, or 9.");
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

       if (address === "") {
        alert("Please enter your address.");
        return false;
      }
     if (!adhar) {
    alert("Please upload Aadhar proof.");
    return false;
     }
     if (state === "") {
        alert("Please enter your state.");
        return false;
      }
     if (city === "") {
        alert("Please enter your city.");
        return false;
      }
     if (!image) {
    alert("Please upload your passport size photo.");
    return false;
     }
     if (shop === "") {
        alert("Please enter your shop name.");
        return false;
      }
    if (saddress === "") {
        alert("Please enter your shop address.");
        return false;
      }
    
     if (!simage) {
        alert("Please upload your shop image.");
        return false;
      }
     if (!license) {
        alert("Please upload your license proof.");
        return false;
      }
      if (hours ==="") {
        alert("Please enter your working hours.");
        return false;
      }

     

      if (!check) {
        alert("You must agree to the Terms and Conditions.");
        return false;
      }
  return true;
}
  </script>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

""")
form = cgi.FieldStorage()
owner_name = form.getvalue("ownerName")
dob = form.getvalue("dob")
owner_mail = form.getvalue("ownerEmail")
phone = form.getvalue("phone")
gender = form.getvalue("gender")
address = form.getvalue("address")
state = form.getvalue("state")
city = form.getvalue("city")
shop_name = form.getvalue("shopName")
shop_address = form.getvalue("shopAddress")
hours = form.getvalue("hours")
confirm = form.getvalue("confirm")

Submit = form.getvalue("submit")



if Submit is not None:
    Image = form['ownerImage']
    Adhar = form['adharProof']
    Shopi = form['shopImage']
    License = form['licenseProof']
    fn = os.path.basename(Image.filename)

    aimage = os.path.basename(Adhar.filename)
    simage = os.path.basename(Shopi.filename)
    limage = os.path.basename(License.filename)
    open("images/" + fn, "wb").write(Image.file.read())
    open("images/" + aimage, "wb").write(Adhar.file.read())

    open("images/" + simage, "wb").write(Shopi.file.read())

    open("images/" + limage, "wb").write(License.file.read())
    q = """INSERT INTO mechanicshops(owner_name, dob, gender, phone, address, adhar_proof, state, city, owner_image, shop_name, shop_address, shop_image, license_proof, operating_hours, owner_email) 
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    cur.execute(q, (
    owner_name, dob, gender, phone, address, aimage, state, city, fn, shop_name, shop_address, simage, limage, hours,
    owner_mail))


    con.commit()

    print("""
        <script>
          alert("Registration successful! Your  password will be sent to your email.");
        </script>
        """)
