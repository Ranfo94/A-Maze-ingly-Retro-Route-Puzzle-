import json
from entities.Room import Room, Coordinates


def readJsonString(jsonMapPath):
    with open(jsonMapPath, 'r') as data:
        return json.load(data)


def buildCoordinates(room):
    return Coordinates(room.get("north"),  room.get("south"), room.get("east"), room.get("west"))


def parseJsonMap(jsonMap):
    '''
    parse the json string to a map of rooms.
    The key is the room id
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
