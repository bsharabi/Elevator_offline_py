import random
def allocateToElevator(calls, elevators):
    'If there is one elevator, we will insert the same elevator for all readings.'
    if len(elevators) == 1:
        for call in calls:
            call.allocateTo(0)
    else:
        for call in calls:
            call.allocateTo(random.randrange(0,len(elevators)))
          
        pass


def allocate(packet, elevators):
    pass


# Ending stamp calcuating the futere ending stamp includ the new call
def EndingStamp(elevator, call):
    pass


# time to get calcuate the time it take the elvator to go from a given source to the given destination without including the current floor of the elevator 
def TimeToGet(src, dest, elevator): 
    pass