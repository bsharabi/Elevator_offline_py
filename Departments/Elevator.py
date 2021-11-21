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
        self._calls = []
        self.offset = int(self._startTime)+int(self._stopTime) + int(self._openTime)+int(self._closeTime)

    def arrivalTime(self, src, dest):
        if src == dest:
            return 0
        return abs(src-dest)/float(self._speed)+(self.offset)

    def timeToComplete(self,call):
        if not self._calls:
            if call.src == 0:
                return call.timeIn
            return call.timeIn + self.offset + (abs(0 - call.src)) / self._speed
        else:
            if self._calls[-1].endTime > call.timeIn:
                return self._calls[-1].endTime + self.offset + (abs(self._calls[-1].dest - call.src)) / self._speed
            else:
                if self._calls[-1].dest == call.src:
                    return call.timeIn
                return call.timeIn + self.offset + (abs(self._calls[-1].dest - call.src)) / self._speed

    def __repr__(self):
        return f"_id:{self._id} _speed:{self._speed} _minFloor:{self._minFloor} _maxFloor:{self._maxFloor} _closeTime:{self._closeTime} _openTime:{self._openTime} _startTime:{self._startTime} _stopTime:{self._stopTime}"

 
