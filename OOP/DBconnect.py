import mysql.connector

class DBconnect(object):

    def __init__(self):
        self.mydb = mysql.connector.connect(
               host = "localhost",
               user = "root",
               passwd = "mysql11",
               database = "thesis"
        )

    def getTupleInArray(self,data):
##        print(data)
        rawData = data
        cleanData = []
        if rawData is None:
            print("Empty Data")
            
        for x in range(0, len(rawData)):
##            print(rawData[x][0][0])
            cleanData.append( rawData[x][0][0])

##        print("After:", cleanData)
        
        return cleanData
    
    def getCleanOneTuple(self, data):
##        print(data)
        rawData = data
        cleanData = []
        if rawData is None:
            print("Empty Data")
            
        for x in range(0, len(rawData)):
            cleanData.append( rawData[x][0] )

##        print("After:", cleanData)
        
        return cleanData

    def getCourseCodeFromDB(self, courseID):
        mycursor = self.mydb.cursor()

##        param = ''
##        for x in range(0, len(courseID)):
##            param += "course_id = " + str(courseID[x])
##            if(x < len(courseID)-1):
##               param += ' OR '
##        print(param)
##        input()
##        mycursor.execute("SELECT course_code FROM course WHERE " + param)
        myresult = []
        for x in range(0, len(courseID)):
            param = ' '
            param += "course_id = " + str(courseID[x])
            mycursor.execute("SELECT course_code FROM course WHERE " + param)
            myresult.append(mycursor.fetchall())
            
        print(len(myresult))
        return myresult

    def getProfFromDB(self, courseCode):
        mycursor = self.mydb.cursor()
    
        param = ''
        for x in range(0, len(courseCode)):
            param += "course = \"" + str(courseCode[x]) + "\""
            if(x < len(courseCode)-1):
               param += ' OR '
    
        mycursor.execute("SELECT Faculty_ID FROM thesis.professors where category in( select category from categories where " + param + ");")

        myresult = mycursor.fetchall()
##        print(param)
        return myresult

##    def getProfFromDB(self):
##
##        mycursor = self.mydb.cursor()
##
##        mycursor.execute("SELECT user_id FROM faculty LIMIT 10")
##
##        myresult = mycursor.fetchall()
##
##        return myresult
    
    def getCourseIdFromDB(self, year, term, courseSection):

        mycursor = self.mydb.cursor()
        
        Param = "start_year = " + str(year) + " AND term = " + str(term)
        #printParam)
        mycursor.execute("Select course_id from offering where " + Param + ";")
        
        myresult = mycursor.fetchall()

        ##GET THE SECTION OF THE CLASS
        mycursor.execute("Select section from offering where " + Param + ";")
        temp = mycursor.fetchall()
        courseSection.append(self.getCleanOneTuple(temp))
        
        return myresult

##    def getCourseIdFromDB(self):
##
##        mycursor = self.mydb.cursor()
##
##        mycursor.execute("SELECT course_id FROM course LIMIT 10")
##
##        myresult = mycursor.fetchall()
##
##        return myresult

    def getUnitsFromDB(courseID):

        mycursor = self.mydb.cursor()

        param = ''
        for x in range(0, len(courseID)):
            param += "course_id = " + str(courseID[x])
            if(x < len(courseID)-1):
               param += ' OR '

        mycursor.execute("SELECT units FROM course WHERE " + param)

        myresult = mycursor.fetchall()

        return myresult


##    def getUnitsFromDB(self):
##
##        mycursor = self.mydb.cursor()
##
##        mycursor.execute("SELECT units FROM course LIMIT 10")
##
##        myresult = mycursor.fetchall()
##
##        return myresult

    def classifyRooms(self, rooms):
##        print(rooms)
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
    
    def getRoomsFromDB(self):
        #get room type
        #get from gokongwei bldg
        #----Query-----
        #SELECT thesisschema.building.﻿building_id FROM thesisschema.building where thesisschema.building.building_code = "GK";
        
        mycursor = self.mydb.cursor()
        #SELECT thesis.building.﻿building_id FROM thesis.building where thesis.building.building_code = \"GK\";
        #SELECT thesisschema.building.﻿building_id FROM thesisschema.building where thesisschema.building.building_code = \"GK\";
        mycursor.execute("SELECT thesis.building.﻿building_id FROM thesis.building where thesis.building.building_code = \"GK\";")

        RoomCodeGK = mycursor.fetchall()

        #SELECT room_code, room_type FROM thesisschema.room Where building_id = " + str(RoomCodeGK[0][0]) + ";
        #SELECT room_code, room_type FROM thesis.room Where building_id = " + str(RoomCodeGK[0][0]) + ";
        mycursor.execute("SELECT room_code, room_type FROM thesis.room Where building_id = " + str(RoomCodeGK[0][0]) + ";")

        myresult = mycursor.fetchall()

##        print(classifyRooms(myresult))
        return self.classifyRooms(myresult)
        #pass

    def getProfPrefFromDb(self, ListOfProf, ListOfAdeptC, ListOfBegC):
        
        mycursor = self.mydb.cursor()
        #ListOfProf = ['CABREDO, RAFAEL', 'CHENG, CHARIBETH', 'CHU, SHIRLEY', 'RIVERA, PAULINE']
##        print(ListOfProf)
        for x in range(0, len(ListOfProf)):
            param = "Faculty_ID = \'" + str(ListOfProf[x]) + "\'"
            #---Check for adept---
            #SELECT course FROM categories where category in ( Select category from thesis.professors Where name =  AND proficiency = 'Adept');
            mycursor.execute("SELECT course FROM categories where category in ( Select category from thesis.professors Where " + param + "  AND proficiency = \'Adept\');" )
            AdeptResult = mycursor.fetchall()
            CleanAdeptResult = self.getCleanOneTuple(AdeptResult)
            ListOfAdeptC.append(CleanAdeptResult)
##            print(ListOfAdeptC)

            #--Get Beginner Courses--
            mycursor.execute("SELECT course FROM categories where category in ( Select category from thesis.professors Where " + param + "  AND proficiency = \'Beginner\');")
            BeginnerResult = mycursor.fetchall()
            CleanBeginnerResult = self.getCleanOneTuple(BeginnerResult)
            ListOfBegC.append(CleanBeginnerResult)
##            print(ListOfBegC)

    def Arrange(self, prof, ListOfAdeptC, ListOfBegC, courseCode):
        CourseTable = [[] for x in range(0, len(courseCode)) ]
        for x in range(0, len(courseCode)):
            for y in range(0, len(ListOfAdeptC)):
                if courseCode[x] in ListOfAdeptC[y]:
                    CourseTable[x].append(prof[y])
            if len(CourseTable[x]) == 0:
                for y in range(0, len(ListOfBegC)):
                    if courseCode[x] in ListOfBegC[y]:
                        CourseTable[x].append(prof[y])
						
        return CourseTable
        
