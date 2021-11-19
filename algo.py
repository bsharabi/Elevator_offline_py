import random
def allocateToElevator(calls, elevators):
    'If there is one elevator, we will insert the same elevator for all readings.'
    if len(elevators) == 1:
        for call in calls:
            call.allocateTo(0)
    else:
        numElevator=0
        minTime=0
        for index,call in enumerate(calls):
            for elv in elevators:                
                pass
        
        print(elevators[0].getTimeToArrive(calls[0].src,calls[0].dest,calls[0].timeIn))
          
        pass


def allocate(packet, elevators):
    pass


# Ending stamp calcuating the futere ending stamp includ the new call
def EndingStamp(elevator, call):
    pass


# time to get calcuate the time it take the elvator to go from a given source to the given destination without including the current floor of the elevator 
def TimeToGet(src, dest, elevator): 
    pass