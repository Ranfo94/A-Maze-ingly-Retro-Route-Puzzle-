import sys
import argparse

from solver.Solver import Solver
import exceptions.MazeExceptions as exceptions


def handle_exception(error_string):
    print(error_string)
    exit(1)


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
    try:
        parser = argparse.ArgumentParser(prog="Maze Puzzle",
                                         description='This program solves the Maze Puzzle')

        parser.add_argument('path', type=str,
                            help='JSON file containing the rooms definition')
        parser.add_argument('id', type=int,
                            help='Identifier of the starting room')
        parser.add_argument('objects', nargs='+', type=str,
                            help='Space separated list of objects to be collected from the rooms')

        args = parser.parse_args()

        rooms_json_file_path = args.path
        starting_room_id = args.id
        input_object_list = args.objects

        to_be_collected_list = []
        for obj in input_object_list:
            to_be_collected_list.append(obj.strip())

        solver = Solver(rooms_json_file_path,
                        starting_room_id, to_be_collected_list)

        result = solver.solve_problem()
        print_solution(result)
    except exceptions.SolverInitException as e:
        handle_exception(str(e))
    except exceptions.FinderException as e:
        handle_exception(str(e))
    except exceptions.ParserException as e:
        handle_exception(str(e))
    except Exception as e:
        handle_exception(
            "A generic error occurred while solving the problem. Please contact the developers")
