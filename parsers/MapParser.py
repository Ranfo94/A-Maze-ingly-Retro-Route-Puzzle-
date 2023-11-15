import json
from entities.Room import Room, Coordinates


def read_json_string(rooms_json_path):
    '''
    Reads a JSON from the given file path

    @param rooms_json_path path to the JSON file containing the rooms definitions

    @returns a JSON object
    '''
    with open(rooms_json_path, 'r') as data:
        return json.load(data)


def build_coordinates(room):
    '''
    Build a Coordinate object from the given room

    @param room The rooms that contain the room coordinates

    @returns a Coordinate object
    '''
    return Coordinates(room.get("north"),  room.get("south"), room.get("east"), room.get("west"))


def build_rooms_dictionary(rooms_json_string):
    '''
    Cornverts the given JSON string to a dictionary of Room objects
    The key for the dictionary is the room ID

    @param rooms_json_string A JSON string containing the rooms definitions

    @returns a dictionary of Room objects
    '''
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
