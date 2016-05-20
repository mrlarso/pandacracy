#!/usr/bin/env python
import os
import sys
import energy_points_assignment
import MySQLdb

#Pandacracy files
import mysqlconn
import roles

def clear():
    os.system("clear")

def main_menu():
    activity = ""
    while activity not in ['1','2','0']:
        clear()
        activity = raw_input('''
Please choose the option number for what you would like to do:

1. Explore team members and roles
2. Explore circles

0. Exit


'''
)
    return activity

cursor = mysqlconn.connect_to_db()

roleList, teamList = roles.import_rolesheet(cursor)

option = ""
while option != "0":
    option = main_menu()
    if option == "1":
        roles.explore_team(teamList, roleList)

clear()
exit()
