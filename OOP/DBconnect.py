import mysql.connector

class DBconnect(object):

    def __init__(self):
        self.mydb = mysql.connector.connect(
               host = "localhost",
               user = "root",
               passwd = "mysql11",
               database = "thesis"
        )

    def getCleanOneTuple(self, data):
        rawData = data
        cleanData = []
        for x in range(0, len(rawData)):
            cleanData.append( rawData[x][0] )

        return cleanData

    def getCourseCodeFromDB(self, courseID):
        
        mycursor = self.mydb.cursor()

        param = ''
        for x in range(0, len(courseID)):
            param += "course_id = " + str(courseID[x])
            if(x < len(courseID)-1):
               param += ' OR '

    ##    print(param)
        mycursor.execute("SELECT course_code FROM course WHERE " + param)
        
        myresult = mycursor.fetchall()

        return myresult

    def getProfFromDB(self):

        mycursor = self.mydb.cursor()

        mycursor.execute("SELECT user_id FROM faculty LIMIT 10")

        myresult = mycursor.fetchall()

        return myresult

    def getCourseIdFromDB(self):

        mycursor = self.mydb.cursor()

        mycursor.execute("SELECT course_id FROM course LIMIT 10")

        myresult = mycursor.fetchall()

        return myresult

    def getUnitsFromDB(self):

        mycursor = self.mydb.cursor()

        mycursor.execute("SELECT units FROM course LIMIT 10")

        myresult = mycursor.fetchall()

        return myresult

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

        mycursor.execute("SELECT thesisschema.building.﻿building_id FROM thesisschema.building where thesisschema.building.building_code = \"GK\";")

        RoomCodeGK = mycursor.fetchall()

        mycursor.execute("SELECT room_code, room_type FROM thesisschema.room Where building_id = " + str(RoomCodeGK[0][0]) + ";")

        myresult = mycursor.fetchall()

##        print(classifyRooms(myresult))
        return self.classifyRooms(myresult)
        #pass

    
