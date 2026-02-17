#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import pymysql
from datetime import datetime
import smtplib
import sys

sys.stdout.reconfigure(encoding='utf-8')
print("Content-Type: text/html\n")

form = cgi.FieldStorage()

# -------------------------------
# ✅ Input validation functions
# -------------------------------
def get_float_field(field_name):
    raw_value = form.getvalue(field_name)
    if raw_value is None or raw_value.strip() == "":
        print(f"<script>alert('Missing or empty value for {field_name}');</script>")
        exit()
    try:
        return float(raw_value)
    except ValueError:
        print(f"<script>alert('Invalid number for {field_name}');</script>")
        exit()

def get_str_field(field_name):
    val = form.getvalue(field_name)
    if val is None or val.strip() == "":
        print(f"<script>alert('Missing value for {field_name}');</script>")
        exit()
    return val.strip()

# -------------------------------
# ✅ Get and validate form data
# -------------------------------
shop_id = get_str_field("shop_id")
request_id = get_str_field("request_id")

name = get_str_field("name")
email = get_str_field("email")
service_charge = get_float_field("service_charge")
extra_charge = get_float_field("extra_charge")
total_charge = get_float_field("total_charge")
amount = round(total_charge * 0.75, 2)

# -------------------------------
# ✅ Database operations
# -------------------------------
try:
    con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
    cur = con.cursor()

    # Secure query for shop name
    cur.execute("SELECT shop_name FROM mechanicshops WHERE id=%s", (shop_id,))
    res = cur.fetchone()

    if res is None:
        print("<script>alert('Shop not found');</script>")
        exit()

    shop_name = res[0]

    # Update refund status
    cur.execute("""
        UPDATE service_requests
        SET refund_status = %s, refund_date = %s
        WHERE request_id = %s
    """, ("Paid", datetime.now(), request_id))
    con.commit()

    print("""
    <script>
        alert("Refund successfully completed");
    </script>
    """)

    # -------------------------------
    # ✅ Email sending (format unchanged)
    # -------------------------------
    fromadd = 'sruthisudhakaran2005@gmail.com'
    ppasswod = 'trng sjeu embt htce'  # ⚠️ Move to environment variable in production
    toadd = email
    subject = "Refund Processed - RoadNova"
    body = f"""
Dear {name},

Your refund request for the service has been successfully processed.

Details:
----------------------------------
Shop Name          : {shop_name}
Service Charge     : {service_charge}
Extra Charge       : {extra_charge}
Total Paid Amount  : {total_charge}
Refund Amount (75%): {amount}
Refund Status      : Paid

Refund Date & Time : {datetime.now().strftime('%d-%b-%Y %I:%M %p')}

We apologize for any inconvenience caused.

Thank you for choosing RoadNova.

Best regards,
RoadNova Team
"""

    msg = """Subject:%s \n\n%s""" % (subject, body)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(fromadd, ppasswod)
        server.sendmail(fromadd, toadd, msg)
        server.quit()

        print(f"""
            <script>
                alert("Mail sent successfully");
                window.top.location.href="current.py?id={shop_id}";
            </script>
        """)

    except Exception as e:
        print(f"""
            <script>
                alert("Failed to send email: {str(e)}");
                window.top.location.href="current.py?id={shop_id}";
            </script>
        """)

except Exception as e:
    print(f"<script>alert('Error: {str(e)}');</script>")
finally:
    if 'con' in locals():
        con.close()
