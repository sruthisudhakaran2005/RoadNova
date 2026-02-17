#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')
print("content-type:text/html \r\n\r\n")

import pymysql, cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
form = cgi.FieldStorage()

location = form.getvalue("sname")
shops = []

# Perform the search only if a location is provided
if location:
    query = """
        SELECT m.*, AVG(r.rating) AS avg_rating
        FROM mechanicshops m
        LEFT JOIN reviews r ON m.id = r.shop_id
        WHERE m.shop_address LIKE %s AND m.status='Approved'
        GROUP BY m.id
    """
    cur.execute(query, ("%" + location + "%",))
    shops = cur.fetchall()

# Print the full HTML page
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RoadNova | Search Results</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sweetalert2@11/dist/sweetalert2.min.css">
    <style>
        body {
            background-color: #f0f2f5;
            font-family: Arial, sans-serif;
        }
        .header-section {
            background-color: #007bff;
            color: white;
            padding: 4rem 0;
            text-align: center;
            border-bottom-left-radius: 50px;
            border-bottom-right-radius: 50px;
            margin-bottom: 2rem;
        }
        .header-section h1 {
            font-size: 2.5rem;
            font-weight: bold;
        }
        .header-section p {
            font-size: 1.1rem;
            opacity: 0.9;
        }
        .card {
            border: none;
            border-radius: 15px;
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
            cursor: pointer;
            margin-bottom: 1.5rem;
            overflow: hidden;
        }
        .card:hover {
            transform: translateY(-10px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
        }
        .card-body {
            padding: 1.5rem;
        }
        .card-img-top {
            border-top-left-radius: 15px;
            border-top-right-radius: 15px;
        }
        .btn-danger {
            background-color: #ff5722;
            border-color: #ff5722;
            transition: background-color 0.3s ease;
        }
        .btn-danger:hover {
            background-color: #e64a19;
            border-color: #e64a19;
        }
        .alert-info {
            background-color: #e7f5ff;
            color: #0056b3;
            border-left: 5px solid #007bff;
            border-radius: 8px;
            padding: 1.5rem;
            text-align: center;
        }
        .alert-info i {
            font-size: 2rem;
            margin-bottom: 1rem;
        }
        .shop-name {
            color: #007bff;
            font-weight: bold;
            font-size: 1.5rem;
        }
        .shop-details {
            font-size: 0.95rem;
        }
        .container {
            max-width: 900px;
        }
        .rating-stars {
            color: gold;
            font-size: 1.2rem;
        }
        .rating-stars .text-warning {
            font-size: 0.9rem;
        }
        .review-modal-body {
            max-height: 400px;
            overflow-y: auto;
        }
        .review-item {
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
            margin-bottom: 10px;
        }
        .review-item:last-child {
            border-bottom: none;
            margin-bottom: 0;
        }
        .review-rating {
            font-size: 1.1rem;
            color: #ffc107;
        }
        .review-author {
            font-weight: bold;
        }
        .review-text {
            color: #555;
            font-style: italic;
        }
    </style>
</head>
<body>

    <div class="header-section">
        <i class="fas fa-search-location fa-2x mb-3"></i>
        <h1>Shops near '%s'</h1>
        <p>Reliable service providers available in your area.</p>
    </div>

    <div class="container">
""" % location)

if shops:
    for shop in shops:
        shop_id = shop[0]
        shop_name = shop[10]
        shop_address = shop[11]
        shop_contact = shop[4]
        shop_image = shop[12]
        status = shop[19]
        avg_rating = shop[20]

        # Generate star rating display
        rating_display = ""
        if avg_rating is not None:
            full_stars = int(avg_rating)
            half_star = (avg_rating - full_stars) >= 0.5
            empty_stars = 5 - full_stars - (1 if half_star else 0)

            rating_display += '<div class="rating-stars">'
            rating_display += '<i class="fas fa-star text-warning"></i>' * full_stars
            if half_star:
                rating_display += '<i class="fas fa-star-half-alt text-warning"></i>'
            rating_display += '<i class="far fa-star text-warning"></i>' * empty_stars
            rating_display += f' <span class="text-muted">({avg_rating:.1f})</span>'
            rating_display += '</div>'
        else:
            rating_display = '<p class="card-text text-muted"><small>No ratings yet</small></p>'

        print(f"""
        <div class="card mb-3 shadow-sm">
          <div class="row g-0 align-items-center">
            <div class="col-md-4">
              <img src="/roadassist/images/{shop_image}" class="img-fluid rounded-start h-100 w-100" alt="Shop Image" style="object-fit: cover;">
            </div>
            <div class="col-md-8">
              <div class="card-body">
                <h5 class="card-title shop-name">{shop_name}</h5>
                {rating_display}
                <p class="card-text shop-details mb-1"><i class="fas fa-map-marker-alt text-secondary me-2"></i><strong>Address:</strong> {shop_address}</p>
                <a href="https://www.google.com/maps/search/?api=1&query={shop_address.replace(' ', '+')}" target="_blank" class="btn btn-outline-primary btn-sm">
                    <i class="bi bi-geo-alt-fill"></i> View on Map
                </a>
                <p class="card-text shop-details mb-1"><i class="fas fa-clock text-secondary me-2"></i><strong>status:</strong> {status}</p>
                <div class="d-flex gap-2">
                    <button type="button" class="btn btn-danger" onclick="showAlertAndRedirect()">
                      <i class="fas fa-tools me-2"></i>Request Service
                    </button>
                    <button type="button" class="btn btn-outline-secondary" data-bs-toggle="modal" data-bs-target="#reviewsModal{shop_id}">
                        <i class="fas fa-comment-dots me-2"></i>View Reviews
                    </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        """)

        # --- Reviews Modal (per shop) ---
        reviews_query = """
            SELECT u.name, r.rating, r.review_text
            FROM reviews r
            JOIN users u ON r.user_id = u.user_id
            WHERE r.shop_id = %s
            ORDER BY r.created_at DESC
        """
        cur.execute(reviews_query, (shop_id,))
        reviews = cur.fetchall()

        print(f"""
        <div class="modal fade" id="reviewsModal{shop_id}" tabindex="-1" aria-labelledby="reviewsModalLabel{shop_id}" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="reviewsModalLabel{shop_id}">Reviews for {shop_name}</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body review-modal-body">
        """)

        if reviews:
            for review in reviews:
                reviewer_name = review[0]
                rating = review[1]
                review_text = review[2]

                # Generate star rating for each review
                review_stars = ""
                for i in range(5):
                    if i < rating:
                        review_stars += '<i class="fas fa-star review-rating"></i>'
                    else:
                        review_stars += '<i class="far fa-star review-rating"></i>'

                print(f"""
                <div class="review-item">
                  <div class="review-header d-flex justify-content-between align-items-center">
                    <span class="review-author">{reviewer_name}</span>
                    <span class="review-rating">{review_stars}</span>
                  </div>
                """)
                if review_text and review_text.strip():
                    print(f"""
                  <p class="review-text mt-2">{review_text}</p>
                    """)
                print("""
                </div>
                """)
        else:
            print("""
            <p class="text-center text-muted">No reviews available for this shop yet.</p>
            """)

        print("""
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>
        """)

else:
    print("""
    <div class="alert alert-info" role="alert">
      <i class="fas fa-frown fa-3x d-block mb-3"></i>
      <h4>No results found.</h4>
      <p>We couldn't find any approved mechanic shops for the given location.</p>
    </div>
    """)

print("""
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <script>
        function showAlertAndRedirect() {
            Swal.fire({
                text: 'Please log in or register to request a service.',
                icon: 'warning',
                showCancelButton: false,
                confirmButtonText: 'OK',
                confirmButtonColor: '#ff5722',
                backdrop: `rgba(0,0,0,0.6)`,
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = "user_reg.py";
                }
            });
        }
    </script>
</body>
</html>
""")

con.close()