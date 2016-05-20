#!/usr/bin/env python

# Takes data from csv sheets and stores in MySQL database.

import MySQLdb
import sys
import csv
import re
import getpass
import os

def clear():
    os.system("clear")


def connect_to_db():
    clear()
    print "Please enter the database information: \n"
    server = raw_input("Server name:  ")
    username = raw_input("username:  ")
    password = getpass.getpass("Password:  ")
    database = raw_input("Database name:  ")
#    db = MySQLdb.connect(server,username,password,database)
    db = MySQLdb.connect("localhost","root","mrl3019","energy_points")
    cursor = db.cursor()
    return cursor
'''
with open(sys.argv[1], 'rb') as rolesCsv:
    rolesFiltered = (line.replace(';\n',';') for line in rolesCsv)
    myRoles = csv.reader(rolesFiltered)
    roleList = []
    for role in myRoles:
        roleList.append(role)


for role in roleList:
    if "'" in role[0]:
        role[0] = re.sub("'","",role[0])
    if "'" in role[1]:
        role[1] = re.sub("'","",role[1])

def insert_role_table(roleList):
    sql = "CREATE TABLE ROLES (ROLE CHAR(250) NOT NULL, ENERGIZER CHAR(250), CIRCLE CHAR(250))"
    cursor.execute(sql)
    inserted = 0
    for role in roleList:
        sql = "INSERT INTO ROLES(ROLE,ENERGIZER,CIRCLE) VALUES ('%s','%s','%s')" % (role[0],role[1],role[2])
        try:
            cursor.execute(sql)
            db.commit()
            inserted += 1
        except:
            print role
            db.rollback()
            print "error"
    print str(inserted) + " roles inserted."

sql = "SHOW TABLES LIKE 'ROLES'"

if cursor.execute(sql):
    overwrite = raw_input("Do you want to overwrite the current 'ROLES' table (y/n)? ")
    overwrite = overwrite.lower()
    if overwrite == "y":
        sql = "DROP TABLE IF EXISTS ROLES"
        cursor.execute(sql)
        insert_role_table(roleList)

else:
    overwrite = raw_input("Do you want to create the table 'ROLES' (y/n)? ")
    overwrite = overwrite.lower()
    if overwrite == "y":
        insert_role_table(roleList)

with open(sys.argv[2], 'rb') as circlesCsv:
    circleList = []
    myCircles = csv.reader(circlesCsv)
    for circle in myCircles:
        circleList.append(circle)

for circle in circleList:
    if "'" in circle[0]:
        circle[0] = re.sub("'","",circle[0])
    if "'" in circle[1]:
        circle[1] = re.sub("'","",circle[1])
    if "'" in circle[2]:
        circle[2] = re.sub("'","",circle[2])
    if "'" in circle[3]:
        circle[3] = re.sub("'","",circle[3])
    if "'" in circle[4]:
        circle[4] = re.sub("'","",circle[4])
    if "'" in circle[5]:
        circle[5] = re.sub("'","",circle[5])

def insert_circle_table(circleList):
    sql = "CREATE TABLE CIRCLES (CIRCLE CHAR(250) NOT NULL, SUPERCIRCLE CHAR(250), LEAD_LINK CHAR(250),FACILITATOR CHAR(250), REP_LINK CHAR(250), SECRETARY CHAR(250))"
    cursor.execute(sql)
    inserted = 0
    for circle in circleList:
        sql = "INSERT INTO CIRCLES(CIRCLE,SUPERCIRCLE,LEAD_LINK,FACILITATOR,REP_LINK,SECRETARY) VALUES ('%s','%s','%s','%s','%s','%s')" % (circle[0],circle[1],circle[2],circle[3],circle[4],circle[5])
        try:
            cursor.execute(sql)
            db.commit()
            inserted += 1
        except:
            print circle
            db.rollback()
            print "error"
    print str(inserted) + " circles inserted."

sql = "SHOW TABLES LIKE 'CIRCLES'"

if cursor.execute(sql):
    overwrite = raw_input("Do you want to overwrite the current 'CIRCLES' table (y/n)? ")
    overwrite = overwrite.lower()
    if overwrite == "y":
        sql = "DROP TABLE IF EXISTS CIRCLES"
        cursor.execute(sql)
        insert_circle_table(circleList)

else:
    overwrite = raw_input("Do you want to create the table 'CIRCLES' (y/n)? ")
    overwrite = overwrite.lower()
    if overwrite == "y":
        insert_circle_table(circleList)


db.close()
'''
