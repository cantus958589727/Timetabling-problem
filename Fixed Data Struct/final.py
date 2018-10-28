import datetime
import mysql.connector
from Scheduler import*
import re


#this function will determine if a course is already in the sched
def isCourseSet():
    pass
    #pass the sched you want to improve and n is the number of course or slot
    #to be edited
    # if 
def improveSched(sched, n, slots):
    if(len(courseCode) == 0):
        for x in range(0, len(sched)-1):
            if(len(sched[x]) != len(sched[x+1])):
                break
            
        #for now, if all scheds have 5 dont do anything
        if((x+2) == len(sched)) :
            print("do nothing ", len(sched))
            return sched
        else:
            print("improving")
            #assuming that TTH has the same sched and same goes for WF
            if(len(sched[x]) > len(sched[x+1])):
                sched[x+1].append(sched[x][len(sched[x])-1])
                sched[x+2].pop(len(sched[x+2])-1)
                sched[x+3].append(sched[x][len(sched[x])-1])
                sched[x].pop(len(sched[x])-1)
                
            else:
                sched[x].append(sched[x+1][len(sched[x+1])-1])
                sched[x+2].append(sched[x+1][len(sched[x+1])-1])
                sched[x+3].pop(len(sched[x+3])-1)
                sched[x+1].pop(len(sched[x+1])-1)
                
            #printSched(sched)
            return sched
            
            

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

def getUnitsFromDB():
    mydb = mysql.connector.connect(
           host = "localhost",
           user = "root",
           passwd = "mysql11",
           database = "thesis"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT units FROM course LIMIT 10")

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

#make a list of unset courses and prof
def printSched(schedule):
    for x in range(0, len(schedule)):
        switcher = {
            0: "Tuesday",
            1: "Wednesday",
            2: "Thursday",
            3: "Friday"
        }
        print(switcher.get(x, " "))
        for y in range(0, len(schedule[x])):
            print(schedule[x][y])
                                
def fillSched(courseCode, prof, units):
    #matrix = per time
    #subMatrix = per day
    #mainMatrix = per classroom
    #process:
    #create sched per time
    #create sched per day
    #create sched per class
    
    subMatrix = []
    mainMatrix = []
    copyMatrix = []
    numOfSetCourses = 0
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
##            copyMatrix.append(subMatrix)
            mainMatrix.append(subMatrix)
            numOfSetCourses += len(subMatrix)
            subMatrix = []
            subMatrix.append(matrix)
            
    if(len(subMatrix) != 0):
        mainMatrix.append(subMatrix)
        numOfSetCourses += len(subMatrix)
        subMatrix = []

    for x in range(0, len(courseCode)):
        #based in the constraints, hours / units will be set as a condition here
        #to determine whether to add it to a thursday, friday or saturday sched
        container = [courseCode[x], prof[x]]
        matrix = []
        matrix.append(container)
        if(len(subMatrix) < 6):
            subMatrix.append(matrix)
        else:
##            copyMatrix.append(subMatrix)
            mainMatrix.append(subMatrix)
            subMatrix = []
            subMatrix.append(matrix)
            
    if(len(subMatrix) != 0):
        mainMatrix.append(subMatrix)

    #Assuming it goes through the list top to bottom
    for x in range(0, numOfSetCourses):
        courseCode.pop(0)
        prof.pop(0)

    print(len(prof))
    print(len(courseCode))
##    for x in range(0 , len(matrix)/2):
##        for y in range(x*5, x+5):
##            subMatrix.append(matrix[y])

    
    return mainMatrix

courseID = getCleanOneTuple(getCourseIdFromDB())
courseCode = getCleanOneTuple(getCourseCodeFromDB(courseID))
prof = getCleanOneTuple(getProfFromDB())
units = getCleanOneTuple(getUnitsFromDB())

schedule = fillSched (courseCode, prof, units)


printSched(schedule)

schedule = improveSched(schedule,1,1)


printSched(schedule)

improveSched(schedule,1,1)





