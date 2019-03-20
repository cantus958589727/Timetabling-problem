# Time scheduling
import random
from Classroom import*

class TimeSchedule(object):
    # init
    def __init__(self):
        # self.mydb = mysql.connector.connect(host="localhost",
        # user="yourusername",
        #            passwd="yourpassword",
        #            database="mydatabase")
        #        self.mycursor = self.mydb.cursor()
        #        self.counter = 0
        #        #self.initialize()
        self.course_id = [['1919'], ['1920']]
        # def initialize(self):
        # self.mycursor.execute(Select course_id from course)
        # self.courseid = self.mycursor.fetchall()
        # def getCourse(self):
        # def random(self):
        # def nextCourse(self):
        #    if(self.counter >= len(self.courseid)):
        #        self.counter = 0
        #    index = self.counter
        #    self.counter++
        #    return self.courseid[index]

    # import mysql.connector
    # mydb = mysql.connector.connect(
    #   host="localhost",
    #   user="yourusername",
    #   passwd="yourpassword",
    #   database="mydatabase"
    # )
    # mycursor = mydb.cursor()
    # mycursor.execute("SELECT * FROM customers")
    # myresult = mycursor.fetchall()
    # for x in myresult:
    #   print(x)

    def matrix_to_Object(self, schedule, ClassroomList):
        # include monday else No monday *** this maybe wrong so will change in the future
        #schedule.insert(0, [])
        #if len(schedule) > 5:
        #    schedule.pop()
        #    list.append(schedule[0])
        #    for x in schedule[0]:
        #        Classroom.available_room_set_prof_m(x[1])
        #        Classroom.available_room_set_course_m(x[0])
        # -----------------------------------PLEASE REMEMBER TO FIX THIS------------------------------------------------
        # if not more than 4 it doesnt include monday ** for now lets just assume that all schedules are aligned by date
        # tuesday
##        for x in schedule[1]:
##            Classroom.available_room_set_prof_t(x[1])
##            Classroom.available_room_set_course_t(x[0])
##
##        for x in schedule[2]:
##            Classroom.available_room_set_prof_w(x[1])
##            Classroom.available_room_set_course_w(x[0])
##
##        for x in schedule[3]:
##            Classroom.available_room_set_prof_h(x[1])
##            Classroom.available_room_set_course_h(x[0])
##
##        for x in schedule[4]:
##            Classroom.available_room_set_prof_f(x[1])
##            Classroom.available_room_set_course_f(x[0])
##        print("Schedule:")
##        for x in range(0, len(sched[1])):
##            print("Room %s:" % sched[0][x])
##            for y in range(0, len(sched[1][x])):
##                print("Day %d:" % y)
##                print(sched[1][x][y])
        #for x in range(0, len(schedule[1])):
        #    print(schedule[1])
        for x in range(0, len(schedule[0])):
            TempClassroom = Classroom(schedule[0][x])
            room = schedule[1][x]
            if room[0] is not None: 
                for sched in room[0]:
                    TempClassroom.available_room_set_prof_m(sched[1])
                    TempClassroom.available_room_set_course_m(sched[0])

            if room[1] is not None: 
                for sched in room[1]:
                    TempClassroom.available_room_set_prof_t(sched[1])
                    TempClassroom.available_room_set_course_t(sched[0])

            if room[2] is not None: 
                for sched in room[2]:
                    TempClassroom.available_room_set_prof_w(sched[1])
                    TempClassroom.available_room_set_course_w(sched[0])

            if room[3] is  not None: 
                for sched in room[3]:
                    TempClassroom.available_room_set_prof_h(sched[1])
                    TempClassroom.available_room_set_course_h(sched[0])

            if room[4] is not None:
                for sched in room[4]:
                    TempClassroom.available_room_set_prof_f(sched[1])
                    TempClassroom.available_room_set_course_f(sched[0])
            ClassroomList.append(TempClassroom)

    # Schedule function
    def schedule_timetabling(self, courseCode, List_prof, tabulist, Classroom, partition, combination):
        # matrix
        print("test")
        schedules = []
