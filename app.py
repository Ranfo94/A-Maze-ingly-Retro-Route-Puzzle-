import sys
from parsers.MapParser import build_rooms_dictionary, read_json_string
from finder.PathFinder import find_path


def solve_problem(maze_file_path, starting_room_id, to_be_collected_list):
    # read json string from json file path
    json_string = read_json_string(maze_file_path)
    # parse and validate json file
    parsed_rooms = build_rooms_dictionary(json_string)
    # iterate over graph to find the path for each object
    result = find_path(parsed_rooms, starting_room_id, to_be_collected_list)
    # return result
    return result


def print_solution(problem_solution):
    '''
    Print the maze problem's solution in the right format. 

    @param problem_solution A list of tuple that represents the solution of the problem 
    '''
    for step in problem_solution:
        room_name = step[2]
        room_objs_string = ""
        for obj in step[1]:
            room_objs_string += str(obj) + " "
        if room_objs_string == "":
            room_objs_string = "None"
        print("Room Name: %s , Objects Collected: %s" % (
            str(room_name), room_objs_string))


if __name__ == "__main__":
    if len(sys.argv) < 4:
        # function can only be launched with 3 params
        print("Error using script. At least 3 params must be specified")
        # TODO finish this
        exit(1)
    maze_file_path = sys.argv[1]
    starting_room_id = sys.argv[2]
    # from third argument put all
    to_be_collected_list = sys.argv[3:]

    result = solve_problem(
        maze_file_path, starting_room_id, to_be_collected_list)
    print_solution(result)
