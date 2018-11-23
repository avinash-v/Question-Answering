<?php
	//get the movie name sent by client
	extract($_GET);

	//We have $movie reaady

	$file = fopen("Elective.txt" , "r");

	if($file){

		$ret = array();

		//loop thru the file and pick all the movies starting with $movie

		while($line = trim(fgets($file)))
		{
			//strncasecmp(string(haystack), substring(needle), len);
			if(strncasecmp($line, $movie, strlen($movie))== 0){
				//[] for auto incrementing the index

				$ret[] = $line;
			}
		}
	//list of movies gotten
		//We assume that the file exists
		echo json_encode($ret);
	}
?>