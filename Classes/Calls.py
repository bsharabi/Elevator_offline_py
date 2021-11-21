class calls:
    # __init__ - is a keyword to the class constructor
    def __init__(self, Call):
        self.name = Call[0]
        self.timeIn = float(Call[1])
        self.src = int(Call[2])
        self.dest = int(Call[3])
        self._allocateTo = int(Call[5])
        self.flag = int(Call[4])
        self.endTime  =0

    def toString(self):
        return str(self.name), str(self.timeIn), str(self.src), str(self.dest), str(self.flag), str(self._allocateTo)

    def __str__(self): 
        return f"{self.name},{self.timeIn},{self.src},{self.dest},{self.flag},{self._allocateTo}"

    def allocateTo(self, numberElevator):
        self._allocateTo = numberElevator

