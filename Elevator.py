import time
class elevator:
    '''This department is responsible for building an object for each elevator and placing
    the values according to the file describing the elevators.'''
    # __init__ - is a keyword to the class constructor

    def __init__(self, elevatotObj):
        self._id = elevatotObj["_id"]
        self._speed = elevatotObj["_speed"]
        self._minFloor = elevatotObj["_minFloor"]
        self._maxFloor = elevatotObj["_maxFloor"]
        self._closeTime = elevatotObj["_closeTime"]
        self._openTime = elevatotObj["_openTime"]
        self._startTime = elevatotObj["_startTime"]
        self._stopTime = elevatotObj["_stopTime"]
        self._direction = 0
        self._timeComplete = 0
        self._calls = []
        self._position = 0

    def __repr__(self):
        return f"_id:{self._id} _speed:{self._speed} _minFloor:{self._minFloor} _maxFloor:{self._maxFloor} _closeTime:{self._closeTime} _openTime:{self._openTime} _startTime:{self._startTime} _stopTime:{self._stopTime}"

    def setPos(self):
        pass
    def getPos(self):
        pass

    def whereIsElevatorwhile(self, sec):

        pass

    def calcPos(self):
        pass

    def arrivalTime(self, src, dest):
        return abs(src-dest)/int(self._speed) + int(self._startTime)+int(self._stopTime)

    def setDirectionComplete(self):
        self._direction = 0
        self._timeComplete = time()
