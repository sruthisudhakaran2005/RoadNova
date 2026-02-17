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
    <title>Forgot Password | RoadNova</title>

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">

    <style>
        body {
            font-family: 'Roboto', sans-serif;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
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

        .container {
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            padding-top: 60px;
            padding-bottom: 40px;
        }

        .form-container {
            width: 100%;
            max-width: 450px;
            background-color: #ffffff;
            border-radius: 15px;
            padding: 40px 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            animation: fadeIn 0.8s ease-in-out;
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
            margin-bottom: 25px;
        }

        .form-control {
            border-radius: 10px;
            padding: 12px;
        }

        .btn-primary {
            background-color: #ff5722;
            border: none;
            width: 100%;
            padding: 12px;
            border-radius: 10px;
            font-size: 16px;
        }

        .btn-primary:hover {
            background-color: #e64a19;
        }
    </style>
</head>
<body>

    <!-- ✅ Navbar -->
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

    <!-- ✅ Forgot Password Form -->
    <div class="container">
        <div class="form-container">
        <h2>USER</h2>
            <h2><i class="fas fa-unlock-alt text-warning me-2"></i>Forgot Password?</h2>
            <p>Enter your registered email to receive an OTP.</p>
            <form action="send_otp.py" method="post">
                <div class="mb-3">
                    <label for="email" class="form-label">Email Address</label>
                    <input type="email" class="form-control" id="email" name="email"  >
                </div>
                <button type="submit" class="btn btn-primary">Send OTP</button>
            </form>
        </div>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>
""")
