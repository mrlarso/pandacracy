#!/usr/bin/env python
import os
import sys
import energy_points_assignment
import MySQLdb

#Pandacracy files
import mysqlconn
import roles
import circles

def clear():
    os.system("clear")

def main_menu():
    activity = ""
    while activity not in ['1','2','3','0']:
        clear()
        activity = raw_input('''
Please choose the option number for what you would like to do:

1. Explore team members and roles
2. Explore circles
3. Upload roles/circles to database

0. Exit


'''
)
    return activity

def getRoles(db,cursor):
    try:
        roleList, teamList = roles.import_rolesheet(cursor)
    except:
        roleList, circleList = mysqlconn.importCsvs(sys.argv[1],sys.argv[2])
        mysqlconn.check_roles_database(cursor, db, roleList)
    return roleList, teamList


db, cursor = mysqlconn.connect_to_db()
roleList, teamList = getRoles(db, cursor)
circleList = circles.import_circlesheet(cursor)

option = ""
while option != "0":
    option = main_menu()
    if option == "1":
        roles.explore_team(teamList, roleList)
    if option == "2":
        clear()
        circles.explore_circles(circleList,roleList)
    if option == "3":
        if len(sys.argv) < 3:
            clear()
            raw_input("No CSV files detected. Please rerun the program followed by <path_to_roles_csv>  <path_to_circles_csv>")
            option = ""
        else:
            roleList, circleList = mysqlconn.importCsvs(sys.argv[1],sys.argv[2])
            mysqlconn.check_roles_database(cursor, db, roleList)
            mysqlconn.check_circles_database(cursor, db, circleList)
            roleList, teamList = getRoles(db, cursor)
            raw_input()

clear()
exit()
