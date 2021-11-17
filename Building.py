from Calls import calls
from Elevator import elevator
class build:
    # __init__ - is a keyword to the class constructor
    def __init__(self, obj,callsList):
        self._minFloor = obj["_minFloor"]
        self._maxFloor = obj["_maxFloor"]
        self._elevators = []
        self._calls=[]
        for e in obj["_elevators"]:
            self._elevators.append(elevator(e))
        for c in callsList:
            self._calls.append(calls(c))
        
