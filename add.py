#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os
from datetime import datetime

cgitb.enable()
form = cgi.FieldStorage()

con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
id = form.getvalue("id")
q = """SELECT * FROM mechanicshops WHERE id=%s"""
cur.execute(q, (id,))

res = cur.fetchall()


for i in res:
    profile_img = i[9]
    shop_name = i[10]
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <title>Add Mechanic | RoadNova</title>
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
    z-index: 1051; /* Make it sit on top of everything */
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
    """)
    print(f"""
    <body>
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
        <!-- Sidebar -->
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
    """)

    print(f"""
    <div id="addMechanic" class="content-section">
      <div class="form-container">
      <h2>Add Mechanics</h2>
        <form method="POST" enctype="multipart/form-data" onsubmit="return add(event)">
          <div class="row">
            <input type="hidden" value="{id}" name="shop_id">

            <div class="col-md-6">
              <label for="name">Full Name</label>
              <input type="text" id="name" name="name" >
            </div>

            <div class="col-md-6">
              <label for="dob">DOB</label>
              <input type="date" id="dob" name="dob" class="form-control">
            </div>

            <div class="col-md-6">
              <label for="gender">Gender</label><br>
              <input type="radio" id="male" name="gender" value="Male"> Male
              <input type="radio" id="female" name="gender" value="Female"> Female
              <input type="radio" id="other" name="gender" value="Other"> Other
            </div>

            <div class="col-md-6">
              <label for="phone">Phone Number</label>
              <input type="tel" id="phone" name="phone" >
            </div>

            <div class="col-md-6">
              <label for="email">Email</label>
              <input type="email" id="email" name="email" >
            </div>

            <div class="col-md-6">
              <label for="address">Address</label>
              <textarea id="address" name="address" rows="2" ></textarea>
            </div>

            <div class="col-md-6">
              <label for="specialization">Specialization</label>
              <select id="specialization" name="specialization" >
                <option value="">-- Select Specialization --</option>
                <option value="engine">Engine Repair</option>
                <option value="transmission">Transmission</option>
                <option value="brakes">Brakes</option>
                <option value="electrical">Electrical</option>
                <option value="general">General Maintenance</option>
              </select>
            </div>

            <div class="col-md-6">
              <label for="experience">Experience (in years)</label>
              <input type="number" id="experience" name="experience" >
            </div>

            <div class="col-md-6">
              <label for="image">Mechanic Photo</label>
              <input type="file" id="image" name="image" >
            </div>

            <div class="col-md-6">
              <label for="idproof">ID Proof</label>
              <input type="file" id="idproof" name="idproof" >
            </div>

            <div class="col-md-12">
              <input type="submit" value="Add Mechanic" name="submit">
            </div>
          </div>
        </form>
      </div>
    </div>
    </main>
    """)
    print("""
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
    function add(event) {
         const name=document.getElementById("name").value.trim();
         const dob=document.getElementById("dob").value.trim();
          const email = document.getElementById("email").value.trim();
          const phone = document.getElementById("phone").value.trim();
          const genderOptions = document.getElementsByName("gender");
          const address = document.getElementById("address").value.trim();
          const specialization = document.getElementById('specialization').value;
          const experience= document.getElementById("experience").value.trim();
          const image= document.getElementById("image").value.trim();
          const adhar= document.getElementById("idproof").value.trim();


          if (name === "" || !/^[a-zA-Z\s]+$/.test(name)) {
            alert("Please enter a valid full name .");
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
           if (!/^\d{10}$/.test(phone)) {
            alert("Please enter a valid 10-digit phone number.");
            return false;
          }
          const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          if (!emailPattern.test(email)) {
            alert("Please enter a valid email address.");
            return false;
          }



           if (address === "") {
            alert("Please enter your address.");
            return false;
          }
          if ( specialization=== "") {
            alert("Please select specialization.");
            return false;
          }
          if ( experience==="") {
            alert("Please enter your experience.");
            return false;
          }
           if (!image) {
        alert("Please upload your passport size photo.");
        return false;
         }
         if (!adhar) {
        alert("Please upload Aadhar proof.");
        return false;
         }



      return true;
    }

    </script>
    """)
    print("""
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """)



if form.getvalue("submit"):
    name = form.getvalue("name")
    dob = form.getvalue("dob")
    gender = form.getvalue("gender")
    phone = form.getvalue("phone")
    mail = form.getvalue("email")
    address = form.getvalue("address")
    special = form.getvalue("specialization")
    experience = form.getvalue("experience")

    # ✅ Handle file uploads
    def save_file(field_item, folder):
        if field_item.filename:
            if not os.path.exists(folder):
                os.makedirs(folder)
            filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{os.path.basename(field_item.filename)}"
            filepath = os.path.join(folder, filename)
            with open(filepath, 'wb') as f:
                f.write(field_item.file.read())
            return filename
        return ""

    image_file = form['image']
    idproof_file = form['idproof']

    image_filename = save_file(image_file, "uploads/photos")
    idproof_filename = save_file(idproof_file, "uploads/idproofs")

    query = """
        INSERT INTO mechanics (name, phone, mail, address, specialization, experience, dob, gender, shop_id, image, idproof)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (name, phone, mail, address, special, experience, dob, gender, id, image_filename, idproof_filename)
    cur.execute(query, values)
    con.commit()

    print(f"""
    <script>
      alert("Mechanic added successfully!");
      window.location.href = "add.py?id={id}";
    </script>
    """)
