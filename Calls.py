class calls:
    id=0
       # __init__ - is a keyword to the class constructor
    def __init__(self, listCall):
        self.name=  listCall[0] + str(calls.id)
        self.timeIn=float(listCall[1])
        self.src =int(listCall[2])
        self.dest=int(listCall[3])
        self.allocateTo=int(listCall[5])
        calls.id +=1 
    pass