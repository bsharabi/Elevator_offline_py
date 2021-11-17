from Building import build
import json
import sys
import csv
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
  
def writeFile(outName,calls):
    with open(outName, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',' , quoting=csv.QUOTE_MINIMAL) 
        for x in calls:  
            (a,b,c,d,e,f)=x.toString()  ;
            spamwriter.writerow([a]+[b]+[c]+[d]+[e]+[f])
        
          
    pass
def main():
    (outName,data,callList)=pars_input()
    b=build(data,callList)
    writeFile(outName,b._calls)
   
  
     
if __name__ == "__main__":
    main()


