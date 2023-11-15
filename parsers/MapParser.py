import json
from entities.Room import Room, Coordinates
from exceptions.MazeExceptions import ParserException


def read_json_string(rooms_json_path):
    '''
    Reads a JSON from the given file path

    @param rooms_json_path path to the JSON file containing the rooms definitions
    @raise ParserException If an error is encountered while reading the JSON file
    @returns a JSON object
    '''
    try:
        with open(rooms_json_path, 'r') as data:
            return json.load(data)
    except Exception as e:
        raise ParserException(
            "The following error occurred while reading the file at path %s: %s" % (rooms_json_path, e))


def build_coordinates(room):
    '''
    Build a Coordinate object from the given room

    @param room The rooms that contain the room coordinates
    @raise ParserException If an error is encountered while building the coordinates
    @returns a Coordinate object
    '''
    try:
        return Coordinates(room.get("north"),  room.get("south"), room.get("east"), room.get("west"))
    except Exception as e:
        raise ParserException(
            "The following error occurred while creating the Coordinate object : %s" % (str(e)))


def build_rooms_dictionary(rooms_json_string):
    '''
    Cornverts the given JSON string to a dictionary of Room objects
    The key for the dictionary is the room ID

    @param rooms_json_string A JSON string containing the rooms definitions
    @raise ParserException if an error occurrs while building the rooms dict
    @returns a dictionary of Room objects
    '''
    try:
        rooms_dict = {}
        for room in rooms_json_string["rooms"]:
            # build a coordinates object
            room_coords = build_coordinates(room)
            objs_in_room = []
            for obj in room["objects"]:
                objs_in_room.append(obj["name"])
            room_cls = Room(room["id"], room["name"],
                            room_coords, objs_in_room)
            rooms_dict[room["id"]] = room_cls
        return rooms_dict
    except Exception as e:
        raise ParserException("The following error occurred while building the Rooms dictionary from %s : %s" % (
            rooms_json_string, str(e)))
