#!/usr/bin/env python

import sys
import csv
import re
import os

with open(sys.argv[1], 'rb') as rolesCsv:
    rolesFiltered = (line.replace(';\n',';') for line in rolesCsv)
    myRoles = csv.reader(rolesFiltered)
    roleList = []
    for role in myRoles:
        roleList.append(role)

if roleList[0][0] == 'Role':
    del roleList[0]

print roleList
print str(len(roleList))
raw_input()

for x in range(0,len(roleList)):
    role = roleList[x]
    for y in range(0,len(role)):
        field = roleList[x][y]
        if ';' in field:
            roleList[x][y] = field.split(';')

print roleList
print str(len(roleList))
raw_input()

for role in roleList:
    if not isinstance(role[1], list):
        role[1] = [role[1]]

print roleList
print str(len(roleList))
raw_input()

for role in roleList:
    if "'" in role[0]:
        role[0] = re.sub("'","",role[0])
    if "'" in role[1]:
        role[1] = re.sub("'","",role[1])

teamList = []
for role in roleList:
    for person in role[1]:
        print person
        if person not in teamList:
            teamList.append(person)


def showteam (teamList):
    count = 1
    for person in teamList:
        print str(count) + " - " + person
        count += 1
    print "\n"
    return raw_input("Choose a team member to see their roles:   ")

def get_person_roles(person):
    person_roles = []
    for role in roleList:
        if person in role[1]:
            person_roles.append(role)
    return person_roles


choice = showteam(teamList)
person_roles = get_person_roles(teamList[int(choice)-1])

print "%s has %s roles: \n" % (teamList[int(choice)-1], str(len(person_roles)))

for role in person_roles:
    print "%s (%s)" % (role[0],role[2])
