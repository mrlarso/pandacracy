#!/usr/bin/env python

import csv
import os

def clear():
    os.system("clear")

def import_circlesheet(cursor):
    cursor.execute("SELECT * FROM CIRCLES")
    circles = cursor.fetchall()
    circleList = []
    for row in circles:
        circle = []
        for i in row:
            circle.extend(row)
        circleList.append(circle)
    return circleList

def get_roles(circle,roleList):
    rolesInCircle = []
    for role in roleList:
        if role[2] == circle[0]:
            rolesInCircle.append(role)
    return rolesInCircle

def get_subcircles (circle,circleList,roleList):
    rolesInCircle = get_roles(circle,roleList)
    subCircleList = []
    for i in circleList:
        if i[1] == circle[0]:
            subCircleList.append(i)
    print "%s has %i subcircles and %i roles\n" % (circle[0],len(subCircleList),len(rolesInCircle))
    for circle in subCircleList:
        print "%i - %s\n" %(subCircleList.index(circle) + 1, circle[0])
    print "\n%i - Explore roles" %(len(subCircleList)+1)
    print "\n\n0 - Back"
    return subCircleList, rolesInCircle

def get_supercircle(circle,circleList):
    for i in circleList:
        if i[0] == circle[1]:
            supercircle = i
    return supercircle

def explore_circles(circleList,roleList):
    option = ""
    for circle in circleList:
        if circle[1] == "":
            superestCircle = circle
    circle = superestCircle
    while option != "0":
        clear()
        if circle == superestCircle:
            print "You have %s circles\n" %(str(len(circleList)))
            print "Your highest level circle is %s\n" % (circle [0])
        else:
            print circle[0] + " -\n"
            superCircle = get_supercircle(circle, circleList)
        subCircleList,rolesInCircle = get_subcircles(circle,circleList,roleList)
        option = raw_input("\nSelect your prefered option  ")
        if not option.isdigit() or ((option != "0") and (int(option) not in range(0,len(subCircleList)+2))):
            pass
        if (option == "0") and (circle != superestCircle):
            option = ""
            circle = superCircle
        elif int(option) > len(subCircleList):
            clear()
            print "%s has %i roles - \n" %(circle[0],len(rolesInCircle))
            for role in rolesInCircle:
                energizers = ""
                for energizer in role[1]:
                    energizers = energizers + energizer + ", "
                print"%i - %s (%s)\n" %(rolesInCircle.index(role)+1, role[0], energizers[:-2])
            print "\n"
            raw_input("Press enter to go back")
        else:
            circle = subCircleList[int(option)-1]
