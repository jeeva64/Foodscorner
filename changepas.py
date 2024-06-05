#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html\r\n\r\n")
print("""
<!DOCTYPE html>
<html>
<head>
    <title>Change Password</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"/>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <link rel="stylesheet"  href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"/>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="style.css">
    <style>
        #formv label{
            font-size: xx-large;
            color:white;
        }
        #formv input{
            height:15%;
            width: 50%;
        }    
    </style>
</head>
<body>
    <header class="container-fluaid con">
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
                <a href="register.py" id="n4" target="_blank" class="btn btn-info"><span class="glyphicon glyphicon-floppy-disk"></span>  Register</a>
              </li>
            </div>
            <div class="col-xs-3">
              <li>
                <a href="login.py" id="n5" target="_blank" class="btn btn-info"><span class="glyphicon glyphicon-user"></span>  Login</a>
              </li>
            </div>
          </ul>
    </header>
    <div align="center">
        <form class="container form-group bg-info " id="formv" enctype="multipart/form-data"method="post">
            <h1 class="heading"> Change Password</h1><br><br>
            <label for="name">Username: </label>
            <input type="text" id="uname" placeholder="  Enter Your Name" name="name" required class="form-control"><br><br>
            <label for="opass">Old Password: </label>
            <input placeholder="  Enter Your Old Password" name="opass" type="password" id="opass" required class="form-control"/><br /><br />
            <label for="upass">New Password: </label>
            <input placeholder="  Enter Your New Password" name="npass" type="password" id="upass" required class="form-control"/><br /><br />
            <label for="cpass">Confirm Password: </label>
            <input placeholder="  Enter Your Confirm Password" name="cpass" type="password" id="cpass" required class="form-control"/><br /><br />
            <input type="submit" onclick="chgpass()" value="Change" name="submit" class="btn btn-success"><br><br>
        </form> 
    </div>
    <footer class="conatainer-fluaid con"><br /><br />
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
            function chgpass() {
                var user = document.getElementById("uname").value;
                var opass=document.getElementById("opass").value;
                var npass = document.getElementById("upass").value;
                var cpass=document.getElementById("cpass").value;
                if (user == "") {
                    alert("Enter Your Username");
                    return false;
                }
                if (opass == "") {
                    alert("Enter Your Old Password");
                    return false;
                }
                if (npass == "") {
                    alert("Enter Your New Password");
                    return false;
                }
                if (cpass == "") {
                    alert("Enter Your Confirm Password");
                    return false;
                }
                if(npass!=cpass){
                    alert("Confirm Password Mismatch");
                    return false;
                }
            }
    </script>
</body>
</html>
""")
import pymysql
import cgi,cgitb
cgitb.enable()
con=pymysql.connect(host="localhost",user="root",password="",database="Foodscorner")
cur=con.cursor()
v=cgi.FieldStorage()
sub=v.getvalue("submit")
if sub!=None:
    name=v.getvalue("name")
    opass=v.getvalue("opass")
    npass=v.getvalue("npass")
    q="""update details set Password='%s' where Username='%s' and Password='%s' """%(npass,name,opass)
    cur.execute(q)
    con.commit()
    print("""<script>
    alert("Password Changed Successfully!");
    </script>
    """)