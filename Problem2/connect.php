<?php
    $database=array();
    $database['host'] = "localhost";
    $database['port'] ='3306';
    $database['name'] = 'forum';
    $database['username'] = 'root';
    $database['password']='';

    $link=mysql_connect($database['host'],$database['username'],$database['password']);

    if ($link){
        echo "Success" .$database['name'];
    }
    else {
        echo "fail".$database['name'];
        echo "Error :  ".mysql_error();
    }

?>