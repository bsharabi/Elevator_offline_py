class calls:
    id=0
    # __init__ - is a keyword to the class constructor
    def __init__(self, Call):
        self.name = Call[0]
        self.timeIn = float(Call[1])
        self.src = int(Call[2])
        self.dest = int(Call[3])
        self.allocateTo = int(Call[5])
        self.flag = int(Call[4])
        calls.id +=1 
        self.diraction = ((self.dest-self.src)>0);

    def toString(self):
        return str(self.name),str(self.timeIn),str(self.src),str(self.dest),str(self.flag),str(self.allocateTo)
    
    def allocateTo(self,numberElevator):
        self.allocateTo=numberElevator;
    