import datetime
import mysql.connector
import re

def getCourseIdFromDB():
    mydb = mysql.connector.connect(
           host = "localhost",
           user = "root",
           passwd = "mysql11",
           database = "thesis"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT course_id FROM course LIMIT 10")

    myresult = mycursor.fetchall()

    return myresult

def getCleanOneTuple(data):
    rawData = data
    cleanData = []
    for x in range(0, len(rawData)):
        cleanData.append( rawData[x][0] )

    return cleanData

def getCourseCodeFromDB(courseID):
    mydb = mysql.connector.connect(
           host = "localhost",
           user = "root",
           passwd = "mysql11",
           database = "thesis"
    )

    mycursor = mydb.cursor()

    param = ''
    for x in range(0, len(courseID)):
        param += "course_id = " + str(courseID[x])
        if(x < len(courseID)-1):
           param += ' OR '

##    print(param)
    mycursor.execute("SELECT course_code FROM course WHERE " + param)
    
    myresult = mycursor.fetchall()

    return myresult

def getProfFromDB():
    mydb = mysql.connector.connect(
           host = "localhost",
           user = "root",
           passwd = "mysql11",
           database = "thesis"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT user_id FROM faculty LIMIT 10")

    myresult = mycursor.fetchall()

    return myresult

def fillSched(courseCode, prof):
    #matrix = per time
    #subMatrix = per day
    #mainMatrix = per classroom
    #process:
    #create sched per time
    #create sched per day
    #create sched per class
    
    subMatrix = []
    mainMatrix = []

    #for now
    if(len(courseCode) != len(prof)):
        return mainMatrix

    for x in range(0, len(courseCode)):
        container = [courseCode[x], prof[x]]
        matrix = []
        matrix.append(container)
        if(len(subMatrix) < 6):
            subMatrix.append(matrix)
        else:
            mainMatrix.append(subMatrix)
            subMatrix = []
            subMatrix.append(matrix)
            
    if(len(subMatrix) != 0):
        mainMatrix.append(subMatrix)
        
    
        
##    for x in range(0 , len(matrix)/2):
##        for y in range(x*5, x+5):
##            subMatrix.append(matrix[y])

    
    return mainMatrix
    
courseID = getCleanOneTuple(getCourseIdFromDB())
courseCode = getCleanOneTuple(getCourseCodeFromDB(courseID))
prof = getCleanOneTuple(getProfFromDB())

schedule = fillSched (courseCode, prof)

for x in range(0, len(schedule)):
    if(x == 0):
        print("Monday: ")
    if(x == 1):
        print("Tuesday: ")
    for y in range(0, len(schedule[x])):
        print(schedule[x][y])







