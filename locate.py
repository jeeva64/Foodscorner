#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html\r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="Foodscorner")
cur = con.cursor()
v = cgi.FieldStorage()
id = v.getvalue("Id")
q = """select Username,Profile,Email,Mobile from details where Id='%s' """ % id
cur.execute(q)
print("""<!DOCTYPE html>
    <html>
    <head>
        <title>Locate Us</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"/>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
        <link rel="stylesheet"  href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"/>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
        <link rel="stylesheet" href="style.css">
        <style>
            #sidebar{
                padding:40px 0 30px 20px; 
            }
        </style>
    </head>
    <body>
        <header class="container-fluaid con">
          <h1 id="tit">Foods Corner</h1>
          <ul id="navbar" class="row" align="center">
            <div class="col-xs-3">
              <li><a href="home.py" id="n1" class="btn btn-info">Home</a></li>
            </div>
            <div class="col-xs-3">
              <div class="dropdown">
                <button data-bs-toggle="dropdown" class="btn btn-info dropdown-toggle">Foods</button>
                <ul class="dropdown-menu">
                  <li class="dropdown-item"><a href="Foodsmain.html" target="_blank">Main</a></li>
                  <li class="dropdown-item"><a href="Foodsother.html" target="_blank">Other</a></li>
                </ul>
              </div>
            </div>
            <div class="col-xs-3">
              <li>
                <a href="register.py" id="n4" target="_blank" class="btn btn-info">Register</a>
              </li>
            </div>
            <div class="col-xs-3">
              <li>
                <a href="login.py" id="n5" target="_blank" class="btn btn-info">Login</a>
              </li>
            </div>
          </ul>
        </header>
        <div class="container-fluaid d-grid">
            <div class="row">
                <div class="col-md-3 col-sm-3 col-xs-3 bg-info" id="sidebar">
                    <ul class="nav navbar-nav nav-stacked">
                        <li><a href="" target="_blank" onclick="profile()">Profile</a></li>
                        <li><a href="changepas.py" target="_self">Change Password</a></li>
                        <li><a href="">Location</a></li>
                        <li><a href="home.py">Log Out</a></li>
                    </ul>
                </div>
                <div class="col-md-9 col-sm-9 col-sm-9" style="display:inline;">
                    <h3>Reach Us</h3>
                    <iframe src="https://www.google.com/maps/embed?pb=!1m10!1m8!1m3!1d7832.315878473138!2d76.9507016!3d11.0267744!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sin!4v1717022043983!5m2!1sen!2sin" width="800" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                    <br>
                </div>
            </div>
        </div>
        <footer class="conatainer-fluaid con">
          <br /><br />
          <div class="row">
            <div class="col-sm-4" align="center">
              <h2 class="ftit" style="display:inline;">Address:</h2>
              <address>
                364,Town Road,<br />
                Busy Street,<br />
                Central city,<br />
                chennai-620678.
              </address>
            </div>
            <div class="col-sm-4" align="center">
              <h2 class="ftit" style="display:inline;">Email:</h2>
              <p>Sample.hotels5@gmail.com</p>
            </div>
            <div class="col-sm-4" align="center">
              <h2 class="ftit" style="display:inline;">Contact Details:</h2>
              <p>+91 9912345467</p>
            </div>
          </div>
          <center class="container"><br />
            <h2 class="ftit">About Us:</h2><br>
            <p style="text-align:justify">FoodsCorner is one of the puriest and culture based restraunt with 
                    affordable price for every foods.You can also order foods via online through this webpage
                    and also home delivery at free of cost for order amount greater than Rs.500.Unless home delivery
                    charge of Rs.100 levied for order amount less than Rs.500.Thank you for choosing us.Don't 
                    hesitate to complaint about problems regarding delivery,foods packing,tec</p> 
            <h3>&copyCopyrights Reserved 2024</h3>
            <h3>All Rights Reserved</h3>
            <br /><br />
          </center>
        </footer>
        <script>
            function profile(){
                location.href="profile.py?Id=%s"
            }
        </script>
    </body>
    </html>
    """ % id)
