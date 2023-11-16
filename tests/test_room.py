import pytest

from entities.Room import Room, Coordinates


class TestRoom:

    def test_coordinates(self):
        north = 1
        south = 10
        east = 8
        west = 5

        coord = Coordinates(north=north, south=south, east=east, west=west)

        assert coord.north == north
        assert coord.south == south
        assert coord.east == east
        assert coord.west == west

    def test_room(self):
        north = 1
        south = 10
        east = 8
        west = 5

        coord = Coordinates(north=north, south=south, east=east, west=west)

        room_id = 4
        name = "Test room"
        objects = ["object1", "object2", "object3", "object4"]

        room = Room(id=room_id, name=name, coordinates=coord, objs=objects)

        assert room.id == room_id
        assert room.name == name
        assert room.coordinates.north == north
        assert room.coordinates.south == south
        assert room.coordinates.east == east
        assert room.coordinates.west == west
        assert room.objects == objects
