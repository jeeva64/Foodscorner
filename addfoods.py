#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html\r\n\r\n")
import pymysql,cgi,cgitb,smtplib,os
cgitb.enable()
con=pymysql.connect(host="localhost",user="root",password="",database="Foodscorner")
cur=con.cursor()
v=cgi.FieldStorage()
id=v.getvalue("Id")
print("""
<!DOCTYPE html>
<html lang="en">
<head>   
    <title>Add Foods</title>
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
            font-size: x-large;
            
        }
        #formv input{
            height:15%;
            width: 50%;
        }
    </style>
</head>""")
print("""
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
    <div class="container bg-warning bg" align="center"><br>
        <form class="form-group" id="formv" enctype="multipart/form-data" method="post">
            <h1 class="text-dark">Add Foods</h1><br>
            <label for="fid">Food Id:</label>
            <input type="number" id="fid" name="fid" placeholder="  Enter Food Id" class="form-control" required><br><br>
            <label for="fname">Food Name:</label>
            <input type="text" id="fname" name="fname" placeholder="  Enter Food Name" class="form-control" required><br><br>
            <label for="eprice">Food Expected Price:</label>
            <input type="number" id="eprice" name="eprice" placeholder="  Enter Food Expected Price" class="form-control" required><br><br>
            <label for="aprice">Food Actual Price:</label>
            <input type="number" id="aprice" name="aprice" placeholder="Enter Food Actual Price" class="form-control" required><br><br>
            <label for="fimgage">Upload Food Image:</label>
            <input type="file" id="fimage" name="fimage" accept="jpg,png" required><br><br> 
            <label for="dfood">Food Description:</label>
            <input type="text" id="dfood" name="dfood" required placeholder="Enter Food Details" class="form-control"><br><br>
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
            var fid=document.getElementById("fid").value;
            var fname=document.getElementById("fname").value;
            var ep=document.getElementById("eprice").value;
            var ap=document.getElementById("aprice").value;
            var df=document.getElementById("dfood").value;
            var fimg=document.getElementById("fimage").value;
            if(fid==""){
                alert("Enter Your Food Id");
                return false;
            }
            if(fname==""){
                alert("Enter Your Food Name");
                return false;
            }
            if(ep==""){
                alert("Enter Your Food Expected Price");
                return false;
            }
            if(ap==""){
                alert("Enter Your Food Actual Price");
                return false;
            }
            if(fimg==""){
                alert("Upload Food Image");
                return false;
            }
            if(df==""){
                alert("Enter Your Food description");
                return false;
            }
        }
    </script>
</body>
</html>
"""%(id))
sub=v.getvalue("submit")
if sub!=None and len(v)!=0:
    fid=v.getvalue("fid")
    fname=v.getvalue("fname")
    ep=v.getvalue("eprice")
    ap=v.getvalue("aprice")
    fimg=v['fimage']
    df=v.getvalue("dfood")
    if fimg.filename:
        fn=os.path.basename(fimg.filename)
        open("media/"+fn,"wb").write(fimg.file.read())
        q="""insert into foods(Fid,Foodname,Price,ActualPrice,Details,Food_Image)values('%s','%s','%s','%s','%s','%s') """%(fid,fname,ep,ap,df,fn)
        cur.execute(q)
        con.commit()
        print("""<script>
        alert("Food Registered Successfully");
        </script>""")
