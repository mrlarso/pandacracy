#!/usr/bin/env python

import sys
import os
import MySQLdb
import re

def clear():
    os.system("clear")

def prepare_identifier(item):
    item = re.sub(";","_",item)
    item = re.sub(" ","_",item)
    item = re.sub("/","_",item)
    item = re.sub("&","_AND_",item)
    item = re.sub("-","",item)
    item = item.upper()
    return item

def check_EP_tables(cursor,db,circleList,roleList):
    tableList = []
    for circle in circleList:
        circleName = circle[0]
        circleName = prepare_identifier(circleName)
        tableList.append(circleName)
    for table in tableList:
        sql = "SHOW TABLES LIKE '%s'" %(table)
        if cursor.execute(sql):
            overwrite = raw_input(table + " already exists. Would you like to overwrite it? y/n ")
        else:
            createTable = ""
            while createTable not in ('y','n'):
                print table + " does not exist"
                createTable = raw_input("Would you like to create it (y/n)?  ")[0].lower()
        if overwrite == 'y' or createTable == 'y':
            if overwrite == 'y':
                sql = "DROP TABLE %s" % (table)
                cursor.execute(sql)
            sql = "CREATE TABLE %s(ASSIGNEE CHAR(250))" % (table)
            try:
                cursor.execute(sql)
                db.commit()
            except:
                print "error inserting " + table
                db.rollback()
            print table + " inserted"
            raw_input()
            for role in roleList:
                print role[0]
                roleCircle = prepare_identifier(role[2])
                roleName = prepare_identifier(role[0])
                if roleCircle == table:
                    print roleName
                    raw_input()
                    sql = "ALTER TABLE %s ADD %s INT(2)" % (table, roleName)
                    try:
                        cursor.execute(sql)
                        "Column %s inserted" % (roleName)
                        db.commit()
                    except:
                        print "Error inserting column "+ roleName
                        db.rollback()
                    raw_input()




        raw_input()
