from parsers.MapParser import build_rooms_dictionary, read_json_string
from finder.PathFinder import find_path
from exceptions.MazeExceptions import SolverInitException


class Solver:
    '''
    The Solver class incapsulates the problem exposing the functions 
    to find the desired path using the given arguments
    '''

    def __init__(self, rooms_json_file_path="", starting_room_id=0, objects_to_be_collected=[]):
        '''
        Init function for the Solver class
        @param rooms_json_file_path Path to the file containing the definition of the rooms in JSON format
        @param starting_room_id Id of the starting room
        @param objects_to_be_collected List of objects to be collected from the rooms

        @raise SolverInitException if wrong arguments are passed to the constructor
        '''
        self.rooms_json_file_path = rooms_json_file_path
        self.starting_room_id = starting_room_id
        self.objects_to_be_collected = objects_to_be_collected
        self.__check_valid_arguments()

    def __check_valid_arguments(self):
        if self.rooms_json_file_path == "":
            raise SolverInitException(
                "The given JSON file path is not valid. Please check arguments")
        if len(self.objects_to_be_collected) == 0:
            raise SolverInitException(
                "The list of objects to be collected is empty. Please check arguments")

    def solve_problem(self):
        '''
        Solves the maze problem using the arguments used to build the Solver class.

        @return A list of tuples that represent each step to find the path to collect all objects
        '''

        # read json string from json file path
        json_string = read_json_string(self.rooms_json_file_path)
        # parse and validate json file
        rooms_dict = build_rooms_dictionary(json_string)
        # iterate over graph to find the path for each object
        result = find_path(rooms_dict, self.starting_room_id,
                           self.objects_to_be_collected)
        # return result
        return result