##        schedules = self.fill_sched(courseCode, List_prof, Classroom, partition, combination)
        schedules = self.fill_schedv2(courseCode, combination, Classroom, partition)
        #self.printschedule(schedules)
        # change it into Object instead of matrix
        self.ClassroomList = []
        self.matrix_to_Object(schedules, self.ClassroomList)
        # -------------------------------Scoring function here------------------------
        #--------------------------------End of Scoring function ---------------------

        if tabulist.checkshort(self.ClassroomList):
            tabulist.enqueueShort(self.ClassroomList)
        # -------------------------------Long term stuff-------------------------------
            #-----------------------Checking-------------------

            #---------------------End---------------------------
        if tabulist.checkLong(self.ClassroomList):
            tabulist.enqueueLong(self.ClassroomList)
        #--------------------------------End Long term stuff-------------------------
##        for x in ClassroomList:
##            x.print_all()
##        tabulist.print_all()

##    def chooseRandomCourseCombi(self, specificCourseList):
#### this function gets a random combination of course and prof
#### returns an array of indexes of the specificCourseCombinationList in random order
##        rangeOfIndices = list(range(len(specificCourseList)))
##        randomizedIndices = []
##        while rangeOfIndices:
##            posit = random.randrange(len(rangeOfIndices))
##            randomizedIndices.append(specificCourseList[posit])
##        
##            rangeOfIndices.pop(posit)
##
##        return randomizedIndices
    
##    return randomizedIndices

    def printschedule(self, sched):
        print("Schedule:")
        for x in range(0, len(sched[1])):
            print("Room %s:" % sched[0][x])
            for y in range(0, len(sched[1][x])):
                print("Day %d:" % y)
                print(sched[1][x][y])
                
    def count_room(self, room):
        #if(len(room) == 0):
            #print("wow")
        counter = 0
        for y in room[1]:
            for z in room[3]:
                if(y == z):
                    counter = counter + 1
                else:
                    counter = counter + 2
        for y in room[2]:
            for z in room[4]:
                if(y == z):
                    counter = counter + 1
                else:
                    counter = counter + 2
                    
        return counter

    def isDayEqual(self, day1, day2):
        if(day1 == day2):
            return True
        else:
            return False
        
    def choose_day(self, room):
        ## assuming subjects are fixed twice a week with one day interval
        chosenindex = 0
        chosenindex2 = 0
        equal = 0
        for x in range(1, 3):
            if(chosenindex != 0):
                equal = 0
                if(len(room[chosenindex]) > len(room[x])):
                    if(len(room[x]) == len(room[x+2])):
                        chosenindex2 = x
                        equal = 1
                    elif(len(room[chosenindex]) > len(room[x+2])):
                        chosenindex2 = x+2
                    else:
                        pass
                else:
                    if(len(room[x]) == len(room[x+2])):
                        chosenindex2 = x
                        equal = 1
                    elif(len(room[x]) > len(room[x+2])):
                        chosenindex2 = x+2
                    else:
                        chosenindex2 = x

            elif(len(room[x]) == len(room[x+2])):
                chosenindex = x
                equal = 0
            else:
                equal = 0
                if(len(room[x]) > len(room[x+2])):
                   chosenindex = x+2
                else:
                   chosenindex = x

##        print(chosenindex, chosenindex2, len(room[chosenindex]), len(room[chosenindex2]))
                                             
        if(chosenindex == 0):
            return chosenindex2
        elif(chosenindex2 == 0):
            return chosenindex
        if(len(room[chosenindex]) > len(room[chosenindex2])):
            return chosenindex2
        else:
            return 1
            
        
        

    def insert_course(self, prof, sched, targetroom, targetday):
        ## follows TH and WF rules
        ## traverse all rooms
        
        allow = 1
        #print(targetroom)
        #print(targetday)
        #print(sched[1])
