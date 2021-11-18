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
        self.endingstamp=0
        self.diraction=0
        self.calls= []
        self.offset= self._openTime+self._closeTime+self._startTime+self._stopTime
