#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>   
    <title>Register</title>
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
        #tit{
            font-size: 70px;
            font-weight: bold;
            font-family: Times New Roman;
            padding-left: 10%;
        }
        .heading{
            text-decoration: underline;
        }
        .con{
            background-image:linear-gradient(cyan,lavender,skyblue);
            border:3px solid;
        }
        .ftit:hover{
            text-decoration: underline;
        }
        #navbar li{
            display: inline;
            font-size: large;
            min-width: 100px;
        }
        a{
            font-size: x-large;
            text-decoration: none;
            color:darkviolet;
        }
        #navbar a:hover{
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
                  <li class="dropdown-item">
                    <a href="Foodsmain.html" target="_blank">Main</a>
                  </li>
                  <li class="dropdown-item">
                    <a href="Foodsother.html" target="_blank">Other</a>
                  </li>
                </ul>
              </div>
            </div>
            <div class="col-xs-3">
              <li>
                <a href="register.py" id="n4" target="_self" class="btn btn-info"><span class="glyphicon glyphicon-floppy-disk"></span>  Register</a>
              </li>
            </div>
            <div class="col-xs-3">
              <li>
                <a href="login.py" id="n5" target="_blank" class="btn btn-info"><span class="glyphicon glyphicon-user"></span>  Login</a>
              </li>
            </div>
          </ul>
    </header>
    <div class="container bg-info bg" align="center"><br>
        <form class="form-group" id="formv" enctype="multipart/form-data" method="post">
            <h1 class="text-dark heading">Register</h1><br>
            <label for="uname">Username:</label>
            <input type="text" id="uname" name="uname" placeholder="Enter Your Username" class="form-control"><br><br>
            <label for="mail">Email:</label>
            <input type="email" id="mail" name="mail" placeholder="Enter Your Email" class="form-control"><br><br>
            <label for="phone">Mobile Number:</label>
            <input type="number" id="phone" name="phone" placeholder="Enter Your Mobile Number" class="form-control"><br><br>
            <label for="pass">Password:</label>
            <input type="password" id="pass" name="upass" placeholder="Enter Your Password" class="form-control"><br><br>
            <label for="cpass">Confirm Password:</label>
            <input type="password" id="cpass" required placeholder="Enter Your Confirm Password" class="form-control"><br><br>
            <input type="submit" name="submit" class="btn btn-success" onclick="Validate()"><br><br>
        </form>    
    </div>
    <footer class="conatainer-fluaid con">
        <br><br>
        <div class="row">
            <div class="col-sm-4" align="center" >
                <h2 class="ftit" style="display:inline;">Address:</h2>
                <address>
                    364,Town Road,<br>
                    Busy Street,<br>
                    Central city,<br>
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
        function Validate(){
            var name=document.getElementById("uname").value;
            var mail=document.getElementById("mail").value;
            var phone=document.getElementById("phone").value;
            var pass=document.getElementById("pass").value;
            var cpass=document.getElementById("cpass").value;
            if(name==""){
                alert("Enter Your Username");
                return false;
            }
            if(mail==""){
                alert("Enter Your Mail");
                return false;
            }
            if(phone==""){
                alert("Enter Your Mobile Number");
                return false;
            }
            if(pass==""){
                alert("Enter Your Password");
                return false;
            }
            if(cpass==""){
                alert("Enter Your Confirm Password");
                return false;
            }
            if(pass!=cpass){
                alert("Password Mismatch");
                return false;
            }
        }
    </script>
</body>
</html>
""")
import pymysql,cgi,cgitb,smtplib
cgitb.enable()
ble()
con=pymysql.connect(host="localhost",user="root",password="",database="Foodscorner")
cur=con.cursor()
v=cgi.FieldStorage()
sub=v.getvalue("submit")
if sub!=None:
    name=v.getvalue("uname")
    mail=v.getvalue("mail")
    phone=v.getvalue("phone")
    pas=v.getvalue("upass")
    q="""insert into details (Username,Password,Email,Mobile,Role)values('%s','%s','%s','%s','user') """%(name,pas,mail,phone)
    cur.execute(q)
    con.commit()
    fromadd=""
    password=""
    toadd=mail
    subject="Welcome {}".format(name)
    body="Hello {} .Welcome to the Foodscorner Community and waiting to serve you at anytime".format(name)
    msg="""Subject: {} \n\n {} """.format(subject,body)
    server=smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(fromadd,password)
    server.sendmail(fromadd,toadd,msg)
    server.quit()
    print("""<script>
    alert("User Registered Successfully");
    </script>""")
