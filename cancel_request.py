#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-

import pymysql, cgi, cgitb, smtplib
from email.message import EmailMessage
from decimal import Decimal

print("Content-Type: text/html; charset=utf-8\r\n\r\n")

cgitb.enable()
form = cgi.FieldStorage()

# Get form values
request_id = form.getvalue('request_id')
email = form.getvalue('email')
customer_name = form.getvalue('customer_name')
shop_id = form.getvalue('shop_id')

# DB Connection
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()

try:
    # Fetch service request details
    cur.execute("""
        SELECT price, total_charge, payment_status, extra_charge_status, problem_type, request_date
        FROM service_requests 
        WHERE request_id = %s
    """, (request_id,))
    row = cur.fetchone()

    if not row:
        # No request found
        print("""
            <script>
                alert("Service request not found.");
                window.history.back();
            </script>
        """)
    else:
        price, total_charge, payment_status, extra_charge_status, problem_type, request_date = row

        # Convert to Decimal for safe calculation
        refund_base = Decimal('0.00')

        if payment_status and payment_status.lower() == 'paid':
            if extra_charge_status and extra_charge_status.lower() == 'paid':
                refund_base = Decimal(str(total_charge))
            else:
                refund_base = Decimal(str(price))

        refund_amount = round(refund_base * Decimal('0.75'), 2)

        # Update service request with refund info
        cur.execute("""
            UPDATE service_requests 
            SET status = 'Cancelled', refund = %s, refund_date = NOW()
            WHERE request_id = %s;
        """, (str(refund_amount), request_id))
        con.commit()

        fromadd = 'sruthisudhakaran2005@gmail.com'
        ppasswod = 'trng sjeu embt htce'
        toadd = email
        subject = "Service Cancellation Confirmation & Refund Details"
        body = f"""
        Dear {customer_name},

        As per your request, we have cancelled your service booking.

        Below are the details of your refund:

        --------------------------------------------------
         Problem Type       : {problem_type}
         Booked On          : {request_date.strftime('%d-%b-%Y %I:%M %p')}
         Original Amount    : {refund_base}
         Refund Percentage  : 75%
         Refunded Amount    : {refund_amount}
         Reason      : As per customer request, we cancelled the service.
        --------------------------------------------------

        The refund will reflect in your account shortly, depending on your payment method.

        If you have any questions, feel free to contact us.

        Thank you for choosing RoadNova.

        Best regards,  
         RoadNova Team
                """
        msg = """Subject:%s \n\n%s""" % (subject, body)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(fromadd, ppasswod)
        server.sendmail(fromadd, toadd, msg)
        server.quit()


        print(f"""
            <script>
                alert("Service cancelled. Refund {refund_amount} initiated. mail send sucessfully");
                window.location.href = "current.py?id={shop_id}";
            </script>
        """)

except Exception as general_error:
    print(f"""
                <script>
                    alert(" An error occur mail is not send.");
                    window.location.href = "current.py?id={shop_id}";
                </script>
            """)

finally:
    con.close()
