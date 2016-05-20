#!/usr/bin/env python

import csv
import re
import os

def import_rolesheet(roles_csv_file):

    # Creates a list from each line of the csv with roles
    with open(roles_csv_file, 'rb') as rolesCsv:
        rolesFiltered = (line.replace(';\n',';') for line in rolesCsv)
        myRoles = csv.reader(rolesFiltered)
        roleList = []
        for role in myRoles:
            roleList.append(role)

    # Removes the titles row if it exists
    if roleList[0][0] == 'Role':
        del roleList[0]

    # Turns energizer field of role into a list
    for x in range(0,len(roleList)):
        role = roleList[x]
        for y in range(0,len(role)):
            field = roleList[x][y]
            if ';' in field:
                roleList[x][y] = field.split(';')

    for role in roleList:
        if not isinstance(role[1], list):
            role[1] = [role[1]]

    # Removes apostrophes from fields (so as to not interfere with mysql syntax)
    for role in roleList:
        if "'" in role[0]:
            role[0] = re.sub("'","",role[0])
        if "'" in role[1]:
            role[1] = re.sub("'","",role[1])

    return roleList
'''
teamList = []
for role in roleList:
    for person in role[1]:
        print person
        if person not in teamList  and (person != ""):
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
'''
