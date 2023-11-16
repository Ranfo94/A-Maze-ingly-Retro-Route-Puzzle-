# A Maze-ingly Retro Route Puzzle

## Summary

1. Problem Description
	1. Example
2. Software Description
3. Installation
4. Tests
5. Usage


## Problem Description

This program outputs a valid route (not the shortest) to collect a set of items within a maze. The maze is a json description of set of rooms. Each room can have one or more objects to be collected and describes all the adjacent rooms.

Program input:

- A path to a valid JSON file containing the maze structures
- The identifier of the starting room
- The list of the objects to be collected

Program output:

- A valid route to collect all the given items


### Example

#### sample_maze.json

```json 
{
  "rooms": [
    {
      "id": 1,
      "name": "Hallway",
      "north": 2,
      "objects": []
    },
    {
      "id": 2,
      "name": "Dining Room",
      "south": 1,
      "west": 3,
      "east": 4,
      "objects": []
    },
    {
      "id": 3,
      "name": "Kitchen",
      "east": 2,
      "objects": [
        {
          "name": "Knife"
        }
      ]
    },
    {
      "id": 4,
      "name": "Sun Room",
      "west": 2,
      "objects": [
        {
          "name": "Potted Plant"
        }
      ]
    }
  ]
} 
```

#### Input

- Map = maze.json
- Starting room = 1
- Objects to collect = Knife

#### Output

| Room Name | Objects Collected |
| :--- | :---: |
|   Hallway   | None |
|   Dining Room   | None |
|  Sun Room   | None |
|  Dining Room   | None |
|  Kitchen   | Knife |

## Software Description

The Maze Solver application solves the problem to find a path to collect a certain amount of objects from a series of rooms starting from a specific room ID. 
The solution has been developed using the Python programming language.

## Software Architecture and Components

For the given problem it was chosen a simple architecture based on 4 modules:
- an Entity module that contains the classes needed to incapsulate rooms and coordinates objects;
- a Mapper module that contains all the functions needed to obtain a dictionary of room objects starting from the path to a valid JSON file;
- a Finder module that contains the functions needed to solve that actual maze problem starting from the problem's input
- a Solver module that encapsulates all arguments and exposes the functions developed by the Solver

## Installation

To setup the environment to run the application just install all the packages contained in the requirements.txt file with pip like the following

```bash
pip install -r requirements.txt 
```

## Tests

To execute the test procedure just run the following

```bash
pytest
```

## Usage

To use the application just run the app.py script that will run the application with 3 parameters

- path: the relative or absolute path to the json file containing the rooms data
- id: an integer representing the identifier of the first room to be visited
- objects: a list of objects incapsulated in double quotes and space separated "Obj 1" "Obj 2" ... "Obj N"

An example of usage 

```bash
python3 app.py src/smallMaze.json 1 Knife
```

To learn more about the usage just run

```bash
python app.py -h
```

If the run is successfull the application will print on stdout the path to collect all items starting from the starting_room_id, otherwise it will print on stderr any possible error