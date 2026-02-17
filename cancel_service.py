#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-

import cgi, cgitb, pymysql, sys, smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')
cgitb.enable()

print("Content-Type: text/html\r\n")

form = cgi.FieldStorage()
request_id = form.getvalue("request_id")

# Connect to DB
try:
    con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
    cur = con.cursor()
except pymysql.MySQLError as e:
    print(f"<h3>Database connection failed: {e}</h3>")
    sys.exit()

# Get shop details from service_requests
cur.execute("SELECT shop_id FROM service_requests WHERE request_id = %s", (request_id,))
r = cur.fetchone()
if not r:
    print("<h3>Error: Request not found.</h3>")
    con.close()
    sys.exit()

shop_id = r[0]
cur.execute("SELECT shop_name, owner_email FROM mechanicshops WHERE id = %s", (shop_id,))
shop_data = cur.fetchone()
if not shop_data:
    print("<h3>Error: Shop not found.</h3>")
    con.close()
    sys.exit()

shop_name, sho_mail = shop_data

# Get user details and payment info
cur.execute("SELECT user_id, total_charge, payment_status FROM service_requests WHERE request_id = %s", (request_id,))
res = cur.fetchone()
if not res:
    print("<h3>Error: Invalid service request.</h3>")
    con.close()
    sys.exit()

user_id, total_charge, payment_status = res
total_charge = float(total_charge)

cur.execute("SELECT name, email FROM users WHERE user_id = %s", (user_id,))
user_info = cur.fetchone()
if not user_info:
    print("<h3>Error: User not found.</h3>")
    con.close()
    sys.exit()

user_name, email = user_info

try:
    fromadd = 'sruthisudhakaran2005@gmail.com'
    ppasswod = 'trng sjeu embt htce'  # Use App Password securely

    # === Case 1: Prepaid Booking (status: 'Paid') ===
    if total_charge > 0 and payment_status.lower() == 'paid':
        refund_amount = round(total_charge * 0.75, 2)
        deducted_amount = round(total_charge - refund_amount, 2)

        # Corrected UPDATE statement
        # This updates status, sets the refund amount, and uses NOW() for the date.
        # It does NOT change the original total_charge.
        cur.execute("""
            UPDATE service_requests
            SET status = %s, refund = %s, cancelled_date = NOW(), refund_status = 'Pending'
            WHERE request_id = %s
        """, ("Cancelled", refund_amount, request_id))
        con.commit()

        subject_customer = "Your service cancellation has been processed - RoadNova"
        body_customer = f"""Dear {user_name},

We have successfully processed your request to cancel your service booking.

📌 As per our cancellation policy, 25% of the service charge has been deducted.  
Original Service Charge: ₹{total_charge}
Refund Amount: ₹{refund_amount}  
Deducted Amount: ₹{deducted_amount}

The remaining 75% will be refunded to your original payment method within 5–7 business days.

Thank you for choosing RoadNova.

Regards,  
Team RoadNova"""

        alert_message = f"Booking cancelled successfully. {deducted_amount} deducted, {refund_amount} will be refunded."

    # === Case 2: Unpaid Booking ===
    else:
        # Update status for unpaid bookings. No refund is needed.
        cur.execute("""
            UPDATE service_requests
            SET status = %s
            WHERE request_id = %s
        """, ("Cancelled", request_id))
        con.commit()

        subject_customer = "Your service booking cancellation - RoadNova"
        body_customer = f"""Dear {user_name},

Your service booking has been successfully cancelled.

ℹ️ No payment was made for this booking, so there is no amount to refund.

If you need further help or wish to rebook, feel free to contact us anytime.

Thank you for choosing RoadNova.

Regards,  
Team RoadNova"""

        alert_message = "Booking cancelled successfully. No amount to be refunded."

    # === Send Email to Customer ===
    msg_customer = MIMEText(body_customer, 'plain', 'utf-8')
    msg_customer['Subject'] = Header(subject_customer, 'utf-8')
    msg_customer['From'] = formataddr(("RoadNova", fromadd))
    msg_customer['To'] = email

    # === Send Email to Shop ===
    subject_shop = "Service Booking Cancelled - RoadNova"
    body_shop = f"""Dear {shop_name},

This is to inform you that the following service booking has been cancelled by the customer:

📄 Booking ID: {request_id}
👤 Customer Name: {user_name}
✉️ Customer Email: {email}

Please update your records accordingly.

Thank you,
RoadNova Support Team"""

    msg_shop = MIMEText(body_shop, 'plain', 'utf-8')
    msg_shop['Subject'] = Header(subject_shop, 'utf-8')
    msg_shop['From'] = formataddr(("RoadNova", fromadd))
    msg_shop['To'] = sho_mail

    # === Send Emails ===
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(fromadd, ppasswod)
    server.sendmail(fromadd, [email], msg_customer.as_string())
    server.sendmail(fromadd, [sho_mail], msg_shop.as_string())
    server.quit()

    # === JS Alert & Redirect ===
    print(f"""
    <script>
    alert("{alert_message}");
    window.top.location.href="approved_booking.py?user_id={user_id}";
    </script>
    """)

except Exception as e:
    print(f"""
    <html><body>
    <h3>Error cancelling booking: {str(e)}</h3>
    <a href="approved_booking.py?user_id={user_id}">Back to Bookings</a>
    </body></html>
    """)

finally:
    if con:
        con.close()