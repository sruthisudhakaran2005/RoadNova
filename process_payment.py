#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe

print("Content-Type: text/html\r\n\r\n")

import pymysql
import cgi
import cgitb
import smtplib
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import io
import html # Added the html module

# Enable CGI traceback for debugging
cgitb.enable()

# Handle Unicode output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()
user_id = form.getvalue("user_id")
request_id = form.getvalue("request_id")
amount = form.getvalue("amount")
payment_method = form.getvalue("payment_method")
shop_id = form.getvalue("shop_id")

# Validate required fields
if not all([user_id, request_id, amount, payment_method, shop_id]):
    print(f"""
    <!DOCTYPE html>
    <html><head><title>Error</title></head><body>
    <h3>Error: Missing form data.</h3>
    <h3>Values received: user_id={user_id}, request_id={request_id}, amount={amount}, payment_method={payment_method}, shop_id={shop_id}</h3>
    </body></html>
    """)
    sys.exit()

try:
    con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
    cur = con.cursor()

    # Check if it's a first or second payment
    cur.execute("SELECT type FROM payments WHERE service_id = %s", (request_id,))
    res = cur.fetchone()
    payment_type = 'second' if res and res[0] else 'first'

    # Get price and extra_charge
    cur.execute("SELECT price, extra_charge FROM service_requests WHERE request_id = %s", (request_id,))
    price_data = cur.fetchone()
    if not price_data:
        raise Exception("Service request not found.")

    price, extra_charge = price_data
    extra_charge = extra_charge or 0.0
    amount_float = float(amount)

    # Update payment status
    # Determine payment status based on amount and method
    if abs(amount_float - float(price)) < 0.01:
        status = 'On Hand' if payment_method.lower() == 'cash' else 'Paid'
        cur.execute("UPDATE service_requests SET payment_status = %s WHERE request_id = %s", (status, request_id))
    elif abs(amount_float - float(extra_charge)) < 0.01:
        status = 'On Hand' if payment_method.lower() == 'cash' else 'Paid'
        cur.execute("UPDATE service_requests SET extra_charge_status = %s WHERE request_id = %s", (status, request_id))
    else:
        raise Exception("Amount does not match the service cost or extra charge.")

    # Insert into payments table
    insert_query = """
        INSERT INTO payments (shop_id, service_id, user_id, amount, method, paid_on, type)
        VALUES (%s, %s, %s, %s, %s, NOW(), %s)
    """
    cur.execute(insert_query, (shop_id, request_id, user_id, amount, payment_method, payment_type))


    cur.execute("SELECT name, email FROM users WHERE user_id = %s", (user_id,))
    user_info = cur.fetchone()
    if not user_info:
        raise Exception("User not found.")

    name, email = user_info

    con.commit()

    # Email setup
    fromadd = 'sruthisudhakaran2005@gmail.com'
    ppassword = 'trng sjeu embt htce'
    toadd = email
    subject = "Payment Successful - RoadNova"
    body = f"""
Dear {name},

Thank you for your payment of ₹{amount} for service request ID #{request_id}.

Payment Method: {payment_method}

Regards,
RoadNova Team
"""

    # Compose and send email
    message = MIMEMultipart()
    message['From'] = fromadd
    message['To'] = toadd
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(fromadd, ppassword)
    server.send_message(message)
    server.quit()

    # On success
    print(f"""
    <script>
        alert("Payment successful.");
        window.top.location.href="approved_booking.py?user_id={user_id}";
    </script>
    """)

except Exception as e:
    if 'con' in locals() and con:
        con.rollback()

    error_details = traceback.format_exc()
    print(f"""
    <script>
    alert("mail not send check your internet");
    window.top.location.href="user.py?user_id={user_id}"
    </script>
    """)

finally:
    if 'con' in locals() and con:
        con.close()