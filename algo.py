
import sys
import math
import copy
import Elevator
size = 0

def ima_shel_boaz_zona(list, elevator):
    counter =0;
    for i in range(len(list)):
        if (list[i==elevator]):
            return i+1
    
def folder(calls, elevators):
    size = len(calls)
    bestElv=-1
    bestTime=sys.maxsize
    endDest=0
    minOpeningTime=sys.maxsize
    minOffset=sys.maxsize
    tempCalls =copy.deepcopy(calls)
    for x in elevators:
        if (x._openTime<=minOpeningTime):
            minOpeningTime=x._openTime
        if (x.offset<minOffset):
            minOffset=x.offset
            
    for x in tempCalls:
        packet = [x] 
        tempCalls.remove(x)
        k=0
        while (k<1):
            for i in tempCalls:
                
            
            
                if (x.diraction ==1 and i.diraction ==1): #this condition chack if both of the calls are in the same diraction
                    if(x.dest>i.src):   
                        # print("upppppppppppppppppp")
                        # print(x.src,"------>",x.dest)
                        # print(i.src,"------>",i.dest)
                        distance = x.dest-i.src
                        
                    
                        if ((i.timeIn-x.timeIn)<=minOffset):
                            packet.append(i)
                            tempCalls.remove(i)
                            endDest= max(x.dest,i.dest)
                    elif(x.dest==i.src):
                        if ((i.timeIn-x.timeIn)<=minOffset):
                            packet.append(i)
                            tempCalls.remove(i)
                            endDest= max(x.dest,i.dest)
            
                    elif(x.src==i.src):                       
            
                        if((i.timeIn-x.timeIn)<=minOffset): #***if the futre calls are at the same floor this condition chacks if the futre call well get before the elevator close the door***
                            packet.append(i)
                            tempCalls.remove(i) 
                            endDest= max(x.dest,i.dest)
                    # --------------------------------and now for the down calls-----------------------------
                        
                elif(x.diraction ==-1 and i.diraction==-1):
                    # print("downnnnnnnnnnnnnnnnnnn")
                    
                    # print(x.src,"------>",x.dest)
                    # print(i.src,"------>",i.dest)
                    if(x.dest > i.src):
                       if ((i.timeIn-x.timeIn)<=minOffset):
                            packet.append(i)
                            tempCalls.remove(i) 
                            endDest= min(x.dest,i.dest) 

                    elif(x.dest==i.src):
                        if ((i.timeIn-x.timeIn)<=minOffset):
                    
                            packet.append(i)
                            
                            tempCalls.remove(i) 
                            
                               
                        

                                
                            
                            endDest= max(x.dest,i.dest)
            k+=1            
            allocate(packet,elevators)
               
                            
            
        
           
        
        
        # for x in calls:
    #     i=ima_shel_boaz_zona(calls,x)
    #     packet = [x]       
        
    #     while i < size:
    #         try:
    #             print(x.diraction, calls[i].diraction)
    #             print(x.src ,"---->" ,x.dest ,"\n"+calls[i].src,"------>"+calls[i].dest  )
    #             if(x.diraction ==1 and calls[i].diraction ==1):
    #                 print("-----------------------FirstIf------------------------------")
    #                 if(x.dest <= calls[i].src):
    #                     packet.append(calls[i])
    #                     del calls[i]
    #                     i += 1
                        
    #                     print("-----------------------FirstUp------------------------------")
    #                     continue
    #                 if(abs(x.dest-calls[i].src <= 1) and (calls[i].timeIn-x.timeIn) <= 10):
    #                     pack
    #                     e+t.append(calls[i])
    #                     del calls[i]
    #                     i += 1
                        
    #                     print("-----------------------secoendUp------------------------------")
    #                     continue
    #                 i+=1
    #                 print("FUCK")
    #             allocate(packet, elevators)

    #             if(x.diraction ==-1 and calls[i].diraction==-1 ):
    #                 print("-----------------------secoend if------------------------------")
    #                 print(x.dest, calls[i].src,"-----------------")
    #                 if(x.dest >= calls[i].src):
    #                     packet.append(calls[i])
    #                     del calls[i]
    #                     i += 1
    #                     print("-----------------------firs down------------------------------")
    #                         continue
                    
    #                 elif(abs(x.dest-calls[i].src <= 1) and (calls[i].timeIn-x.timeIn) <= 10):
    #                     packet.append(calls[i])
    #                     del calls[i]
    #                     i += 1
                        
    #                     print("-----------------------SecoendDOWN------------------------------")
    #                     continue
    #                 i+=1
    #                 print("fuck")
    #                 allocate(packet, elevators)
                    

                
    #             i += 1
    #         except :
    #            print(i,len(calls))
    #            break


def allocate(packet, elevators):
    temp = 0
    bestTime=sys.maxsize
    id=0
    bestElev=-1
    bestMatch = [sys.maxsize, -1]
    for x in elevators:
        temp = x.calls+packet
        for i in packet:
           
            tempTime=EndingStamp(x,i)   
            if(tempTime<bestTime):
                bestElev=x
                bestTime=tempTime
                print("bestTime=",bestTime,x._id)
               
       
    print("----------------------------------")
    for i in packet:
        
        i.allocateTo(bestElev._id)
        bestElev.endingstamp=EndingStamp(x,i)
        bestElev.calls.append(i)
        print(i.src,"------>",i.dest,"TimeIn",i.timeIn)
    print(bestElev._id)
    print("----------------------------------")
   


# Ending stamp calcuating the futere ending stamp includ the new call
def EndingStamp(elevator, call):
    current = elevator.endingstamp
    counter=0
    if(len(elevator.calls) == 0):
    
        return TimeToGet(0, call.dest, elevator)+TimeToGet(call.src, call.dest, elevator)
    
    return current + TimeToGet(elevator.calls[len(elevator.calls)-1].dest, call.src, elevator)+TimeToGet(call.src, call.dest, elevator)



def TimeToGet(src, dest, elevator):  # time to get calcuate the time it take the elvator to go from a given source to the given destination without including the current floor of the elevator
    return (elevator._speed*abs(dest-src)+elevator.offset)
