#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html\r\n\r\n")
print(""" 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Foods Corner</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"/>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <link rel="stylesheet"  href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"/>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <style>
      * {
        padding: 0px;
        margin: 0px;
      }
      #tit {
        font-size: 70px;
        font-weight: bold;
        font-family: Times New Roman;
        padding-left: 10%;
      }
      .con {
        background-image: linear-gradient(cyan, lavender, skyblue);
        border: 3px solid;
      }
      .ftit:hover {
        text-decoration: underline;
      }
      #navbar li {
        display: inline-block;
        font-size: large;
      }
      a {
        font-size: x-large;
        text-decoration: none;
        color: darkviolet;
      }
      #navbar a:hover {
        text-decoration: underline;
      }
      #content {
        font-size: x-large;
        text-indent: 7%;
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
    <div class="container">
      <br />
      <div class="carousel slide" id="caro" data-ride="carousel">
        <ol class="carousel-indicators">
          <li data-target="#caro" class="active" data-slide-to="0"></li>
          <li data-target="#caro" data-slide-to="1"></li>
          <li data-target="#caro" data-slide-to="2"></li>
        </ol>
        <div class="carousel-inner" align="center">
          <div class="item active">
            <img
              src="img1.jpg"
              alt="Builiding Image 1"
              class="img-thumbnail"
              height="400px"
              width="70%"
            />
          </div>
          <div class="item">
            <img
              src="img2.webp"
              alt="Builiding Image 2"
              class="img-thumbnail"
              height="400px"
              width="75%"
            />
          </div>
          <div class="item">
            <img
              src="img3.webp"
              alt="Builiding Image 3"
              class="img-thumbnail"
              height="400px"
              width="75%"
            />
          </div>
        </div>
        <a href="#caro" class="left carousel-control" data-slide="prev">
          <span class="glyphicon glyphicon-chevron-left"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a href="#caro" class="right carousel-control" data-slide="next">
          <span class="glyphicon glyphicon-chevron-right"></span>
          <span class="sr-only">Next</span>
        </a>
      </div>
      <br />
      <h1>Description:</h1>
      <p id="content" align="justify">
        Lorem ipsum dolor sit amet consectetur, adipisicing elit. Minus nisi ut
        suscipit libero veniam quisquam, quas nihil accusamus, perferendis
        fugiat soluta odit consequuntur exercitationem vel qui nostrum tenetur.
        Error, quia? Animi tenetur expedita vel dignissimos et consectetur
        itaque repellat ipsum libero quidem. Qui laudantium tempora eos quasi
        nostrum deleniti quidem maiores earum eligendi nisi ullam aut, incidunt
        vitae, fugiat itaque! Praesentium suscipit obcaecati iure, debitis
        doloremque earum, fuga ab illo doloribus consequatur ut natus autem
        error. Nesciunt deleniti, dolorum cum perspiciatis officia fuga. Tempore
        suscipit aspernatur veniam. Itaque, quaerat voluptate. Ab laudantium
        neque quasi sit obcaecati illo vitae perspiciatis, eius quod similique
        voluptatum doloremque quidem dolorum, unde quam commodi, at dicta.
        Eligendi optio nam expedita consequuntur, ullam ipsum modi quae! Minus
        dicta numquam eos illum perspiciatis saepe magni beatae libero
        exercitationem et, tenetur ratione, eaque hic. Fuga soluta laboriosam
        facilis tenetur sapiente. Et nisi culpa ipsum mollitia iste dolorem
        repellendus. Minus non quos eveniet dolorem, harum velit officiis
        dolores est ipsum assumenda iusto quo repellendus fugit atque voluptates
        asperiores omnis ipsa? Et velit provident recusandae dicta magni porro
        reprehenderit fugit. Esse culpa, dolores soluta dolorum ab doloremque
        voluptatum sequi unde dolore explicabo voluptates quas nobis. Doloribus
        laboriosam eum officia ullam alias, adipisci numquam rem ipsa odit,
        fugit corporis a accusantium? Enim fuga quae nobis quasi placeat
        voluptate modi quidem amet, dolorem velit eligendi tempora expedita
        laudantium eos, veniam voluptatum? Doloribus, praesentium! Temporibus ex
        asperiores ipsa tempore aliquid omnis, ipsam natus? Culpa sed
        doloremque, modi dolore obcaecati repudiandae, enim alias aspernatur
        ipsa ipsam, iste nesciunt amet minima dolor sequi corporis soluta sit
        nostrum voluptatem aliquid quo. Ab illo totam fugit. Id. Consectetur
        excepturi, error, sit accusantium, ad unde ducimus officiis distinctio a
        velit eos quia modi? Rem, est facilis laudantium quam inventore aliquid
        quaerat, accusamus nemo itaque sed eos, placeat possimus?
      </p>
    </div>
    <br />
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