from Building import build
import json
import sys
import csv
from Calls import calls
def pars_input():
    listCalls=[]
    submission_file_build = sys.argv[1]
    submission_file_calls = sys.argv[2]
    submission_file_out = sys.argv[3]
    with open(submission_file_build) as build:
        data = json.load(build)
    with open(submission_file_calls, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            listCalls.append(row)
    return (submission_file_out,data,listCalls)
  
def algo():
    
    
    
    pass
def main():
    (outName,data,callList)=pars_input()
    print(data)
    b=build(data)
    c=calls(callList[0])
  
    
    print(c.dest)
    for x in b._elevators:
        print(x._minFloor)
   
 
if __name__ == "__main__":
    main()


