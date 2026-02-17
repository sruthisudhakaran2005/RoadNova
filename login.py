#!C:/Users/SRUTHI S/AppData/Local/Programs/Python/Python311/python.exe
import pymysql, cgi, cgitb
print("content-type:text/html \r\n\r\n")

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="roadassist")
cur = con.cursor()
print("""
<div class="modal fade" id="userLoginModal" tabindex="-1" aria-labelledby="userLoginModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <button type="button" class="btn-close position-absolute end-0 m-3" data-bs-dismiss="modal" aria-label="Close"></button>
      <div class="modal-header">
        <div class="text-center w-100">
          <i class="fas fa-user-circle fa-3x mb-2"></i>
          <h5 class="modal-title">User Login</h5>
        </div>
      </div>
      <div class="modal-body">
        <form name="form2" method="post" enctype="multipart/form-data">
        <h4>Login As User</h4>
          <div class="mb-3">
                <label for="usermail"  class="form-label">Email:</label>
                <input type="email"id="usermail" class="form-control" name="usermail">
                </div>
                <div class="mb-3">
                <label for="password"  class="form-label">Password</label>
                <input type="password" id="password" class="form-control" name="password"> 
                 </div>                      
              <button type="submit" class=" btn btn-primary " name="submit">Login</button>
             
            </form>
      </div>
    </div>
  </div>
</div>

""")
form = cgi.FieldStorage()
Email = form.getvalue("usermail")
Password = form.getvalue("password")
Submit = form.getvalue("submit")

if Submit != None:
    q = """select user_id from users where email="%s" and password="%s" """ %( Email, Password)
    cur.execute(q)
    res = cur.fetchone()
    if res is not None:
        print("""
        <script>
        alert("login success!");
        location.href="user.py?id=%s"
        </script>
        """ % (res[0]))
    else:
        print("""
        <script>
        alert("incorrect username or password" );
        location.href="login.py"
        </script>
        """)