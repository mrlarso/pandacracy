#!/usr/bin/python

import sys
import csv
import os

if len(sys.argv) < 3:
    print "Please include 2 arguments, <roles csv> and <circles csv>"
    exit()

with open(sys.argv[2], 'rb') as circlesCsv:
    circleList = []
    myCircles = csv.reader(circlesCsv)
    for circle in myCircles:
        circleList.append(circle)

with open(sys.argv[1], 'rb') as rolesCsv:
    rolesFiltered = (line.replace(';\n',';') for line in rolesCsv)
    myRoles = csv.reader(rolesFiltered)
    roleList = []
    for role in myRoles:
        roleList.append(role)

if roleList[0][0] == 'Role':
    del roleList[0]

for x in range(0,len(roleList)):
    role = roleList[x]
    for y in range(0,len(role)):
        field = roleList[x][y]
        if ';' in field:
            roleList[x][y] = field.split(';')

if circleList[0][0] == 'Circle Name':
    del circleList[0]

for circle in circleList:
    leadlink = ['Lead Link - %s' % (circle[0]),circle[2],circle[0]]
    facilitator = ['Facilitator - %s' % (circle[0]),circle[3],circle[0]]
    replink = ['Rep Link - %s' % (circle[0]),circle[4],circle[0]]
    secretary = ['Secretary - %s' % (circle[0]),circle[5],circle[0]]
    roleList.extend((leadlink,facilitator,replink,secretary))

for role in roleList:
    if not isinstance(role[1], list):
        role[1] = [role[1]]
#        print role
#print str(len(roleList))
#raw_input()

for role in roleList:
    if (role[1]==[""]) or (role[2]==""):
#        print role
#        raw_input()
        roleList.remove(role)

if "" in role[1]:
    roleList.remove(role)

#for role in roleList:
#    print role
#print str(len(roleList))
#raw_input()


#raw_input()
# Gets a list of all people in the organization

teamList = []
for role in roleList:
    energizers = role[1]
    for name in energizers:
        if (name not in teamList) and name != "":
            teamList.append(name)

for i in range(0,len(teamList)):
    teamList[i] = [teamList[i]]

#raw_input(teamList)

for teamMember in teamList:
    teamMember.append(0)

total = 0
#print circleList[0]
#print roleList
for circle in circleList:
    amount =  input("What is the total money to be distributed for %s?   " % (circle[0]))
    for role in roleList:
        if role[2] == circle[0]:
            role_percent = input("What is the percentage that should go to %s?   " % (role[0]))/100
            n = len(role[1])
            amount_per_person = (amount*role_percent)/n
            for name in teamList:
                if name[0] in role[1]:
                    name[1] = name[1] + amount_per_person
    print teamList
    for i in teamList:
        total = total + i[1]
    print total
    total = 0

for teammember in teamList:
    print "%s  - %s  ksh" % (teammember[1], str(round(teammember[2])))
