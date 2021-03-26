<?php
    include("connect.php");

    $username=$_POST['username'];
    $password=$_POST['password'];
    $name=$_POST['name'];

    $MIN_LENGTH = 8;
    if ( $username =="" || $passwor==""){
        echo "Username and Password can't be empty";
    }
    else {
        if ( strlen($password) >= $MIN_LENGTH ){
             $sql="INSERT INTO forum.users(name,username,paswword)
        VALUES('$name','$username','$password');
        ";
    $res=mysql_query($sql);

    if($res){
        echo "Successfully registered as : ".$username;

    }
    else {
        echo "Failed to register";
        echo "MySQL errors : ".mysql_error();
    }
        }
        else {
            echo "Please enter a password at least 8 characters long";
        }
    }

   
?>