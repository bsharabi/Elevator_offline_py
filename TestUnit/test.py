import csv
import json
import unittest
import sys
sys.path.append('../')
from Departments.Building import build
from Departments.Calls import calls
import algorithm.algo 


class Test(unittest.TestCase):
    def BuldingTest(self):
        with open('.\testBuild.json') as buildfile:
            ObjectBuild = json.load(buildfile)
        buildfile.close()
        b = build(ObjectBuild)
        self.assertEqual(b._minFloor, -2)
        self.assertEqual(b._maxFloor, 10)
        self.assertEqual(len(b._elevators), 2)
        self.assertEqual(b._elevators[0]._minFloor, -2)
        self.assertEqual(b._elevators[0]._maxFloor, 10)

  
    def allocateTest(self):
        with open('.\testCalls.csv',newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
        csvfile.close()
        with open('.\testBuild.json') as buildfile:
            ObjectBuild = json.load(buildfile)
        buildfile.close()
        b = build(ObjectBuild)
        callList=[]
        callList.append(calls(spamreader[0]))
        callList.append(calls(spamreader[1]))
        callList.append(calls(spamreader[2]))
        callList.append(calls(spamreader[3]))
        algorithm.algo.allocateToElevator(callList,b._elevators)
        self.assertEqual(callList[0].src, 0)
        self.assertEqual(callList[1].src, -1)
        self.assertEqual(callList[2].dest, -1)
        self.assertEqual(callList[0]._allocateTo, 0)
        self.assertEqual(callList[1]._allocateTo, 0)
        self.assertEqual(callList[2]._allocateTo, 1)
        self.assertEqual(callList[3]._allocateTo, 1)

if __name__ == '__main__':
    unittest.main()