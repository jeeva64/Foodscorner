#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html\r\n\r\n")
import pymysql
import cgi,cgitb
cgitb.enable()
con=pymysql.connect(host="localhost",user="root",password="",database="Foodscorner")
cur=con.cursor()
v=cgi.FieldStorage()
id1=v.getvalue("Id")
q1="""select Username,Profile,Email,Mobile from details where Id='%s' """%id1
cur.execute(q1)
res1=cur.fetchone()
print("""<!DOCTYPE html>
    <html>
    <head>
        <title>Admin Page</title>
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
            .btbr,.btbr:hover,.btbr:visited{
                border:0px;
                font-size: x-large;
                color:darkviolet; !important
            }
        </style>
    </head>
    <body>
        <header class="container-fluaid con">
          <h1 id="tit">Foods Corner</h1>
          <ul id="navbar" class="row" align="center">
            <div class="col-xs-3">
              <li><a href="admin.py?Id=%s" id="n1" class="btn btn-info"><span class="glyphicon glyphicon-home"></span>  Home</a></li>
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
                <a href="register.py" id="n4" target="_blank" class="btn btn-info"><span class="glyphicon glyphicon-floppy-disk"></span>  Register</a>
              </li>
            </div>
            <div class="col-xs-3">
              <li>
                <a href="login.py" id="n5" target="_blank" class="btn btn-info"><span class="glyphicon glyphicon-user"></span>  Login</a>
              </li>
            </div>
          </ul>
        </header>"""%(id1))
print("""<div class="container-fluaid d-grid">
            <div class="row">
                <div class="col-md-3 col-sm-3 col-xs-3 bg-info" id="sidebar">
                    <ul class="nav navbar-nav nav-stacked">
                        <li><a href="" onclick="profile()"><span class="glyphicon glyphicon-user"></span>  Profile</a></li>
                         <div class="dropdown">
                            <button data-bs-toggle="dropdown" class="btn dropdown-toggle btbr"><span class="glyphicon glyphicon-glass"></span>  Foods</button>
                            <ul class="dropdown-menu">
                                <li class="dropdown-item"><a href="addfoods.py?Id=%s"><span class="glyphicon glyphicon-plus"></span>  Add Foods</a></li>
                                <li class="dropdown-item"><a href="updatefoods.py?Id=%s"><span class="glyphicon glyphicon-edit"></span>  Update Foods</a></li>
                                <li class="dropdown-item"><a href="deletefoods.py?Id=%s"><span class="glyphicon glyphicon-trash"></span>  Delete Foods</a></li>
                            </ul>
                        </div>
                        <li><a href=""><span class="glyphicon glyphicon-book"></span>  Order Summary</a></li>
                        <li><a href="home.py"><span class="glyphicon glyphicon-off"></span>  Log Out</a></li>
                    </ul>
                </div>
                <div class="col-md-9 bg-warning col-sm-9 col-sm-9" style="display:inline;">
                    <center><br><br>
                        <h1>Welcome : %s<img src="media/%s" height="200px" width="auto" class="rounded-circle"></h1>
                        <h3>Email: %s</h3>
                        <h3>Mobile Number: %s</h3><br><br>
                    </center>
                </div>
            </div>
        </div>    
            <div class="Container" align="center">
                <h1 align="center">Order Summary</h1>
                <table border="5px" width="600px" height="auto" cellpadding="5px" class="table table-bordered table-striped" >
                    <tr>
                        <th>Customer Name</th>
                        <th>Food Name</th>
                        <th>Food Price</th>
                        <th>Quantity</th>
                        <th>Total Price</th>
                        <th>Amount to Pay</th>
                    </tr> 
"""%(id1,id1,id1,res1[0],res1[1],res1[2],res1[3]))
q2 = """select Fid,Uid,Quantity,Price,TotalPrice from ordercart where Adminid='%s'""" % (id1)
cur.execute(q2)
res2 = cur.fetchall()
for i in res2:
    fdid = i[0]
    uid = i[1]
    qt = i[2]
    p=i[3]
    tp = i[4]
    q3 = """select Foodname,Food_Image from foods where Fid='%s'""" % (fdid)
    cur.execute(q3)
    res3 = cur.fetchone()
    fname = res3[0]
    fimg = res3[1]
    q4="""select Username from details where Id='%s' and Role='User'"""%(uid)
    cur.execute(q4)
    res4=cur.fetchone()
    uname=res4[0]
    q5 = """select sum(TotalPrice) from cart where Uid='%s' """ % (uid)
    cur.execute(q5)
    res5 = cur.fetchone()
    print("""
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>RS.%s</td>
    </tr>
"""%(uname,fname,p,qt,tp,res5[0]))
print("""</table> 
</div><br>
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
    </body>
    </html>
    """)
