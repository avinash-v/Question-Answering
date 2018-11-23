<?php
	if($_POST['formsub'] == "submit")
	{
		$fname = $_POST['fname'];
		$email = $_POST['email'];
		$mes   = $_POST['feedback'];

		$file = 'C:\xampp\htdocs\hostspace\feedback.txt';

		$f = fopen($file,"a");
		$val = $fname . $email . $mes . "\n";
		fwrite($f, $val);
		fclose($f);
	}
	
?>