##        print(sched[targetroom][targetday])
        if sched[1][targetroom][targetday] is None:
            targetTime = 0
        else:
            targetTime = len(sched[1][targetroom][targetday])
            
        for x in range(0, len(sched[1])):
            ## traverse specific rooms
            for y in range(1,3):
                
                ## check all timeslot in all rooms
                if sched[1][x][y] is None:
                    #print("none")
                    pass
                elif(targetTime < len(sched[1][x][y])):
                    #print(sched[1][x][y])
                    if sched[1][x][y][targetTime] is None:
                        pass
                    elif(sched[1][x][y][targetTime][1] == prof):
                        allow = 0
                        break

        if(allow):
            #print("true")
            return True
        else:
            #print("false")
            return False
                           
                            
                
## this function checks if the course is in conflict with the same time and the same prof with other rooms
## returns a true/false value

    def getSpecificCourseList(self, cCombinations, coursename, coursecodes):
## this function gets the combination of a specific list of a specific coursecode
## call chooseRandomCourseCombi
## returns a list of specificCourseCombinationList
        specificList = []
        for x in range(0, len(coursecodes)): ## access the coursename cCombinations[x][0] is not final
            if(coursecodes[x][0] == coursename):
                specificList = cCombinations[x]
                random.shuffle(specificList)
                break
        #print("In get specificlist function", specificList)
        return specificList
        
    def fill_schedv2(self, courseOffered, cCombinations, sched, partition):
##      lacks the following function(s) implementation:
##          insert_course
##      courseOffered is an array of coursecode strings
##      How to access:
##       sched[0] = list of rooms
##       sched[0][0] = name of first room
##       sched[1] = list of schedule per room
##       sched[1][0] = schedule of first room
##       therefore: sched[0][n] == sched[1][n]
        
        for currentCourse in range(0, len(courseOffered)):
##            print("test" , currentCourse)
            #print("currentCourse", courseOffered[currentCourse])
            room = 0
            insertflag = 0
            courseCountPrevious = 0
            approvedcombi = []
            ## room = per room
            
            ## assuming currentCourse[0][0] is type of room
            ## lecture rooms
            if(courseOffered[currentCourse][1] == "Lecture"):
                #print("is lec")
                for room in range(0, partition):
##                    print(sched[1][room])
                    #print("room num:", room)
                    ##if course inserted successfully, stop searching for available rooms
                    if(insertflag == 1):
                        break
                    ##if current room has no course, insert
                    elif sched[1][room] is None:
                        print(sched[0][room], "none")
                        chosen_day = self.choose_day(sched[1][room])
                        randSpecificList = self.getSpecificCourseList(cCombinations, courseOffered[currentCourse][0], courseOffered)
                        if(len(randSpecificList) == 0):
                            approvedcombi.append(courseOffered[currentCourse][0])
                            approvedcombi.append(" ")
                            insertflag = 1
                            sched[1][room][chosen_day].append(approvedcombi)
                            sched[1][room][chosen_day+2].append(approvedcombi)
                            
                        else:
                            for i in randSpecificList :
                                if(self.insert_course(i, sched, room, chosen_day)):
                                    approvedcombi.append(courseOffered[currentCourse][0])
                                    approvedcombi.append(i)
                                    insertflag = 1
                                    sched[1][room][chosen_day].append(approvedcombi)
                                    sched[1][room][chosen_day+2].append(approvedcombi)
                                    break
                                
                        if(insertflag != 1):
                            #print(chosen_day, "chosen")
                            #print("room", sched[1][room])
