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
        role.extend(row)
        roleList.append(role)

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

    # Creates a list of all team members

    teamList = []
    for role in roleList:
        for person in role[1]:
            if person not in teamList  and (person != ""):
                teamList.append(person)

    return (roleList, teamList)


def explore_team (teamList, roleList):
    option = ""
    while option != "0" and option not in list(map(str, range(len(teamList)))):
        count = 1
        for person in teamList:
            print str(count) + " - " + person
            count += 1
        print "\n"
        print "0. Back to main menu"
        option =  raw_input("Choose a team member to see their roles:   ")
        if option in list(map(str, range(len(teamList)))):
            person = teamList[int(option)-1]
            person_roles = []
            for role in roleList:
                if person in role[1]:
                    person_roles.append(role)
            print "%s has %s roles: \n" % (teamList[int(option)-1], str(len(person_roles)))
            for role in person_roles:
                print "%s (%s)" % (role[0],role[2])
            raw_input("Press 'Enter' to return to list of team members")

def get_person_roles(person):
    person_roles = []
    for role in roleList:
        if person in role[1]:
            person_roles.append(role)
    return person_roles

'''
choice = showteam(teamList)
person_roles = get_person_roles(teamList[int(choice)-1])


'''
