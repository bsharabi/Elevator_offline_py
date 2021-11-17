class elevator:
    # __init__ - is a keyword to the class constructor
    def __init__(self, elevatotObj):
        self._id=elevatotObj["_id"]
        self._speed=elevatotObj["_speed"]
        self._minFloor=elevatotObj["_minFloor"]
        self._maxFloor=elevatotObj["_maxFloor"]
        self._closeTime=elevatotObj["_closeTime"]
        self._openTime=elevatotObj["_openTime"]
        self._startTime=elevatotObj["_startTime"]
        self._stopTime=elevatotObj["_stopTime"]
        
