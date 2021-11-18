import math
import sys


def folder(calls):
    for x in calls:
        packet =[x]
        for i in range(1,len(calls)):
            if(x.diraction and calls[i].dir==1):
                if(x.dest<=calls[i].src):
                    packet.append(i)
                    del calls[i]
                if(math.abs(x.dest-calls[i].src<=1)and (calls[i].timeIn-x.timeIn)<=6):
                    packet.append(i)
                    del calls[i]
                allocate(packet)
                
            if(x.diraction and calls[i].diraction==-1):
                if(x.dest>=calls[i].src):
                    packet.append(i)
                    del calls[i]
                if(math.abs(x.dest-calls[i].src<=1)and (calls[i].timeIn-x.timeIn)<=6):
                    packet.append(i)
                    del calls[i]
                allocate(packet)        
   
def allocate(packet ,elevators):
    temp =0; 
    bestMatch = [sys.maxsize,-1]
    for x in elevators:
        for i in packet:
            temp =EndingStamp(x,packet[i])
            if (temp<bestMatch[0] ): 
                bestMatch=[temp,x] 
    for i in packet:        
        bestMatch[1].calls.appaned[i]
    bestMatch[1].EndingTime=temp;  


def EndingStamp(elevator,call):  ## Ending stamp calcuating the futere ending stamp includ the new call
    current = elevator.endingstamp
    return current +TimeToGet(elevator.calls[len(elevator.calls)].dest,call.src,elevator)+TimeToGet (call.src,call.dest,elevator)
        


def TimeToGet(src,dest,elevator):   ## time to get calcuate the time it take the elvator to go from a given source to the given destination without including the current floor of the elevator
    return (elevator.speed*math.abs(dest-src)+elevator.offset)


        

    

