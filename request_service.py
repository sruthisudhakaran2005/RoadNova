#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
import sys
sys.stdout.reconfigure(encoding='utf-8')
print("Content-Type: text/html\r\n\r\n")

import pymysql, smtplib
import cgi
import cgitb
cgitb.enable()

try:
    con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
    cur = con.cursor()

    form = cgi.FieldStorage()
    user_id = form.getvalue("user_id")
    shop_id = form.getvalue("shop_id")
    service_name = form.getvalue("service_name")
    vehicle_type = form.getvalue("vehicle_type")
    vehicle_brand = form.getvalue("vehicle_brand")
    registration_number = form.getvalue("registration_number")
    location = form.getvalue("user_location")
    name = form.getvalue("shop_name")
    email = form.getvalue("email")
    cur.execute("SELECT name FROM users WHERE user_id = %s", (user_id,))
    res = cur.fetchone()
    if res is not None:
        user_name = res[0]
    if user_id and shop_id and service_name:
        query = """
            INSERT INTO service_requests (user_id, shop_id, problem_type, status, payment_status, location, vehicle_type, vehicle_brand, reg_no  )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (user_id, shop_id, service_name, "Pending", "Pending", location, vehicle_type, vehicle_brand, registration_number))
        con.commit()
        fromadd = 'sruthisudhakaran2005@gmail.com'
        ppasswod = 'trng sjeu embt htce'
        toadd = email
        subject = " New Service Request Received from roadnova"
        body = """hello %s,
         You have received a new service request from a customer. Please review the details and take the necessary steps to follow up.
         Request Details:
        
        *Customer Name:%s
        *Issue :%s
        *Vehicle Type :%s
       
        Please log in to your dashboard to view the full request and respond to the customer as soon as possible.
        If you have any questions or need assistance, feel free to reach out to our support team.

        Best regards,
        Support Team RoadNova """ % (name, user_name, service_name, vehicle_type)
        msg = """Subject:%s \n\n%s """ % (subject, body)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(fromadd, ppasswod)
        server.sendmail(fromadd, toadd, msg)
        server.quit()

        print(f"""
        <html>
        <head>
            <title>Service Request Submitted</title>
            <meta http-equiv="refresh" content="3;url=approved_booking.py?user_id={user_id}">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f8f9fa;
                    text-align: center;
                    padding: 50px;
                }}
                .msg {{
                    background-color: #d1e7dd;
                    color: #0f5132;
                    padding: 20px;
                    margin: 50px auto;
                    width: 60%;
                    border: 1px solid #badbcc;
                    border-radius: 8px;
                    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
                }}
            </style>
        </head>
        <body>
            <div class="msg">
                <h2>Service Request Submitted Successfully!</h2>
            </div>
        </body>
        </html>
        """)
    else:
        print("<h3 style='color:red;'>Missing required fields. Please go back and try again.</h3>")

except Exception as e:
    print(f"""
        <script>
        alert("mail not send check your internet");
        window.top.location.href="user.py?user_id={user_id}"
        </script>
        """)


finally:
    try:
        con.close()
    except:
        pass
