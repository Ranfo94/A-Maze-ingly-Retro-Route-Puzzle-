class Room:
    '''
    Class defining Rooms properties
    '''

    def __init__(self, id, name, coordinates, objs):
        '''
        Constructor for Room
        @param id : Room identifier
        @param name : Room name
        @param coordinates : Room coordinates object
        @param objs : List of objects placed in the rooms
        '''
        self.id = id
        self.name = name
        self.coordinates = coordinates
        self.objects = objs


class Coordinates:
    '''
    This class represent the geographical position of a Room
    Each of the coordinates below correspond to a specific room ID 
    '''

    def __init__(self, north=None, south=None, east=None, west=None):
        '''
        Constructor for the Coordinates class

        @param north : North Room identifier
        @param south : South Room identifier
        @param east : East Room identifier
        @param west : West Room identifier
        '''
        if not north == None:
            self.north = north
        if not south == None:
            self.south = south
        if not east == None:
            self.east = east
        if not west == None:
            self.west = west