##                            print(randSpecificList)
##                            print(randSpecificList[len(randSpecificList)-1])
                            ##if last class still conflict, insert
                            if(len(randSpecificList) == 0):
                                approvedcombi.append(courseOffered[currentCourse][0])
                                approvedcombi.append(" ")
                                insertflag = 1
                                sched[1][room][chosen_day].append(approvedcombi)
                                sched[1][room][chosen_day+2].append(approvedcombi)
                            
                            else:
                                for i in randSpecificList :
                                    if(self.insert_course(i, sched, room, chosen_day)):
                                        approvedcombi.append(courseOffered[currentCourse][0])
                                        approvedcombi.append(i)
                                        insertflag = 1
                                        sched[1][room][chosen_day].append(approvedcombi)
                                        sched[1][room][chosen_day+2].append(approvedcombi)
                                        break
                    ##if previous room has course
                    elif(courseCountPrevious != 0):
                        ## if previous room has greater course count, then insert 
                        if(courseCountPrevious > self.count_room(sched[1][room])):
                            chosen_day = self.choose_day(sched[1][room])
                            randSpecificList = self.getSpecificCourseList(cCombinations, courseOffered[currentCourse][0], courseOffered)
                            if(len(randSpecificList) == 0):
                                approvedcombi.append(courseOffered[currentCourse][0])
                                approvedcombi.append(" ")
                                insertflag = 1
                                sched[1][room][chosen_day].append(approvedcombi)
                                sched[1][room][chosen_day+2].append(approvedcombi)
                                
                            else:
                                for i in randSpecificList :
                                    if(self.insert_course(i, sched, room, chosen_day)):
                                        approvedcombi.append(courseOffered[currentCourse][0])
                                        approvedcombi.append(i)
                                        insertflag = 1
                                        sched[1][room][chosen_day].append(approvedcombi)
                                        sched[1][room][chosen_day+2].append(approvedcombi)
                                        break
                                
                                    
                            if(insertflag != 1):
                                randSpecificList = self.getSpecificCourseList(cCombinations, courseOffered[currentCourse][0], courseOffered)
                                ##if last class still conflict, insert
                                #print(chosen_day, "chosen")
                                #print("room", sched[1][room])
##                                print(randSpecificList)
##                                print(randSpecificList[len(randSpecificList)-1])
##                                sched[1][room][chosen_day].append(randSpecificList[len(randSpecificList)-1])
                                if(len(randSpecificList) == 0):
                                    approvedcombi.append(courseOffered[currentCourse][0])
                                    approvedcombi.append(" ")
                                    insertflag = 1
                                    sched[1][room][chosen_day].append(approvedcombi)
                                    sched[1][room][chosen_day+2].append(approvedcombi)
                            
                                else:
                                    for i in randSpecificList :
                                        if(self.insert_course(i, sched, room, chosen_day)):
                                            approvedcombi.append(courseOffered[currentCourse][0])
                                            approvedcombi.append(i)
                                            insertflag = 1
                                            sched[1][room][chosen_day].append(approvedcombi)
                                            sched[1][room][chosen_day+2].append(approvedcombi)
                                            break
                        ## if previous room has less than or equal the current, move to the next room
                        else:
                            courseCountPrevious = self.count_room(sched[1][room])
                            
                    ##if previous room is not 0
                    else:
                        courseCountPrevious = self.count_room(sched[1][room])
                    #roomlec loop ends here
                        
                ## if not inserted, insert it at first lec room
                if(insertflag != 1):
                    chosen_day = self.choose_day(sched[1][0])
                    randSpecificList = self.getSpecificCourseList(cCombinations, courseOffered[currentCourse][0], courseOffered)
                    for i in randSpecificList :
                        if(self.insert_course(i, sched, room, chosen_day)):
                            approvedcombi.append(courseOffered[currentCourse][0])
                            approvedcombi.append(i)
                            insertflag = 1
                            sched[1][0][chosen_day].append(approvedcombi)
                            sched[1][0][chosen_day+2].append(approvedcombi)
                            break
                #lecture if statement ends here
                        
            elif(courseOffered[currentCourse][1] == "Laboratory"):
                #room lab loop
                #print("is lab")
                #print("test")
                for room in range(partition, len(sched[1])):
