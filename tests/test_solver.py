import pytest

from unittest.mock import patch
import solver.Solver as solver
from exceptions.MazeExceptions import SolverInitException


class TestSolver:

    def test_solver(self):
        rooms_json_file_path = "path/to/rooms.json"
        starting_room_id = 1
        objects_to_be_collected = ["object1", "object2", "object3"]

        solv = solver.Solver(rooms_json_file_path,
                             starting_room_id, objects_to_be_collected)

        assert solv.rooms_json_file_path == rooms_json_file_path
        assert solv.starting_room_id == starting_room_id
        assert solv.objects_to_be_collected == objects_to_be_collected

    def test_solver_invalid_json_file_path(self):
        with pytest.raises(SolverInitException) as e:
            rooms_json_file_path = ""
            starting_room_id = 1
            objects_to_be_collected = ["object1", "object2", "object3"]

            solver.Solver(rooms_json_file_path,
                          starting_room_id, objects_to_be_collected)
        error_string = str(e)
        assert "The given JSON file path is not valid" in error_string

    def test_solver_invalid_objects_to_collect(self):
        with pytest.raises(SolverInitException) as e:
            rooms_json_file_path = "path/to/file.json"
            starting_room_id = 1
            objects_to_be_collected = []

            solver.Solver(rooms_json_file_path,
                          starting_room_id, objects_to_be_collected)
        error_string = str(e)
        assert "The list of objects to be collected is empty" in error_string

    def test_solver_invalid_object(self):
        with pytest.raises(SolverInitException) as e:
            rooms_json_file_path = "path/to/file.json"
            starting_room_id = 1
            objects_to_be_collected = ["object1", ""]

            solver.Solver(rooms_json_file_path,
                          starting_room_id, objects_to_be_collected)
        error_string = str(e)
        assert "An invalid object was encountered in the given object list" in error_string

    @patch('solver.Solver.find_path', autospec=True)
    @patch('solver.Solver.build_rooms_dictionary', autospec=True)
    @patch('solver.Solver.read_json_string', autospec=True)
    def test_solve_problem(self, patched_read_json_string, patched_build_rooms_dictionary, patched_find_path):
        read_json_result = "mocked_json_string"
        build_rooms_dictionary_result = {1: "mocked_room1"}
        find_path_result = ["mocked_step1", "mocked_step2"]

        patched_read_json_string.return_value = read_json_result
        patched_build_rooms_dictionary.return_value = build_rooms_dictionary_result
        patched_find_path.return_value = find_path_result

        rooms_json_file_path = "path/to/rooms.json"
        starting_room_id = 1
        objects_to_be_collected = ["object1", "object2", "object3"]

        solv = solver.Solver(rooms_json_file_path,
                             starting_room_id, objects_to_be_collected)
        result = solv.solve_problem()

        assert result == find_path_result
        patched_read_json_string.assert_called_once_with(rooms_json_file_path)
        patched_build_rooms_dictionary.assert_called_once_with(
            read_json_result)
        patched_find_path.assert_called_once_with(
            build_rooms_dictionary_result, starting_room_id, objects_to_be_collected)
