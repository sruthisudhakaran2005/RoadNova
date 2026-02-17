#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')
print("content-type:text/html \r\n\r\n")

import cgi, cgitb
cgitb.enable()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forgot Password</title>

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">

    <style>
        body {
            font-family: 'Roboto', sans-serif;
        }

        .overlay {
            background-color: rgba(255, 255, 255, 0.9);
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
        }

        .navbar {
            background-color: #ffffff;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .navbar-brand {
            font-weight: bold;
            color: #ff4500;
        }

        .navbar-brand:hover {
            color: #c0392b;
        }

        .nav-link {
            color: #333;
            font-weight: 500;
        }

        .nav-link:hover {
            color: #007bff;
        }

        .form-container {
            max-width: 500px;
            margin: 100px auto;
            padding: 30px 40px;
            background-color: #ffffff;
            border-radius: 15px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
            animation: fadeIn 1.2s ease-in-out;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .form-container h2 {
            text-align: center;
            margin-bottom: 20px;
            color: #333;
        }

        .form-container p {
            text-align: center;
            color: #666;
        }

        .form-control {
            border-radius: 8px;
            padding: 12px;
        }

        .btn-primary {
            background-color: #ff4500;
            border-color: #ff4500;
            width: 100%;
            padding: 12px;
            font-size: 16px;
            border-radius: 8px;
        }

        .btn-primary:hover {
            background-color: #e03e00;
            border-color: #e03e00;
        }
        
    </style>
</head>
<body>

    <div class="overlay"></div>

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
        <div class="form-container">
        <h2>Mechanic Shops</h2>
            <h2><i class="fas fa-unlock-alt me-2 text-danger"></i>Forgot Password</h2>
            <p>Enter your email address to request a new password.</p>
            <form action="verify_send_password.py" method="post">
                <div class="mb-3">
                    <label for="email" class="form-label">Email Address</label>
                    <input type="email" class="form-control" id="email" name="email" required>
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
    </div>
   
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>
""")
