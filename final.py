import datetime
import mysql.connector
from Scheduler import*
import re
import copy
import time
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)

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

def getRoomsFromDB():
    #get room type
    #get from gokongwei bldg
    #----Query-----
    #SELECT thesisschema.building.﻿building_id FROM thesisschema.building where thesisschema.building.building_code = "GK";
    mydb = mysql.connector.connect(
           host = "localhost",
           user = "root",
           passwd = "mysql11",
           database = "thesis"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT thesisschema.building.﻿building_id FROM thesisschema.building where thesisschema.building.building_code = \"GK\";")

    RoomCodeGK = mycursor.fetchall()

    mycursor.execute("SELECT room_code, room_type FROM thesisschema.room Where building_id = " + str(RoomCodeGK[0][0]) + ";")

    myresult = mycursor.fetchall()

    print(classifyRooms(myresult))
    #return classifyRooms(myresult)
    #pass

def classifyRooms(rooms):
    print(rooms)
    i = 0
    ClassifiedRoom = [[]for x in range(2)]
    while(i < len(rooms)):
          if(rooms[i][1] == "Computer Laboratory"):
              ClassifiedRoom[1].append(rooms[i][0])
          elif(rooms[i][1] == "Lecture"):
              ClassifiedRoom[0].append(rooms[i][0])
          i = i + 1
    #ClassifiedRoom[0] Lecture, [1] Lab
    return ClassifiedRoom

      
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
        if(len(subMatrix) < 6):
            subMatrix.append(container)
        else:
##            copyMatrix.append(subMatrix)
            mainMatrix.append(subMatrix)
            numOfSetCourses += len(subMatrix)
            subMatrix = []
            subMatrix.append(container)
            
    if(len(subMatrix) != 0):
        numOfSetCourses += len(subMatrix)
        emptyMatrix = ["", ""]
        while(len(subMatrix) < 6):
            subMatrix.append(emptyMatrix)
        mainMatrix.append(subMatrix)
        
        subMatrix = []

    for x in range(0, len(courseCode)):
        #based in the constraints, hours / units will be set as a condition here
        #to determine whether to add it to a thursday, friday or saturday sched
        container = [courseCode[x], prof[x]]
##        matrix = []
##        matrix.append(container)
        if(len(subMatrix) < 6):
            subMatrix.append(container)
        else:
##            copyMatrix.append(subMatrix)
            mainMatrix.append(subMatrix)
            subMatrix = []
            subMatrix.append(container)
            
    if(len(subMatrix) != 0):
        emptyMatrix = ["", ""]
        while(len(subMatrix) < 6):
            subMatrix.append(emptyMatrix)
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

def clearAll():
    indexSlots = []
    indexDay = []
    
def clearSlotsAndMarkDay(n):
    indexSlots = []
    indexDay.append(n)
    
def checkIndexSlot(maxSlot, day):
    if(len(indexSlot) >= maxSlot):
        clearSlotsAndMarkDay(day)
        
def checkIndexDay(days):
    if(len(indexDay) >= days):
        clearAll()
        
       
def checkIfEmptySlot(slot):
    if(slot[0] == "" and slot[1] == ""):
        return True
    else:
        return False

def checkSlotSimilarity(slot1, slot2):
    done = False
    i = 0
    while(i < len(slot1) and not(done)):
        if(slot1[i] != slot2[i]):
            done = True
        i += 1
        
    return not(done)

def checkIfIntegerExistInArray(n, arr):
    i = 0
    done = False
    
    while(i < len(arr) and not(done)):
        if(arr[i] == n):
            done = True
        i +=1
            
    return done

def checkCourseExistInMultiple(course, day, sched):
    interval = [day]
    for x in range(0, len(sched)):
        if(not(x == day)):
            done = False
            y = 0
            while(y < len(sched[x]) and not(done)):
                if(checkSlotSimilarity(sched[x][y], course)):
                   done = True

                y += 1
                   
            if(done):
                interval.append(x)
    if(len(interval) > 1):
        return interval[0] - interval[1]
    else:
        return 0
    
