<?php
  $password_hash = "0e902564435691274142490923013038";
  $input_password = htmlspecialchars(stripslashes(trim($_POST['password'])));
  $input_username = htmlspecialchars(stripslashes(trim($_POST['username'])));

  if(isset($input_password) && md5($input_password) == $password_hash){
    header("location: ../index.php?login=true");
  }
  else{
    if(isset($input_username) && $input_username == "admin"){
      header("location: ../index.php?error=adminerror");
    }
    else {
      header("location: ../index.php?error=loginerror");
    }
  }
?>
