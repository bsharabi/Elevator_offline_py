from sys import float_info as Float
def allocateToElevator(calls, elevators):
    'If there is one elevator, we will insert the same elevator for all calls.'
    if len(elevators) == 1:
        for call in calls:
            call.allocateTo(0)
    else:
        timeComplete = 0
        bestMatchElevator = -1
        for call in calls:
            minTime = Float.max
            for elevator in elevators:
                tTc=elevator.timeToComplete(call)
                if tTc < minTime:
                    bestMatchElevator = elevator._id
                    minTime = tTc
                    timeComplete = minTime+1 +elevator.arrivalTime(call.src,call.dest)
            call.allocateTo(bestMatchElevator)
            call.endTime = timeComplete
            elevators[bestMatchElevator]._calls.append(call)