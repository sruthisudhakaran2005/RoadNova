#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
import sys
import cgi
import cgitb
import pymysql

# Enable detailed error reporting for development
cgitb.enable()

# Print the HTTP header for redirection
print("Content-Type: text/html\r\n\r\n")

# Connect to the database
try:
    con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
    cur = con.cursor()
except pymysql.MySQLError as e:
    print(f"<p>Database connection error: {e}</p>")
    sys.exit()

# Get form data
form = cgi.FieldStorage()
user_id = form.getvalue("user_id")
request_id = form.getvalue("request_id")
shop_id = form.getvalue("shop_id")  # Added this line
rating = form.getvalue("rating")
review_text = form.getvalue("review")

# Handle potential missing values
if not user_id or not request_id or not shop_id:
    print("<p>Error: User ID, Request ID, or Shop ID is missing.</p>")
    print("<p>Please go back and try again.</p>")
    sys.exit()

# Prepare and execute the SQL query to insert the review
try:
    # SQL query now includes shop_id
    sql = """
    INSERT INTO reviews (user_id, request_id, shop_id, rating, review_text)
    VALUES (%s, %s, %s, %s, %s)
    """

    if rating or review_text:
        cur.execute(sql, (user_id, request_id, shop_id, rating, review_text))
        con.commit()

        # Redirect the user back to the completed requests page
        print(f"""
        <script>
            alert("Review submitted successfully!");
            window.location.href = 'completed_booking.py?user_id={user_id}';
        </script>
        """)
    else:
        print("<p>Error: No rating or review provided.</p>")

except pymysql.MySQLError as e:
    con.rollback()
    print(f"<p>An error occurred while submitting your review: {e}</p>")
finally:
    # Close the database connection
    cur.close()
    con.close()