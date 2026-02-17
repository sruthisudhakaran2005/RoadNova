#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

import cgi, cgitb
import pymysql
import html

cgitb.enable()
print("Content-type: text/html\n")
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
form = cgi.FieldStorage()
service_id = form.getvalue("id")
q = "SELECT * FROM services WHERE service_id = %s"
cur.execute(q, (service_id,))
res = cur.fetchone()

if res:
    shop_id = res[1]
else:
    error_msg = "Invalid service request ID."
    shop_id = None  # To avoid further errors


# Variables to hold service data and messages
service_name = ""
price = ""
error_msg = ""
success_msg = ""

if not service_id:
    error_msg = "Service ID not provided."
else:
    try:
        con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
        cur = con.cursor()
        if form.getvalue("service_name") and form.getvalue("price"):
            new_name = form.getvalue("service_name")
            new_price = form.getvalue("price")

            if not new_name or not new_price:
                error_msg = "Please fill in all fields."
            else:
                try:
                    new_price_float = float(new_price)
                    update_query = "UPDATE services SET service_name=%s, price=%s WHERE service_id=%s"
                    cur.execute(update_query, (new_name, new_price_float, service_id))
                    con.commit()
                    success_msg = "Service updated successfully."
                    service_name = new_name
                    price = new_price
                except ValueError:
                    error_msg = "Price must be a valid number."
                except Exception as e:
                    error_msg = f"Database error: {str(e)}"

        if not success_msg:
            # Fetch existing service details if no successful update yet
            select_query = "SELECT service_name, price FROM services WHERE service_id=%s"
            cur.execute(select_query, (service_id,))
            row = cur.fetchone()
            if row:
                service_name, price = row
            else:
                error_msg = "Service not found."

        con.close()

    except Exception as e:
        error_msg = f"Error: {str(e)}"

print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Edit Service</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" />
  <style>
    body {{
      background-color: #e6f0ff;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      padding: 40px 20px;
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: flex-start;
    }}
    .edit-container {{
      background: white;
      max-width: 480px;
      width: 100%;
      padding: 30px 25px;
      border-radius: 14px;
      box-shadow: 0 6px 16px rgba(58, 102, 204, 0.15);
    }}
    h2 {{
      color: #3a66cc;
      margin-bottom: 25px;
      text-align: center;
      font-weight: 700;
    }}
    label {{
      font-weight: 600;
      color: #2a4d99;
    }}
    input[type="text"],
    input[type="number"] {{
      width: 100%;
      padding: 10px 12px;
      margin-top: 6px;
      margin-bottom: 18px;
      border: 2px solid #5a86e6;
      border-radius: 10px;
      font-size: 1rem;
      transition: border-color 0.3s;
    }}
    input[type="text"]:focus,
    input[type="number"]:focus {{
      border-color: #3a66cc;
      outline: none;
      box-shadow: 0 0 8px rgba(58, 102, 204, 0.4);
    }}
    .btn-submit {{
      background-color: #3a66cc;
      border: none;
      color: white;
      padding: 12px 0;
      width: 100%;
      font-size: 1.1rem;
      font-weight: 700;
      border-radius: 10px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }}
    .btn-submit:hover {{
      background-color: #2a4d99;
    }}
    .message {{
      margin-bottom: 20px;
      padding: 10px 14px;
      border-radius: 10px;
      font-weight: 600;
      text-align: center;
    }}
    .error {{
      background-color: #ffd6d6;
      color: #b32e2e;
      border: 1px solid #b32e2e;
    }}
    .success {{
      background-color: #d6f0d6;
      color: #2b7a2b;
      border: 1px solid #2b7a2b;
    }}

    @media (max-width: 520px) {{
      body {{
        padding: 20px 15px;
      }}
      .edit-container {{
        padding: 25px 20px;
      }}
    }}
  </style>
</head>
<body>
  <div class="edit-container">
    <h2>Edit Service</h2>
""")

# Display error or success messages
if error_msg:
    print(f'<div class="message error">{html.escape(error_msg)}</div>')

if success_msg:
    print(f'''
    <div class="message success">{html.escape(success_msg)}</div>
    <script>
      setTimeout(function() {{
        window.location.href = "view_services.py?id={shop_id}";
      }}, 1000);  
    </script>
    ''')


# Form
print(f"""
    <form method="post" action="edit_service.py?id={service_id}">
      <label for="service_name">Service Name</label>
      <input type="text" id="service_name" name="service_name" value="{html.escape(service_name)}" required />

      <label for="price">Price (₹)</label>
      <input type="number" id="price" name="price" step="0.01" min="0" value="{price}" required />

      <button type="submit" name="submit" class="btn-submit">Update Service</button>
    </form>
  </div>
</body>
</html>
""")
