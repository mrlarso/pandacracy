#!/usr/bin/python

import sys
import csv
import os

with open(sys.argv[1], 'rb') as rolesCsv:
    rolesFiltered = (line.replace(';\n',';') for line in rolesCsv)
    myRoles = csv.reader(rolesFiltered)
    roleList = []
    for role in myRoles:
        roleList.append(role)

# Creates a list of energizers if more than one exists
for x in range(0,len(roleList)):
    role = roleList[x]
    print role
    for y in range(0,len(role)):
        field = roleList[x][y]
        print field
        if ';' in field:
            print field.split(';')
            roleList[x][y] = field.split(';')

print roleList
