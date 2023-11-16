class SolverInitException(Exception):
    '''
    Raised when an error occurs during the initialization of a Solver class instance.
    '''
    pass


class ParserException(Exception):
    '''
    Raised when an error occurs during the parsing of a JSON Maze file to a dictionary of Rooms 
    '''
    pass


class FinderException(Exception):
    '''
    Raised when an error occurs during the search for the path to find all required objects in the rooms
    '''
    pass
