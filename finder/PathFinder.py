from exceptions.MazeExceptions import FinderException


def get_adjacent_rooms(room):
    '''
    Returns the list of rooms adjacent to the given room

    @param room: The room to get the list of adjacent rooms for
    @raise FinderException 
    @return: A list of rooms adjacent to the given room
    '''
    try:
        result = []
        if hasattr(room.coordinates, "north"):
            result.append(rooms_dictionary[room.coordinates.north])
        if hasattr(room.coordinates, "south"):
            result.append(rooms_dictionary[room.coordinates.south])
        if hasattr(room.coordinates, "east"):
            result.append(rooms_dictionary[room.coordinates.east])
        if hasattr(room.coordinates, "west"):
            result.append(rooms_dictionary[room.coordinates.west])
        return result
    except Exception as e:
        raise FinderException(
            "The following error occurred while trying to get the list of rooms adjacent to Room (%s): %s" % (room.name, str(e)))


def check_left_items():
    '''
    Check if there are left items to be collected from rooms

    @returns True if all items are collected, False otherwise
    '''
    return len(objects_to_collect) == 0


def search_objects(objects_in_room):
    '''
    Search for objects to be collected. If the objects in the room match with the objects to be collected, 
    than the objects are collected and removed from the list of objects to collect.

    @param objects_in_room The list of objects in the current room
    @raise FinderException
    @returns The objects in the room that must be collected
    '''

    try:
        result = []
        for obj in objects_in_room:
            if obj in objects_to_collect:
                # add found item in resulting list
                result.append(obj)
                # remove the object from the list of objects to be found
                objects_to_collect.remove(obj)
        return result
    except Exception as e:
        raise FinderException(
            "The following error occurred while processing the objects (%s): %s" % (objects_in_room, str(e)))


def visit_room(room, prev_room_id, prev_room_name=""):
    '''
    Visits in a recursive manner all rooms connected with the current one
    If no connected rooms are left to visit go back to the previous one adding that to the output path

    @param room The current room
    @param prev_room_id Identifier of the previous room
    @param prev_room_name Name of the previous room

    @raise FinderException
    '''
    try:
        room_id = room.id
        room_name = room.name
        if not room_id in visited_rooms:
            # add room to visited
            visited_rooms.append(room_id)
            # process room objects
            objects_found = search_objects(room.objects)
            # update output path with objects found in this room
            result_path.append((room_id, objects_found, room.name))
            if check_left_items():
                # if all items are found there is no reason to go deeper in path
                return
            # now get all adjacent rooms
            adj_rooms = get_adjacent_rooms(room)
            for adj_room in adj_rooms:
                if not adj_room.id in visited_rooms:
                    visit_room(adj_room, room_id, room_name)
                    if check_left_items():
                        return
            # if no rooms are left to visit go back to previous room
            if not prev_room_id == 0:
                result_path.append((prev_room_id, [], prev_room_name))
    except FinderException:
        raise
    except Exception as e:
        raise FinderException(
            "The following error occurred while visiting room %s: %s" % (room.name, str(e)))


def find_path(rooms_dict, starting_room_id, to_be_collected_list):
    '''
    Computes a valid path to find all the items to be collected from a dictionary of rooms starting from the given room ID.

    @param rooms_dict Dictionary of rooms, the Key is the ID of the room
    @param starting_room_id ID of the room where to start the search
    @param to_be_collected_list list of items to be collected
    @raise FinderException
    @returns List of tuple that represents a valid path to collect all items
    '''
    try:
        global rooms_dictionary, visited_rooms, objects_to_collect, result_path
        rooms_dictionary = rooms_dict
        # first room has no previous room
        prev_room_id = 0
        # init list of already visited rooms to avoid double visits
        visited_rooms = []
        # init list of items that still needs to be collected
        objects_to_collect = to_be_collected_list
        # init a list of tuple that represents the output path
        result_path = []
        # start visiting first room
        visit_room(rooms_dict[int(starting_room_id)], prev_room_id)

        if len(objects_to_collect) != 0:
            raise FinderException(
                "There is no valid path to collect all objects. Please check arguments")
        return result_path
    except FinderException:
        raise
