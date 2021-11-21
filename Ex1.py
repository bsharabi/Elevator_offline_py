from Classes.Building import build
import json
import sys
import csv
import algorithm.algo
def pars_input():# -> tuple["str", "Any", "list"]:
    '''Function is responsible for receiving the arguments sent from the user through the command line,
    decoding them, and returning an object of readings and information about the data'''
    callList=[]
    submission_file_build = sys.argv[1]
    submission_file_calls = sys.argv[2]
    submission_file_out = sys.argv[3]
    
    with open(submission_file_build) as build:
        data = json.load(build)
    build.close()
    with open(submission_file_calls, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            callList.append(row)
    submission_file_out=submission_file_out.split(".")[0]+'.csv'
    csvfile.close()
    return (submission_file_out,data,callList)


def writeFile(outName,calls):#->None:
    '''Function responsible for writing the results in the output file received at the command prompt '''
    with open(outName, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',' , quoting=csv.QUOTE_MINIMAL) 
        for call in calls:  
            (name_elev,timeIn,src,dest,flag,allocate)=call.toString()  ;
            spamwriter.writerow([name_elev]+[timeIn]+[src]+[dest]+[flag]+[allocate])
        
def main():# -> None:
    '''The main function from which to execute the algorithm and find the output'''
    (outName,data,callList)=pars_input()
    b=build(data,callList)
    algorithm.algo.allocateToElevator(b._calls,b._elevators)
    writeFile(outName,b._calls)
   
     
if __name__ == "__main__":
    main()


    