#!/usr/bin/env python

import csv
import re
import os

def import_rolesheet(cursor):
    # Fetches roles from database and creates a list of roles
    cursor.execute( "SELECT * FROM ROLES")
    roles = cursor.fetchall()
    roleList = []
    for row in roles:
        role = []
        role.append(i[0])
        role.append(i[1])
        role.append(i[2])
        roleList.append[role]

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
