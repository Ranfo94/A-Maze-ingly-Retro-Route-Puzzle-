def getAdjacentRooms(room):
    '''
    Returns the list of rooms adjacent to the given room

    @param room: The room to get the list of adjacent rooms for

    @return: A list of rooms adjacent to the given room
    '''
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


def checkLeftItems():
    '''
    Check if there are left items to be collected from rooms

    @returns True if all items are collected, False otherwise
    '''
    return len(objectsToCollect) == 0


def searchObjects(objsInRoom):
    '''
    Search for objects to be collected. If the objects in the room match with the objects to be collected, 
    than the objects are collected and removed from the list of objects to collect.

    @param objsInRoom The list of objects in the current room

    @returns The objects in the room that must be collected
    '''
    result = []
    for obj in objsInRoom:
        if obj in objectsToCollect:
            # add found item in resulting list
            result.append(obj)
            # remove the object from the list of objects to be found
            objectsToCollect.remove(obj)
    return result


def visitRoom(room, prevRoomId, prevRoomName=""):
    '''
    Visits in a recursive manner all rooms connected with the current one
    If no connected rooms are left to visit go back to the previous one adding that to the output path

    @param room The current room
    @prevRoomId Identifier of the previous room
    @prevRoomName Name of the previous room
    '''

    print("visitRoom("+str(room.id) + "," + str(prevRoomId)+")")
    print("objs to find: " + str(objectsToCollect))
    # TODO this check should be useless check whether to delete or not
    if checkLeftItems():
        # if all items are found there is no reason to continue with loop
        return
    roomId = room.id
    roomName = room.name
    # TODO maybe too defensive --> this check should be useless
    if not roomId in visitedRooms:
        # add room to visited
        visitedRooms.append(roomId)
        print("visited: " + str(visitedRooms))
        # process room objects
        objsFound = searchObjects(room.objects)
        # update output path with objects found in this room
        resultPath.append((roomId, objsFound, room.name))
        if checkLeftItems():
            # if all items are found there is no reason to go deeper in path
            return
        # now get all adjacent rooms
        adjRooms = getAdjacentRooms(room)
        for adjRoom in adjRooms:
            if not adjRoom.id in visitedRooms:
                visitRoom(adjRoom, roomId, roomName)
                if checkLeftItems():
                    return
        # if no rooms are left to visit go back to previous room
        if not prevRoomId == 0:
            resultPath.append((prevRoomId, [], prevRoomName))


def findPath(parsedMap, startingRoomID, toBeCollectedList):
    '''
    Computes a valid path to find all the items to be collected from a dictionary of rooms starting from the given room ID.

    @param parsedMap Dictionary of rooms, the Key is the ID of the room
    @param startingRoomID ID of the room where to start the search
    @param toBeCollectedList list of items to be collected

    @returns List of tuple that represents a valid path to collect all items
    '''

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
    # init a list of tuple that represents the output path
    global resultPath
    resultPath = []
    # start visiting first room
    visitRoom(parsedMap[int(startingRoomID)], 0)
    return resultPath
