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
    item = re.sub("\(","",item)
    item = re.sub("\)","",item)
    item = re.sub("!","",item)
    item = re.sub("\.","",item)
    item = re.sub(",","",item)
    item = item.upper()
    return item

def insert_circle_table(table,roleList,cursor,db):
    sql = "CREATE TABLE %s(ASSIGNEE CHAR(250))" % (table)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print "error inserting " + table
        db.rollback()
    print table + " inserted"
    addedRoles = 0
    for role in roleList:
        roleCircle = prepare_identifier(role[2])
        roleName = prepare_identifier(role[0])
        if roleCircle == table:
            sql = "ALTER TABLE %s ADD %s INT(2)" % (table, roleName)
            try:
                cursor.execute(sql)
                "Column %s inserted" % (roleName)
                db.commit()
                addedRoles += 1
            except:
                print "Error inserting column "+ roleName
                db.rollback()
    print str(addedRoles) + " roles succesfully inserted"

def add_energizers(cursor,db,roleList):
    cursor.execute("SHOW TABLES")
    uglyList = cursor.fetchall()
    tableList = []
    for item in uglyList:
        tableList.append(item[0])
    for table in tableList:
        energizers = []
        for role in roleList:
            if prepare_identifier(role[2]) == table:
                for person in role[1]:
                    if person not in energizers:
                        energizers.append(person)
        inserted = 0
        for energizer in energizers:
            sql = "INSERT INTO %s(ASSIGNEE) VALUES('%s')" % (table, energizer)
            try:
                cursor.execute(sql)
                db.commit()
                inserted += 1
            except MySQLdb.Error, e:
                print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
                print "Error inserting " + energizer + " into " + table
        raw_input("%i energizers inserted into %s" %(inserted, table))


def check_EP_tables(cursor,db,circleList,roleList):
    tableList = []
    for circle in circleList:
        circleName = circle[0]
        circleName = prepare_identifier(circleName)
        tableList.append(circleName)
    for table in tableList:
        sql = "SHOW TABLES LIKE '%s'" %(table)
        createTable = ""
        overwrite = ""
        if cursor.execute(sql):
            overwrite = "n"
            #raw_input(table + " already exists. Would you like to overwrite it? y/n ")
        else:
            insert_circle_table(table,roleList,cursor,db)

        if overwrite == 'y':
            sql = "DROP TABLE %s" % (table)
            cursor.execute(sql)
            insert_circle_table(table, roleList,cursor,db)
    add_energizers(cursor,db,roleList)
