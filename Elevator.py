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
        self._severalFloors = abs(self._maxFloor-self._minFloor)
        self._direction = 0
        self._timeComplete = 0
        self._calls = []
        self.offset = int(self._startTime)+int(self._stopTime) + int(self._openTime)+int(self._closeTime)
        self._position = self.setGraphTime(0)

    def setGraphTime(self,timeIn):
        return [[self.arrivalTime(i, j,timeIn) for j in range(self._severalFloors)] for i in range(self._severalFloors)]

    def arrivalTime(self, src, dest,timeIn):
        if src == dest:
            return 0
        countCall=len(self._calls) if len(self._calls)>0 else 1
        return abs(src-dest)/float(self._speed)+(self.offset)*countCall+timeIn

    def getTimeToArrive(self, src, dest,timeIn):
        self._position=self.setGraphTime(timeIn)
        if src < 0:
            src = src % abs(self._minFloor)
        else:
            src += abs(self._minFloor)
        if(dest < 0):
            dest = dest % abs(self._minFloor)
        else:
            dest += abs(self._minFloor)   
        return self._position[src][dest]

    def __repr__(self):
        return f"_id:{self._id} _speed:{self._speed} _minFloor:{self._minFloor} _maxFloor:{self._maxFloor} _closeTime:{self._closeTime} _openTime:{self._openTime} _startTime:{self._startTime} _stopTime:{self._stopTime}"
