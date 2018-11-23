<?php
    header("Access-Control-Allow-Origin: *");
    header('Access-Control-Allow-Methods: *');
    

    
    $file = 'C:\xampp\htdocs\hostspace\counter.txt';

    $f = fopen($file,"a+");
    $line = trim(fgets($f));
	#echo gettype($line);

	$counterVal = intval($line);

	#echo($counterVal);
    fclose($f);
	#echo($counterVal);

    $ret = json_encode($counterVal);
    echo $ret; 
	
    ?>

 
