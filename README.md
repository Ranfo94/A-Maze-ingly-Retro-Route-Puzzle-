# A-Maze-ingly-Retro-Route-Puzzle-

Docs

summary

1. Software Description
2. Software Architecture and Components
	2.1 Entities
	2.2 Mapper
	2.3 Solver
3. Installation
4. Tests
5. Usage


1. Software Description

The Maze Solver application solves the problem to find a path to collect a certain amount of objects from a series of rooms starting from a specific room ID. 
The solution has been developed using the Python programming language.

2. Software Architecture and Components

For the given problem it was chosen a simple architecture based on 3 modules:
	- an Entity module that contains the classes needed to incapsulate rooms and coordinates objects;
	- a Mapper module that contains all the functions needed to obtain a dictionary of room objects starting from the path to a valid JSON file;
	- a Solver module that contains the functions to solve that actual maze problem starting from the problem's inputs.

2.1 Entities

There are two entities that have been identified to correctly model the application:
	- Room
	- Coordinates

A Room object contains the following informations
	- Id: an integer that represents the room identifier;
	- Name: a string that reprepresents the room name;
	- Coordinates: a coordinates object that contains the identifiers of all the rooms adjacent with the current one;
	- Objects: a list of string that represent the list of the object that can be collected inside the room.

A Coordinates object the following information
	- North: the identifier of the room north of the current room;
	- South: the identifier of the room south of the current room;
	- East: the identifier of the room east of the current room;
	- West: the identifier of the room west of the current room.

2.2 Mapper

The mapper module is responsible for creating a list of Room objects staring from the path to the input JSON file. It helps to isolate all functions that operates on the json object in a single module and helps the overall readability of the code

When a JSON file is processed some checks are made to prevent the solver module to use a non-compliant JSON file. The application raises an error if:
	- the json path specified as input is a non-existing file;
	- the json file is empty;
	- the json file is a non-valid JSON.

The hearth of this module is the parseJsonMap function that returns a dictionary where the key is represented by the room's identifier and the value is the room object associated with the key. This choise has been made to simplify the search for a room. In fact the search for a specific room's id has a complexity of O(1) against the complexity of O(n) of seaching all items untill the desired one is found.

2.3 Solver

The solver module is the hearth of the application as it contains the functions needed to find the path to collect all the items that the application is searching for. 

The findPath function is the access point to the module. This function sets the initial values for the recursion and calls the recursive function visitRoom with inputs the room to be visited and the identifier of the previus room. The identifier the of the previous room is needed to let the function know where the path is going if no rooms can be visited and not all items have been found.

This function add a new entry to the path if the room has not been visited yet and then checks if there are adjacent rooms that needs to be visited. If all adjacent rooms have been visited already and there are still items to be collected the functions knows that path is getting back to the previous room and writes an entry to the path with the previous room and empty objects.

The function raises and error if the recursion is over and there are still items to be found.

3. Installation

To setup the environment to run the application just run the "install.sh" script that will:
	- install pip with the following command 

	- install the pytest to run the tests 
		pip install -U pytest

4. Tests

To run the test just run the "test.sh"" script that will use pystest to run all the unit tests written for the application

5. Usage

To use the application just run the run.sh script that will run the application with 3 parameters

	- path_to_json_file: the relative or absolute path to the json file containing the rooms data
	- staring_room_id: an integer representing the identifier of the first room to be visited
	- objects_list: a list of objects incapsulated in double quotes and space separated "Obj 1" "Obj 2" ... "Obj N"

the run.sh script will invoke the python application with the following code

	python3 app.py path_to_json_file staring_room_id objects_list

If the run is successfull the application will print on stdout the path to collect all items starting from the starting_room_id, otherwise it will print on stderr any possible error