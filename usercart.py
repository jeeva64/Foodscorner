#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html\r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="Foodscorner")
cur = con.cursor()
v = cgi.FieldStorage()
id = v.getvalue("Id")
f="""select Fid from cart where Uid=%s """%(id)
cur.execute(f)
fid=cur.fetchall()
print("""<!DOCTYPE html>
    <html>
    <head>
        <title>Cart Products</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"/>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
        <link rel="stylesheet"  href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"/>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
        <style>
            *{
                padding: 0px;
                margin: 0px;
            }
            .bg{
                opacity:0.8;
            }
            #cart-img{
                height:300px;
                width:70%;
            }
            .cart-item{
                    max-height:450px;
                    padding:1%;
                    width:30%;
                    margin:1%;
                    border:1px solid black;
                    border-radius:10px;
                }
            #tit{
                font-size: 70px;
                font-weight: bold;
                font-family: Times New Roman;
                padding-left: 10%;
            }
            .heading{
                text-decoration: underline;
            }
    
            #formv label{
                font-size: xx-large;
                color:white;
            }
    
            #formv input{
                height:15%;
                width: 50%;
            }
            .con{
                background-image:linear-gradient(cyan,lavender,skyblue);
                border:3px solid;
                box-sizing:border-box;
            }
            footer{
                height:auto;
            }
            .ftit:hover{
                text-decoration: underline;
            }
            #navbar li{
                display: inline;
                font-size: large;
            }
            a{
                font-size: x-large;
                text-decoration: none;
                color:darkviolet;
            }
            #navbar a:hover{
                text-decoration: underline;
            }
            #row-img{
                padding:5%;
            }
            #col-img{
                margin-bottom:2%;
            }
        </style>
    </head>""")
print("""
    <body>
        <header class="container-fluaid con" id="fh">
              <h1 id="tit">Foods Corner</h1>
              <ul id="navbar" class="row" align="center">
                    <div class="col-xs-3">
                        <li><a href="userdashboard.py?Id=%s" id="n1" class="btn btn-info"><span class="glyphicon glyphicon-home"></span>  Home</a></li>
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
                          <li><a href="usercart.py?Id=%s" id="n5" class="btn btn-info"><span class="glyphicon glyphicon-shopping-cart"></span>  Cart</a></li>
                    </div>
              </ul>
        </header>
        <h1 align="center">Foods:</h1>
        <div class="container">
        <div class="row" id="row-img">
""" %(id,id))
for i in fid:
    q1 = """select * from foods where Fid='%s'"""%(i)
    cur.execute(q1)
    res = cur.fetchone()
    q2="""select Quantity from cart where Fid='%s' """%(i)
    cur.execute(q2)
    res1=cur.fetchone()
    print(""" 
        <div class="col-md-9" id="col-img">
                <img src="media/%s" alt="%s" id="cart-img" height="300px" class="rounded" align="center">
        </div>
        <div class="col-md-3"><br>
                   <h2>%s</h2><br>
                   <input type="hidden" name="foodid" value="%s">
                   <h4><del>RS.%s</del>  RS.%s</h4>
                   <h6>%s</h6><br>
                   <p>Quantity: %s</p>   
                   <a href="removecart.py?Id=%s&fid=%s"><button type="submit" class="btn btn-danger"><span class="glyphicon glyphicon-trash"></span>  Remove</button></a>
        </div>""" %(res[5],res[1], res[1], res[0],res[2], res[3], res[4],res1[0],id,res[0]))
print("""
</div>  
</div>
<div align="center">
    <a href="order.py?Id=%s"<button type="submit" class="btn btn-success"><span class="glyphicon glyphicon-ok"></span>  Proceed</button></a>
</div><br>"""%(id))
print("""
<footer class="conatainer-fluaid con" id="hf">
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