def traverseIndex(slot, day, sched):
    #copy that certain slot of that day in that sched and try to move it to
    #different slots
    setOfSchedules = []
    copyMatrix = copy.deepcopy(sched[day][slot])
    print("copying this: ", copyMatrix)
    interval = checkCourseExistInMultiple(copyMatrix, day, sched)
    if(interval == 0):
        for x in range(0, len(sched)):
            for y in range(0, len(sched[x])):
                if(not(x == day and y == slot)):
                    editedSched = sched.copy()
                    editedSched[day][slot] = sched[x][y]
                    editedSched[x][y] = copyMatrix
                    setOfSchedules.append(editedSched)
                           
        return setOfSchedules        

    else:
        if(interval < 0):
            interval *= -1
        print(interval)
        for x in range(0, len(sched)//2):
            print(x)
            for y in range(0, len(sched[x])):
                if(not(x == day and y == slot) and not(x == day - interval) and not(x == day + interval)):                                           
                    editedSched = copy.deepcopy(sched)
                    
                    print("target: " , sched[x][y])
                    print("target: " , sched[x+interval][y])
                    
                    print("editedSched: " , editedSched[day][slot])
                    if(day + interval > len(sched)):
                        print("editedSched: " , editedSched[day-interval][slot])
                    else:
                        print("editedSched: " , editedSched[day+interval][slot])
                        
                    
                    editedSched[day][slot] = sched[x][y]
                    if(day + interval > len(sched)):
                        editedSched[day-interval][slot] = sched[x+interval][y]
                    else:
                        editedSched[day+interval][slot] = sched[x+interval][y]
                        
                    editedSched[x][y] = copyMatrix
                    editedSched[x+interval][y] = copyMatrix
                    
                    print("new editedSched: " , editedSched[day][slot])
                    if(day + interval > len(sched)):
                        print("new editedSched: " , editedSched[day-interval][slot])
                    else:
                        print("new editedSched: " , editedSched[day+interval][slot])

                    print("new editedSched: ", editedSched[x][y])
                    print("new editedSched: ", editedSched[x+interval][y])

                    setOfSchedules.append(editedSched)
                else:
                    print("skipped values!", x, y)
                    
        return setOfSchedules
                
                
def improveSchedV2(sched):
    setOfSchedules = []
    x = 0
    done = False
    while(x < len(sched) and not(done)):
        checkIndexSlot(len(sched[x]), x)
        if(not(checkIfIntegerExistInArray(x, indexDay))):
            print("Integer Does Not Exist In Array!")
            y = 0
            while(y < len(sched[x]) and not(done)):
                if(not(checkIfIntegerExistInArray(y, indexSlot))):
                    indexSlot.append(y)
                    done = True
                    
                y += 1
                
            x += 1
        else:
            x += 1

    if(done):
        last = len(indexSlot) - 1
        print("last value: ", indexSlot[last])
        print("day value: ", x-1)
        setOfSchedules = traverseIndex(indexSlot[last], x-1, sched)

    return setOfSchedules                            
       
    #move scheds multiple times
    #assuming all courses are set on a specific time slot
    #return multiple instances of MainMatrix

def gapYScoring(sched, score):
    for x in range(0, len(sched)):
        tempScore = 1
        prevCheck = False
        currCheck = False
        perfect = True
        multiplier = 1
        for y in range(0, len(sched[x])):
##            print(y)
            if(y == 0):
                if(not(sched[x][y][0] == "")):
                    prevCheck = True
            else:
                if(not(sched[x][y][0] == "")):
                    currCheck = True
                else:
                    currCheck = False

                if(not(currCheck) and prevCheck and tempScore == 1):
##                    print("T, F")
                    tempScore -= multiplier
                elif(not(prevCheck) and currCheck and tempScore <= 0):
##                    print("F, T")
                    score += tempScore
                    multiplier += 1
                    perfect = False
                elif(not(currCheck) and not(prevCheck) and tempScore <= 0):
##                    print("F, F")
                    tempScore -= multiplier
                elif(currCheck and prevCheck):
##                    print("T, T")
                    if(tempScore <= 0):
                        tempScore = 1
                        
                prevCheck = currCheck
                
        if(perfect):
            score += 1
        
##        print("current score: ", score)
                    
    return score

def mainScoringFunction(sched):
    score = 0
    ##define multiple scoring functions
    score += gapYScoring(sched, score)

    return score

def printSample(editedSched):
    for x in range(len(editedSched)):
        printSched(editedSched[x])
        
def logMultipleSchedule(sched):
    logging.info("Start of Multiple Schedule")
    for x in range(0, len(sched)):
        logging.info("Schedule " + str(x+1))
        logSchedule(sched[x])
    logging.info("End of Multiple Schedule")
    
def logSchedule(sched):
    logging.info("Start of Single Schedule")
    for x in range(len(sched)):
        switcher = {
            0: "Tuesday",
            1: "Wednesday",
            2: "Thursday",
            3: "Friday"
        }
        logging.info(switcher.get(x, "Index out of bounds!"))
        logging.info(sched[x])
    logging.info("End of Single Schedule")
        
def logMessage(msg, val):
    logging.info(msg + " " + str(val))

def logScoreSchedule(sched):
    logging.info("Start of Scheduling Score")
    logSchedule(sched)
    logging.info("Score: " + str(mainScoringFunction(sched)))
    logging.info("End of Scheduling Score")

def logMultipleScoreSchedule(sched):
    logging.info("Start of Multiple Scheduling Score")
    
    for x in range(0, len(sched)):
        logging.info("Schedule " + str(x+1))
        logSchedule(sched[x])
        logging.info("Score: " + str(mainScoringFunction(sched[x])))
        
    logging.info("End of Multiple Scheduling Score")

 
indexDay = []
indexSlot = []

courseID = getCleanOneTuple(getCourseIdFromDB())
courseCode = getCleanOneTuple(getCourseCodeFromDB(courseID))
prof = getCleanOneTuple(getProfFromDB())
units = getCleanOneTuple(getUnitsFromDB())

schedule = fillSched (courseCode, prof, units)

printSched(schedule)

logSchedule(schedule)
logScoreSchedule(schedule)
print("Score: ", mainScoringFunction(schedule))
##schedule = improveSched(schedule,1,1)

##printSched(schedule)

##improveSched(schedule,1,1)

##start = time.time()
sample = improveSchedV2(schedule)
##end = time.time()

logMultipleScoreSchedule(sample)

print("Created schedule length: ", len(sample))
printSample(sample)

sample = improveSchedV2(schedule)
##printSample(sample)
##print("time elapsed:", end - start)

##logMultipleSchedule(sample)
logMultipleScoreSchedule(sample)

##for x in range(0, len(sample)):
##    print("Schedule " , x+1)
##    printSched(sample[x])
##    print("Score: ", mainScoringFunction(sample[x]))
