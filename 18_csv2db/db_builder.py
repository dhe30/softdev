#Team Green Monkeys; Daniel He, Faiyaz Rafee
#SoftDev  
#K18 SQLITE3 BASICS- making tables and adding data from csv files in sqlite through python
#2022-10-26
#time spent: 1.5 hrs

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
c.execute("DROP TABLE if exists students")
c.execute("DROP TABLE if exists courses")
#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
def reading_it(a):
    with open(a, newline = "") as file:
        courses = csv.DictReader(file)
        table_name = a[:-4]
        print(table_name)
        if a == "courses.csv":
            c.execute("create table " + table_name + " (code TEXT, mark INTEGER, id INTEGER);")
        else:
            c.execute("create table " + table_name + " (name TEXT, age INTEGER, id INTEGER);")
        for course in courses: # creates an object where each row is a dictonary
            if a == "courses.csv":
                command = "insert into " + table_name + " values (\"" + course['code'] + "\", " + course['mark'] + ", " + course['id'] + ");"          # test SQL stmt in sqlite3 shell, save as string
            else: 
                command = "insert into " + table_name + " values (\"" + course['name'] + "\", " + course['age'] + ", " + course['id'] + ");"          # test SQL stmt in sqlite3 shell, save as string

            print(command)
            c.execute(command)    # run SQL statement
reading_it("courses.csv")
reading_it("students.csv")
#==========================================================

db.commit() #save changes
db.close()  #close database


