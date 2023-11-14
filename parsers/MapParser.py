import json
from entities.Room import Room, Coordinates


def readJsonString(jsonMapPath):
    '''
    Reads a JSON from the given file path

    @param jsonMapPath path to the JSON file

    @returns a JSON object
    '''
    with open(jsonMapPath, 'r') as data:
        return json.load(data)


def buildCoordinates(room):
    '''
    Build a Coordinate object from the given room

    @param room The rooms that contain the room coordinates

    @returns a Coordinate object
    '''
    return Coordinates(room.get("north"),  room.get("south"), room.get("east"), room.get("west"))


def parseJsonMap(jsonMap):
    '''
    Cornverts the given JSON object to a dictionary of Room objects
    The key for the dictionary is the room ID

    @param jsonMap the JSON object to parse

    @returns a dictionary of Room objects
    '''
    roomsMap = {}
    for room in jsonMap["rooms"]:
        # build a coordinates object
        roomCoords = buildCoordinates(room)
        roomObjs = []
        for obj in room["objects"]:
            roomObjs.append(obj["name"])
        roomObj = Room(room["id"], room["name"], roomCoords, roomObjs)
        roomsMap[room["id"]] = roomObj
    return roomsMap
