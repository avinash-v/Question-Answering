//Constructor function. Will be used to create "obj"
//All functions will be written here

function Suggest()
{
	//Save 'this' because when the browser fires a function
	//registered with setTimeout , it fires it on the Window object
	//and so "this" will mean window
	othis = this;

	this.xhr = new XMLHttpRequest();

	this.movie = null;

	this.containerdiv = null;

	this.timer = null;

	//This function is fired every time there is a keyup event

	this.getMovies = function()
	{
		//If a function was already registered , cancel him out
		if(othis.timer){

			clearTimeout(othis.timer);
		}


		//Go to server in 1 second
		othis.timer = setTimeout(othis.fetchMovies , 1000);
	}

	this.fetchMovies = function(){
		
		//alert("going now");
		//We need to show list of movies corresponding to the substring that we typed.
		//If the substring was already searched , then we dont need to visit the server
		//First check if there is anything in the field at all
		othis.movie = document.getElementById("movie");
		othis.containerdiv = document.getElementById("container");

		if(othis.movie.value == ""){ 									//here
		
			//alert(document.getElementById("movie").value);
			othis.containerdiv.innerHTML = "";
			othis.containerdiv.style.display = "none";
			return;
		}
		//Else somethis is typed.
		else{
			mykey = "http://localhost/auto_Suggest/get_movies.php?movie="+othis.movie.value;
			if(localStorage[mykey]){

				cachedmovies = JSON.parse(localStorage[mykey]);

				othis.populateMovies(cachedmovies);
				//present in cache
			
			}
			else{

				//else not present
				//alert(document.getElementById("movie").value);
				
				othis.xhr.onreadystatechange = othis.processResults;

				othis.xhr.open("GET" , "http://localhost/auto_Suggest/get_movies.php?movie="+othis.movie.value,true);
				
				othis.xhr.send();

			}

		}
	}

	this.processResults = function(){

		if(othis.xhr.readyState == 4 && othis.xhr.status == 200){

			//alert("Cleared#");
			//We expect a JSON return value
			movies = JSON.parse(othis.xhr.responseText)	;

			//First check if movies is null or not
			if(movies.length == 0)
			{
				//Clean up the container div . Should be empty
				othis.containerdiv.innerHTML = "";
				othis.containerdiv.style.display = "none";

				//alert("Cleared2");
				//Tell the user that nothing was returned
				othis.movie.className = "notfound";
			}	

			else{

				//We got some movies
				//alert("Cleared3");
				othis.movie.className = "found";
				//using function to make it easier for use , can reuse this function when we have cache too

				othis.populateMovies(movies);
				//now cache the movies in Localstorage
				//url as key , not sure why it is used
				key = "http://localhost/auto_Suggest/get_movies.php?movie=" + othis.movie.value;

				localStorage[key] = othis.xhr.responseText;
			
			}
		}
	}

	this.populateMovies = function(movies){

		othis.containerdiv.innerHTML = "";

		for (i = 0; i < movies.length ; i++){

			newdiv = document.createElement("div");

			newdiv.innerHTML = movies[i];

			newdiv.className = "suggest";
			//Add it to container

			othis.containerdiv.appendChild(newdiv);
			othis.containerdiv.style.display = "block";

			//onclick functionality

			newdiv.onclick = othis.setMovie;
		}
		othis.containerdiv.style.display = "block";
	}

	this.setMovie = function(event){

		//First find out which movie was selected
		clickedelem = event.target;

		othis.movie.value = clickedelem.innerHTML;

		//Clean up the container div

		othis.containerdiv.innerHTML = "";
		othis.containerdiv.style.display = "none";

	}
}


obj = new Suggest();