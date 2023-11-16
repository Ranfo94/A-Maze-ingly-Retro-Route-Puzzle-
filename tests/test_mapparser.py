import pytest

import parsers.MapParser as parser
from unittest.mock import patch
from exceptions.MazeExceptions import ParserException


class TestParser:

    def test_read_json_string(self):
        test_maze_path = "tests/src/test_maze.json"
        result = parser.read_json_string(test_maze_path)

        room_1 = result["rooms"][0]
        room_2 = result["rooms"][1]

        assert len(result["rooms"]) == 2
        assert room_1["id"] == 1
        assert room_1["name"] == "Test Room 1"
        assert room_1["north"] == 2
        assert len(room_1["objects"]) == 0
        assert room_2["id"] == 2
        assert room_2["name"] == "Test Room 2"
        assert room_2["south"] == 1
        assert len(room_2["objects"]) == 1
        assert room_2["objects"][0]["name"] == "test_object"

    @patch('parsers.MapParser.json.load', autospec=True)
    def test_read_json_string_exception(self, patched_load):
        with pytest.raises(ParserException) as e:
            patched_load.side_effect = ValueError("test error")
            test_maze_path = "tests/src/test_maze.json"
            parser.read_json_string(test_maze_path)
        error_string = str(e)
        assert "test error" in error_string
        assert "The following error occurred while reading the file at path" in error_string
        assert test_maze_path in error_string
        patched_load.assert_called_once()

    def test_build_coordinates(self):
        room_json = {}
        room_json["north"] = 2
        room_json["south"] = 3
        room_json["west"] = 4
        room_json["east"] = 5
        result = parser.build_coordinates(room_json)

        assert result.north == 2
        assert result.south == 3
        assert result.west == 4
        assert result.east == 5

    @patch('parsers.MapParser.Coordinates', autospec=True)
    def test_build_coordinates_exception(self, patched_coordinates):
        with pytest.raises(ParserException) as e:

            patched_coordinates.side_effect = ValueError("test error")

            room_json = {}
            room_json["north"] = 2
            room_json["south"] = 3
            room_json["west"] = 4
            room_json["east"] = 5

            parser.build_coordinates(room_json)

        error_string = str(e)
        patched_coordinates.assert_called_once_with(2, 3, 5, 4)
        assert "test error" in error_string
        assert "The following error occurred while creating the Coordinate object" in error_string

    def test_build_rooms_dictionary(self):
        test_maze_path = "tests/src/test_maze.json"
        rooms_json_string = parser.read_json_string(test_maze_path)
        result = parser.build_rooms_dictionary(rooms_json_string)

        assert result[1].id == 1
        assert result[1].name == "Test Room 1"
        assert result[1].coordinates.north == 2
        assert len(result[1].objects) == 0

        assert result[2].id == 2
        assert result[2].name == "Test Room 2"
        assert result[2].coordinates.south == 1
        assert len(result[2].objects) == 1
        assert result[2].objects[0] == "test_object"

    @patch('parsers.MapParser.build_coordinates', autospec=True)
    def test_build_rooms_dictionary_exception(self, patched_coordinates):
        with pytest.raises(ParserException) as e:
            patched_coordinates.side_effect = ValueError("test_error")
            test_maze_path = "tests/src/test_maze.json"
            rooms_json_string = parser.read_json_string(test_maze_path)
            parser.build_rooms_dictionary(rooms_json_string)
        error_string = str(e)
        assert "test_error" in error_string
        assert "The following error occurred while building the Rooms dictionary from" in error_string
        patched_coordinates.assert_called_once()
