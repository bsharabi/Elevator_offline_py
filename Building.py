from Elevator import elevator
class build:
    # __init__ - is a keyword to the class constructor
    def __init__(self, obj):
        self._minFloor = obj["_minFloor"]
        self._maxFloor = obj["_maxFloor"]
        self._elevators = []
        for e in obj["_elevators"]:
            self._elevators.append(elevator(e))
