# RoadNova – 24/7 On-Road Vehicle Breakdown Assistance

**RoadNova** is a web-based emergency roadside assistance system designed to help vehicle owners get quick help during breakdowns.  
Users can request assistance instantly by locating the **nearest mechanic shop** based on their current location.


## Main Features
- User registration & login
- Mechanic/shop registration & login
- **Location-based nearest mechanic shop finder**
- Request breakdown assistance / emergency service
- Real-time request status tracking (pending, approved, in-progress, completed, cancelled)
- Admin dashboard for managing requests & shops
- Mechanic dashboard for accepting/rejecting jobs
- OTP verification for secure login & password reset
- Notifications for request updates
- Payment processing for service charges

## Technologies Used
- **Backend**: Python (CGI scripts)
- **Database**: MySQL (running on XAMPP)
- **Frontend**: HTML, CSS, JavaScript (with browser Geolocation API for location)
- **Server**: Apache + MySQL (XAMPP local server)

## How to Run Locally
1. Install **XAMPP** (Apache + MySQL)
2. Start Apache and MySQL modules in XAMPP control panel
3. Copy this entire project folder to:  
   `C:\xampp\htdocs\roadnova`  
   (or rename the folder to match your preferred name)
4. (If you have `database.sql`)  
   Open http://localhost/phpmyadmin  
   → Create a new database (e.g. `roadnova_db`)  
   → Import your `database.sql` file
5. Update database connection details in your `.py` files  
   (usually: host='localhost', user='root', password='', db='roadnova_db')
6. Open in browser:  
   http://localhost/roadnova/home.py  
   (or your main entry file like `index.py` / `user_login.py`)

**Important**: Allow location access when prompted in the browser for the "nearest shop" feature to work.

## Project Notes
- This project uses classic **Python CGI** + XAMPP (great for learning and college projects)
- For modern production use, consider migrating to Flask / Django + a proper web server + frontend framework (React/Vue)
- Location is calculated using **Haversine formula** (straight-line distance) based on latitude/longitude

## Future Improvements (Ideas)
- SMS/email notifications
- Mobile-responsive design
- Shop ratings & reviews


Feel free to contribute, fork, or use it for learning! 🚗💨

Sruthi  
Palakkad, Kerala  
February 2026