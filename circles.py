#!/usr/bin/python

import sys
import csv
import os


# Import csv file and create list of circles

myCircles = []
with open(sys.argv[1], 'rb') as circlesCsv:
    circleList = csv.reader(circlesCsv)
    for circle in circleList:
        myCircles.append(circle)
        if circle[1] == "":
            superestCircle = circle

def getCircleInfo(circle):
    os.system('clear')
    print "The elected roles of %s are: \nLead Link: %s \nFacilitator: %s \nRep Link: %s \nSecretary: %s \n" % (circle[0],circle[2],circle[3],circle[4],circle[5])

    subCircleList = [circle]
    subCircleNumber = 1
    for i in myCircles:
        if i[1] == circle[0]:
            subCircleList.append(i)

    if len(subCircleList) == 0:
        print circle[0] + " does not have any subcircles.\n"
    else:
        print circle[0]+" has the following subcircles:\n"
        for i in subCircleList[1:]:
            print str(subCircleNumber) + ". "+i[0]+"\n"
            subCircleNumber += 1
    if circle[1] != "":
        print "0. Go back to "+ circle[1]
    return subCircleList

print "You have %s circles\n" % (str(len(myCircles)))
print "Your highest level circle is %s\n" % (superestCircle[0])
subCircleList = getCircleInfo(superestCircle)
currentCircle = superestCircle
choice = ""
while choice != "exit":
    choice = raw_input("Select the number of the circle you would like to know more about, or type 'exit' to exit.")
    if choice == "exit":
        break
    elif choice == "0":
        for i in myCircles:
            if i[0] == currentCircle[1]:
                currentCircle = i
                subCircleList = getCircleInfo(currentCircle)
                getCircleInfo(currentCircle)
    else:
        subCircleList = getCircleInfo(subCircleList[int(choice)])
        getCircleInfo(subCircleList[int(choice)])
    print "Current Circle "
    print currentCircle
    print "choice = "+ choice
    print subCircleList