##                    print(sched[1][room])
                    #print("room num:", room)
                    ##if course inserted successfully, stop searching for available rooms
                    if(insertflag == 1):
                        break
                    ##if current room has no course, insert
                    elif sched[1][room] is None:
                        print(sched[0][room], "none")
                        chosen_day = self.choose_day(sched[1][room])
                        randSpecificList = self.getSpecificCourseList(cCombinations, courseOffered[currentCourse][0], courseOffered)
                        if(len(randSpecificList) == 0):
                            approvedcombi.append(courseOffered[currentCourse][0])
                            approvedcombi.append(" ")
                            insertflag = 1
                            sched[1][room][chosen_day].append(approvedcombi)
                            sched[1][room][chosen_day+2].append(approvedcombi)
                            
                        else:
                            for i in randSpecificList :
                                if(self.insert_course(i, sched, room, chosen_day)):
                                    approvedcombi.append(courseOffered[currentCourse][0])
                                    approvedcombi.append(i)
                                    insertflag = 1
                                    sched[1][room][chosen_day].append(approvedcombi)
                                    sched[1][room][chosen_day+2].append(approvedcombi)
                                    break

                        if(insertflag != 1):
                            #print(chosen_day, "chosen")
                            #print("room", sched[1][room])
##                            print(randSpecificList)
##                            print(randSpecificList[len(randSpecificList)-1])
                            ##if last class still conflict, insert
                            if(len(randSpecificList) == 0):
                                approvedcombi.append(courseOffered[currentCourse][0])
                                approvedcombi.append(" ")
                                insertflag = 1
                                sched[1][room][chosen_day].append(approvedcombi)
                                sched[1][room][chosen_day+2].append(approvedcombi)
                            
                            else:
                                for i in randSpecificList :
                                    if(self.insert_course(i, sched, room, chosen_day)):
                                        approvedcombi.append(courseOffered[currentCourse][0])
                                        approvedcombi.append(i)
                                        insertflag = 1
                                        sched[1][room][chosen_day].append(approvedcombi)
                                        sched[1][room][chosen_day+2].append(approvedcombi)
                                        break
                                    
                    ##if previous room has course
                    elif(courseCountPrevious != 0):
                        ## if previous room has greater course count, then insert 
                        if(courseCountPrevious > self.count_room(sched[1][room])):
                            chosen_day = self.choose_day(sched[1][room])
                            randSpecificList = self.getSpecificCourseList(cCombinations, courseOffered[currentCourse][0], courseOffered)
                            if(len(randSpecificList) == 0):
                                approvedcombi.append(courseOffered[currentCourse][0])
                                approvedcombi.append(" ")
                                insertflag = 1
                                sched[1][room][chosen_day].append(approvedcombi)
                                sched[1][room][chosen_day+2].append(approvedcombi)
                                
                            else:
                                for i in randSpecificList :
                                    if(self.insert_course(i, sched, room, chosen_day)):
                                        approvedcombi.append(courseOffered[currentCourse][0])
                                        approvedcombi.append(i)
                                        insertflag = 1
                                        sched[1][room][chosen_day].append(approvedcombi)
                                        sched[1][room][chosen_day+2].append(approvedcombi)
                                        break
                                    
                            if(insertflag != 1):
                                #print(chosen_day, "chosen")
                                #print("room", sched[1][room])
##                            print(randSpecificList)
##                            print(randSpecificList[len(randSpecificList)-1])
                            ##if last class still conflict, insert
                                if(len(randSpecificList) == 0):
                                    approvedcombi.append(courseOffered[currentCourse][0])
                                    approvedcombi.append(" ")
                                    insertflag = 1
                                    sched[1][room][chosen_day].append(approvedcombi)
                                    sched[1][room][chosen_day+2].append(approvedcombi)
                                    
                                else:
                                    for i in randSpecificList :
                                        if(self.insert_course(i, sched, room, chosen_day)):
                                            approvedcombi.append(courseOffered[currentCourse][0])
                                            approvedcombi.append(i)
                                            insertflag = 1
                                            sched[1][room][chosen_day].append(approvedcombi)
                                            sched[1][room][chosen_day+2].append(approvedcombi)
                                            break
                        ## if previous room has less than or equal the current, move to the next room
                        else:
                            courseCountPrevious = self.count_room(sched[1][room])
                            
                    ##if previous room is not 0
                    else:
                        courseCountPrevious = self.count_room(sched[1][room])
                    #roomlab loop ends here
                        
                ## if not inserted, insert it at first lab room
                if(insertflag != 1):
                    #print("lab not inserted")
                    chosen_day = self.choose_day(sched[1][partition])
                    randSpecificList = self.getSpecificCourseList(cCombinations, courseOffered[currentCourse][0], courseOffered)
                    #print(chosen_day, "chosen")
                    #print("room", sched[1][room])
