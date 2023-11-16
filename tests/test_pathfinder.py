import pytest

from unittest.mock import patch
from exceptions.MazeExceptions import FinderException

from entities.Room import Room, Coordinates
import finder.PathFinder as finder


class TestPathfinder:

    def test_get_adjacent_rooms(self):
        finder.rooms_dictionary = {
            2: Room(2, "test_adj_room", Coordinates(south=1), [])}

        coords = Coordinates(north=2)
        room = Room(1, "test room", coords, [])
        result = finder.get_adjacent_rooms(room)

        assert result[0].id == 2
        assert result[0].name == "test_adj_room"
        assert result[0].coordinates.south == 1
        assert result[0].objects == []

    def test_get_adjacent_rooms_exception(self):
        with pytest.raises(FinderException) as e:
            finder.rooms_dictionary = {}
            coords = Coordinates(north=2)
            room = Room(1, "test room", coords, [])
            finder.get_adjacent_rooms(room)
        error_string = str(e)
        assert "The following error occurred while trying to get the list of rooms adjacent to Room" in error_string

    def test_check_left_items_not_empty(self):
        finder.objects_to_collect = ["obj1", "obj2"]
        result = finder.check_left_items()
        assert result == False

    def test_check_left_items_empty(self):
        finder.objects_to_collect = []
        result = finder.check_left_items()
        assert result == True

    def test_search_objects(self):
        objects_in_room = ["obj1", "obj2"]
        finder.objects_to_collect = ["obj1", "obj3"]
        result = finder.search_objects(objects_in_room)

        assert len(result) == 1
        assert result[0] == "obj1"
        assert len(finder.objects_to_collect) == 1
        assert finder.objects_to_collect[0] == "obj3"

    def test_visit_room(self):
        room1 = Room(1, "test room", Coordinates(north=2), [])
        room2 = Room(2, "test room", Coordinates(south=1), ["obj1"])

        finder.visited_rooms = []
        finder.result_path = []
        finder.rooms_dictionary = {}
        finder.rooms_dictionary[1] = room1
        finder.rooms_dictionary[2] = room2
        finder.objects_to_collect = ["obj1"]

        finder.visit_room(room1, 0)

        assert len(finder.visited_rooms) == 2
        assert finder.visited_rooms[0] == room1.id
        assert finder.visited_rooms[1] == room2.id
        assert len(finder.objects_to_collect) == 0
        assert len(finder.result_path) == 2
        assert finder.result_path[0][0] == room1.id
        assert len(finder.result_path[0][1]) == 0
        assert finder.result_path[0][2] == room1.name
        assert finder.result_path[1][0] == room2.id
        assert len(finder.result_path[1][1]) == 1
        assert finder.result_path[1][1][0] == "obj1"
        assert finder.result_path[1][2] == room2.name

    @patch('finder.PathFinder.search_objects', autospec=True)
    def test_visit_room_exception(self, patched_search):
        with pytest.raises(FinderException) as e:
            patched_search.side_effect = ValueError("Error in search")

            room1 = Room(1, "test room", Coordinates(north=2), [])
            room2 = Room(2, "test room", Coordinates(south=1), ["obj1"])

            finder.visited_rooms = []
            finder.result_path = []
            finder.rooms_dictionary = {}
            finder.rooms_dictionary[1] = room1
            finder.rooms_dictionary[2] = room2
            finder.objects_to_collect = ["obj1"]

            finder.visit_room(room1, 0)

        error_string = str(e)
        assert "Error in search" in error_string
        assert "The following error occurred while visiting room" in error_string
        assert "test room" in error_string
        patched_search.assert_called_once()

    def test_find_path(self):
        room1 = Room(1, "test room 1", Coordinates(north=2), [])
        room2 = Room(2, "test room 2", Coordinates(south=1), ["obj1"])

        rooms_dictionary = {}
        rooms_dictionary[1] = room1
        rooms_dictionary[2] = room2
        starting_room_id = 1
        to_be_collected_list = ["obj1"]

        result = finder.find_path(rooms_dictionary, starting_room_id,
                                  to_be_collected_list)

        assert len(result) == 2
        assert result[0][0] == room1.id
        assert len(result[0][1]) == 0
        assert result[0][2] == room1.name
        assert result[1][0] == room2.id
        assert len(result[1][1]) == 1
        assert result[1][1][0] == "obj1"
        assert result[1][2] == room2.name

    def test_find_path(self):
        room1 = Room(1, "test room 1", Coordinates(north=2), [])
        room2 = Room(2, "test room 2", Coordinates(south=1), ["obj1"])

        rooms_dictionary = {}
        rooms_dictionary[1] = room1
        rooms_dictionary[2] = room2
        starting_room_id = 1
        to_be_collected_list = ["obj1"]

        result = finder.find_path(rooms_dictionary, starting_room_id,
                                  to_be_collected_list)

        assert len(result) == 2
        assert result[0][0] == room1.id
        assert len(result[0][1]) == 0
        assert result[0][2] == room1.name
        assert result[1][0] == room2.id
        assert len(result[1][1]) == 1
        assert result[1][1][0] == "obj1"
        assert result[1][2] == room2.name

    def test_find_path_objects_left(self):
        with pytest.raises(FinderException) as e:
            room1 = Room(1, "test room 1", Coordinates(north=2), [])
            room2 = Room(2, "test room 2", Coordinates(south=1), ["obj1"])

            rooms_dictionary = {}
            rooms_dictionary[1] = room1
            rooms_dictionary[2] = room2
            starting_room_id = 1
            to_be_collected_list = ["obj1", "obj3"]

            finder.find_path(rooms_dictionary, starting_room_id,
                             to_be_collected_list)
        error_string = str(e)
        assert "There is no valid path to collect all objects" in error_string

    @patch('finder.PathFinder.visit_room', autospec=True)
    def test_find_path_exception(self, patched_visit_room):
        with pytest.raises(FinderException) as e:
            patched_visit_room.side_effect = FinderException(
                "Error in visit room")

            room1 = Room(1, "test room 1", Coordinates(north=2), [])
            room2 = Room(2, "test room 2", Coordinates(south=1), ["obj1"])

            rooms_dictionary = {}
            rooms_dictionary[1] = room1
            rooms_dictionary[2] = room2
            starting_room_id = 1
            to_be_collected_list = ["obj1"]

            finder.find_path(rooms_dictionary, starting_room_id,
                             to_be_collected_list)
        error_string = str(e)
        assert "Error in visit room" in error_string
        patched_visit_room.assert_called_once()
