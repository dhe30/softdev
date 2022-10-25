#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
courses = csv.DictReader(open("courses.csv", "r"))
c.execute("create table courses (code TEXT, mark INTEGER, id INTEGER);")
for course in courses: # creates an object where each row is a dictonary
    command = "insert into courses values (\"" + course['code'] + "\", " + course['mark'] + ", " + course['id'] + ");"          # test SQL stmt in sqlite3 shell, save as string
    print(command)
    c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


