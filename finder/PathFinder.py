def getAdjacentRooms(room):
    result = []
    if hasattr(room.coordinates, "north"):
        result.append(roomsDictionary[room.coordinates.north])
    if hasattr(room.coordinates, "south"):
        result.append(roomsDictionary[room.coordinates.south])
    if hasattr(room.coordinates, "east"):
        result.append(roomsDictionary[room.coordinates.east])
    if hasattr(room.coordinates, "west"):
        result.append(roomsDictionary[room.coordinates.west])
    return result

# Check if all items to be searched are found


def checkLeftItems():
    return len(objectsToCollect) == 0


def searchObjects(objsInRoom):
    result = []
    for obj in objsInRoom:
        if obj in objectsToCollect:
            # add found item in resulting list
            result.append(obj)
            # remove the object from the list of objects to be found
            objectsToCollect.remove(obj)
    return result


# This function visits in a recursive manner all rooms connected with the current one
# If no connected rooms are left to visit go back to the previous one adding that to the output path
# room = current room class
# prevRoom = previous room ID in path
# @returns list of tuple(roomId, list[foundObjs])
def visitRoom(room, prevRoom):
    print("visitRoom("+str(room.id) + "," + str(prevRoom)+")")
    print("objs to find: " + str(objectsToCollect))
    # TODO this check should be useless check whether to delete or not
    if checkLeftItems():
        # if all items are found there is no reason to continue with loop
        return
    roomId = room.id
    # TODO maybe too defensive --> this check should be useless
    if not roomId in visitedRooms:
        # add room to visited
        visitedRooms.append(roomId)
        print("visited: " + str(visitedRooms))
        # process room objects
        objsFound = searchObjects(room.objects)
        # update output path with objects found in this room
        resultPath.append((roomId, objsFound))
        if checkLeftItems():
            # if all items are found there is no reason to go deeper in path
            return
        # now get all adjacent rooms
        adjRooms = getAdjacentRooms(room)
        for adjRoom in adjRooms:
            if not adjRoom.id in visitedRooms:
                visitRoom(adjRoom, roomId)
                if checkLeftItems():
                    return
        # if no rooms are left to visit go back to previous room
        if not prevRoom == 0:
            resultPath.append((prevRoom, []))

#
# parsedMap = dictionary in which the key is represented by the roomID


def findPath(parsedMap, startingRoomID, toBeCollectedList):
    global roomsDictionary
    roomsDictionary = parsedMap
    # first room has no previous room
    prevRoom = 0
    # init list of already visited rooms to avoid double visits
    global visitedRooms
    visitedRooms = []
    # init list of items that still needs to be collected
    global objectsToCollect
    objectsToCollect = toBeCollectedList
    # init a dictionary that represents the output path
    global resultPath
    resultPath = []
    # start visiting first room
    visitRoom(parsedMap[int(startingRoomID)], 0)
    return resultPath
