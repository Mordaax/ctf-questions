
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Nullsec Login</title>
    <link rel="stylesheet" href="">
  </head>
  <body>
    <img src=Nullseclogo.png alt="NullsecLogo" width="300px" height="300px"/>
    <form action="includes/login.inc.php" method="post">
      <input type="username" name="username" placeholder="Username....">
      <input type="password" name="password" type="number" placeholder="Password...." pattern="[0-9]{0,10}" title="Password should only contain numbers">
      <button class="password" type="submit" name="submit">Login</button>
    </form>
    <style>
      input {
        width: 100%;
        padding: 12px 20px;
        margin: 8px 0;
        box-sizing: border-box;
      }
      /* hello nothing here flag{_N0ta_flag}*/
      .button{
        display:inline-block;
        padding:0.7em 1.4em;
        margin:0 0.3em 0.3em 0;
        border-radius:0.15em;
        box-sizing: border-box;
        text-decoration:none;
        font-family:'Roboto',sans-serif;
        text-transform:uppercase;
        font-weight:400;
        color:#FFFFFF;
        background-color:#3369ff;
        box-shadow:inset 0 -0.6em 0 -0.35em rgba(0,0,0,0.17);
        text-align:center;
        position:relative;
      }
      .button:active{
        top:0.1em;
      }
      @media all and (max-width:30em){
        .button{
          display:block;
          margin:0.4em auto;
        }
      }
    </style>
  </body>
</html>


<?php
  if(isset($_GET["login"])){
    if ($_GET["login"] == "true"){
      echo "HNF{w3b_2_simple_5873}";
    }
  }
  else if(isset($_GET["error"])){
    if ($_GET["error"] == "loginerror"){
      echo "<b>Invalid Credentials</b>";
    }
    else if ($_GET["error"] == "adminerror"){
      echo "<p>admin error, password hint: 2406*****</p>";
    }
  }
?>