##                            print(randSpecificList)
##                            print(randSpecificList[len(randSpecificList)-1])
                    ##if last class still conflict, insert
                    if(len(randSpecificList) == 0):
                        approvedcombi.append(courseOffered[currentCourse][0])
                        approvedcombi.append(" ")
                        insertflag = 1
                        sched[1][partition][chosen_day].append(approvedcombi)
                        sched[1][partition][chosen_day+2].append(approvedcombi)
                            
                    else:
                        for i in randSpecificList :
                            if(self.insert_course(i, sched, room, chosen_day)):
                                approvedcombi.append(courseOffered[currentCourse][0])
                                approvedcombi.append(i)
                                insertflag = 1
                                sched[1][partition][chosen_day].append(approvedcombi)
                                sched[1][partition][chosen_day+2].append(approvedcombi)
                                break
                #laboratory if statement ends here
                    
            #currentcourseloop continues here
                
            #currentcourseloop ends here
                       
        return sched
        #end of fill_schedv2
                    
    def fill_sched(self, courseCode, List_prof):
##      check fill_schedv2
##      pass the coursecombinations and empty schedule

        
##        subMatrix = []
##        mainMatrix = []
##        numOfSetCourses = 0

        
##        if (len(courseCode) != len(List_prof)):
##            return mainMatrix
##        for x in range(0, len(courseCode)):
##            container = [courseCode[x], List_prof[x]]
##            if (len(subMatrix) < 6):
##                subMatrix.append(container)
##            else:
##                mainMatrix.append(subMatrix)
##                numOfSetCourses += len(subMatrix)
##                subMatrix = []
##                subMatrix.append(container)
##        if (len(subMatrix) != 0):
##            numOfSetCourses += len(subMatrix)
##            emptyMatrix = ["", ""]
##            while (len(subMatrix) < 6):
##                subMatrix.append(emptyMatrix)
##            mainMatrix.append(subMatrix)
##
##            subMatrix = []
##
##        for x in range(0, len(courseCode)):
##            # based in the constraints, hours / units will be set as a condition here
##            # to determine whether to add it to a thursday, friday or saturday sched
##            container = [courseCode[x], List_prof[x]]
##            if (len(subMatrix) < 6):
##                subMatrix.append(container)
##            else:
##                mainMatrix.append(subMatrix)
##                subMatrix = []
##                subMatrix.append(container)
##
##        if (len(subMatrix) != 0):
##            emptyMatrix = ["", ""]
##            while (len(subMatrix) < 6):
##                subMatrix.append(emptyMatrix)
##            mainMatrix.append(subMatrix)
##
##        for x in range(0, numOfSetCourses):
##            courseCode.pop(0)
##            List_prof.pop(0)
        ##    for x in range(0 , len(matrix)/2):
        ##        for y in range(x*5, x+5):
        ##            subMatrix.append(matrix[y])

        return mainMatrix


    def random_schedule(self, class_room_list, prof):
        for x in range(0, 6):
            class_room_list[0].available_room_set_prof_mw(prof)
        for x in range(0, 6):
            class_room_list[0].available_room_set_prof_th(prof)
        for x in range(0, len(self.course_id)):
            if class_room_list[0].available_room_set_course(self.course_id[x]):
                print('course set')

    # def set_sched_manually(self, class_room, ):

    def tabulist(self, tabu_list, schedule):
        # short-term
        # check if the sched is in the
        if tabu_list.checkshort(schedule):
            tabu_list.enqueueLong(schedule)





