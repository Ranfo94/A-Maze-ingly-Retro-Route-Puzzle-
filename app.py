import sys
from parsers.MapParser import parseJsonMap, readJsonString
from finder.PathFinder import findPath


def solveProblem(jsonMapPath, startingRoomID, toBeCollectedList):
    # read json string from json file path
    jsonString = readJsonString(jsonMapPath)
    # parse and validate json file
    parsedRooms = parseJsonMap(jsonString)
    # iterate over graph to find the path for each object
    result = findPath(parsedRooms, startingRoomID, toBeCollectedList)
    # return result
    print(result)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        # function can only be launched with 3 params
        print("Error using script. At least 3 params must be specified")
        # TODO finish this
        exit(1)
    jsonMapPath = sys.argv[1]
    startingRoomID = sys.argv[2]
    # from third argument put all
    toBeCollectedList = sys.argv[3:]
    # TODO delete this
    print(str(jsonMapPath) + " " + str(startingRoomID) +
          " " + str(toBeCollectedList))
    solveProblem(jsonMapPath, startingRoomID, toBeCollectedList)
