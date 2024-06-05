#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html\r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="Foodscorner")
cur = con.cursor()
v = cgi.FieldStorage()
id = v.getvalue("Id")
uid=id
q = """select Username,Profile,Email,Mobile from details where Id='%s' """ % (uid)
cur.execute(q)
q1 = """select Foodname,Food_image,ActualPrice,Price,Details,Fid from foods order by Fid"""
cur.execute(q1)
res = cur.fetchall()
print("""<!DOCTYPE html>
    <html>
    <head>
        <title>User Details</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"/>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
        <link rel="stylesheet"  href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"/>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
        <link rel="stylesheet" href="style.css">
        <style>
             *{
            padding: 0px;
            margin: 0px;
            }
            #sidebar{
                padding:40px 0 30px 20px; 
            }
            #cart-text{
                font-size:2rem;
            }
        </style>
    </head>""")
print("""
    <body>
        <header class="container-fluaid con" id="fh">
          <h1 id="tit">Foods Corner</h1>
          <ul id="navbar" class="row" align="center">
            <div class="col-xs-3">
              <li><a href="home.py" id="n1" class="btn btn-info"><span class="glyphicon glyphicon-home"></span>  Home</a></li>
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
                <a href="usercart.py?Id=%s" id="n5" class="btn btn-info"><span class="glyphicon glyphicon-shopping-cart"></span>Cart</a>
              </li>
            </div>
            <div class="col-xs-3">
              <li>
                <a href="login.py" id="n4" class="btn btn-info"><span class="glyphicon glyphicon-off"></span>  Log Out</a>
              </li>
            </div>
          </ul>
        </header>
        <!--<div class="container-fluaid d-grid">
            <div class="row">
                    <ul>
                        <li><a href="changepas.py" target="_self">Change Password</a></li>
                        <li><a href="locate.py"><span class="glyphicon glyphicon-map-marker"></span>Location</a></li>
                    </ul>
                </div>
            </div>
        </div>-->   
"""%(uid))
print("""<h1 align="center">Foods:</h1>
         <div class="container" width="100%" height="auto" align="center">""")
for i in res:
        print("""<div class="col-md-3 col-sm-12 col-xs-6 cart-item" >
                <header>
                        <img src="media/%s" alt="%s" id="cart-img" class="rounded" align="center">
                </header>
                <h2 style="display:inline-block;" id="cart-text">%s</h2><br>
                <h4 style="display:inline-block;"><del>RS.%s</del>  RS.%s</h4><br>
                <h6 style="display:inline-block;" >%s</h6><br>
                <footer>
                        <a href="addcart.py?Id=%s&fid=%s">
                        <button type="submit" class="btn btn-danger"><span class="glyphicon glyphicon-copy"></span>  Add to Cart</button></a><br>
                </footer>
         </div>"""% (i[1],i[0],i[0],i[3],i[2],i[4],uid,i[5]))

print("""  
</div><br><br>
<footer class="container-fluaid con" id="hf">
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
""" % (uid))