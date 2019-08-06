In order to run the script, the data file (exercise1.json) must be in the same directory. Other than that, one just need to open the console at such path and run the script. On windows, it should be written "python ex1.py".


###########################################################


The script is divided into several sections.

In the first section, we create the different tools we will need later: the class City, a list of the cities involved as well as a dictionary used to represent the connection between cities, as well as the objective function, named "balance".
We use the word tour to refer to the sequence of cities the player visits (this word is widely used for the TSP, another combinatorial optimization problem I tackled for my Bachelor's thesis).

In the second section, we make all the arrangements required to get the data input from exercise1.json.

The third section represents the main part of the solution.
	· The first function builds all the possible tours of n cities such that start and end at the base.
	· The second one generates all the possible tours of length from one to n. This way, we accept the fact that a tour of length less than n might be better than another one with n cities.
	· mainFuction is used to, once we have all the valid tours thanks to the previous function, get the best tours (the optimal tours). In case of tie, the shortest tours are chosen.
	
The last section lets the user interact with the program by means of the console.