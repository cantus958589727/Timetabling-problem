# Time scheduling
import random
from Classroom import*
import copy

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

    def move_course(self, timeslot, sched, partition, courseOffered, random, flowchart):
        #print(sched[0].get_monday_time()[0].get_course())
        #input()
        if(random == 1):
            #copy the else and change it randomly
            for x in timeslot:
                roomtype = self.check_course_room(courseOffered, sched[x[0]].get_time(x[1])[x[2]])

                lowerbound = 0
                upperbound = len(sched)
    
                if(roomtype == "Lecture"):
                    upperbound = partition
                elif(roomtype == "Laboratory"):
                    lowerbound = parition

                check = False
                while(check != True):
                    room = random.randint(lowerbound-1 , upperbound)
                    day = random.randint(0,2)
                    slot = random.randint(-1, len(sched[room].get_time(day)))

                    indexval = []
                    indexval.append(room)
                    indexval.append(day)
                    indexval.append(slot)
                            
                    if(timeslot == indexval):
                        pass
                    else:
                        check = self.check_conflict_slot(sched, x, indexval)
                        check = self.check_conflict_slot(sched, indexval, x)
                                
                    if(check == True):
                        break
                    #end of while loop
                    
                #perform swap
##                print("Start swap..")
##                print("type: Random")
##                print("origin:")
##                print(sched[x[0]].get_time(x[1])[x[2]].toString())
##                print(x)
##                sched[x[0]].print_all()
##                print("target:")
##                print(sched[indexval[0]].get_time(indexval[1])[indexval[2]].toString())
##                print(indexval)
##                sched[indexval[0]].print_all()
                origin = sched[x[0]].get_time(x[1])[x[2]]
                target = sched[indexval[0]].get_time(indexval[1])[indexval[2]]
                
                sched[x[0]].set_slot(x[1], target, x[2])
                sched[x[0]].set_slot(x[1]+2, target, x[2])
                sched[indexval[0]].set_slot(indexval[1], origin, indexval[2])
                sched[indexval[0]].set_slot(indexval[1]+2, origin, indexval[2])
##                print("origin:")
##                print(sched[x[0]].get_time(x[1])[x[2]].toString())
##                print(x)
##                sched[x[0]].print_all()
##                print("target:")
##                print(sched[indexval[0]].get_time(indexval[1])[indexval[2]].toString())
##                print(indexval)
##                sched[indexval[0]].print_all()
##                print("End swap..")
##                input()
        else:

            for x in timeslot:  
                roomtype = self.check_course_room(courseOffered, sched[x[0]].get_time(x[1])[x[2]])

                lowerbound = 0
                upperbound = len(sched)
                
                if(roomtype == "Lecture"):
                    upperbound = partition
                elif(roomtype == "Laboratory"):
                    lowerbound = parition
                
                
                for room in range(lowerbound, upperbound):
                    
                    check = False
                    for day in range(1,3):
                        for slot in range(0, len(sched[room].get_time(day))):
                            indexval = []
                            indexval.append(room)
                            indexval.append(day)
                            indexval.append(slot)

                            if(x == indexval):
##                                print("same")
                                pass
                            else:
                                check = self.check_conflict_slot(sched, x, indexval)
                                check = self.check_conflict_slot(sched, indexval, x)
                                
                            if(check == True):
                                break
                            
                            #end of slot loop
                        if(check == True):
                            break

                        
                        #end of day loop
                    
                    if(check == True):
                        break  
                    #end of room loop

                #perform swap
##                print("Start swap..")
##                print("type: Non Random")
##                print("origin:")
##                print(sched[x[0]].get_time(x[1])[x[2]].toString())
##                print(x)
##                sched[x[0]].print_all()
##                print("target:")
##                print(sched[indexval[0]].get_time(indexval[1])[indexval[2]].toString())
##                print(indexval)
##                sched[indexval[0]].print_all()
                origin = sched[x[0]].get_time(x[1])[x[2]]
                target = sched[indexval[0]].get_time(indexval[1])[indexval[2]]
                
                sched[x[0]].set_slot(x[1], target, x[2])
                sched[x[0]].set_slot(x[1]+2, target, x[2])
                sched[indexval[0]].set_slot(indexval[1], origin, indexval[2])
                sched[indexval[0]].set_slot(indexval[1]+2, origin, indexval[2])
##                print("origin:")
##                print(sched[x[0]].get_time(x[1])[x[2]].toString())
##                print(x)
##                sched[x[0]].print_all()
##                print("target:")
##                print(sched[indexval[0]].get_time(indexval[1])[indexval[2]].toString())
##                print(indexval)
##                sched[indexval[0]].print_all()
##                print("End swap..")
##                input()
                #end of timeslot loop
            
            #end of else
        #end of move_course function
                    
    def check_conflict_slot(self, sched, slot, target):
        #print(slot)
##        print("evaluating..")
        prof = sched[slot[0]].get_time(slot[1])[slot[2]].get_prof()
        course = sched[slot[0]].get_time(slot[1])[slot[2]].get_course()
        day = target[1]
        time = target[2]
        
        check = True
        
        for room in range(0, len(sched)):
##            print(prof, "vs" , sched[room].get_time(day)[time].get_prof())
##            print(course, "vs", sched[room].get_time(day)[time].get_course())
            if(room == target[0]):
##                print("target")
##                print(prof, "vs" , sched[room].get_time(day)[time].get_prof())
##                print(course, "vs", sched[room].get_time(day)[time].get_course())
##                input()
                pass
##            elif(day % 2 == 1):
##                #TH
##                print(sched[room].get_tuesday_time()[time].get_prof(), "vs" , prof)
##                print(sched[room].get_tuesday_time()[time].get_course(), "vs", course)
##                if(sched[room].get_tuesday_time()[time].get_prof() == prof or sched[room].get_tuesday_time()[time].get_course() == course):
##                    check = False
##            elif(day % 2 == 0):
##                #WF
##                print(sched[room].get_wednesday_time()[time].get_prof(), "vs" , prof)
##                print(sched[room].get_wednesday_time()[time].get_course(), "vs", course)
            elif(sched[room].get_time(day)[time].get_prof() == prof and sched[room].get_time(day)[time].get_course() == course):
##                print("wat")
##                print(prof, "vs" , sched[room].get_time(day)[time].get_prof())
##                print(course, "vs", sched[room].get_time(day)[time].get_course())
##                input()
                pass
            
            elif(sched[room].get_time(day)[time].get_prof() == prof):
##                print("Conflict!")
##                print(prof, "vs" , sched[room].get_time(day)[time].get_prof())
##                print(course, "vs", sched[room].get_time(day)[time].get_course())
##                input()
                check = False

            if(check == False):
                break

##        if(check == True):
##            print(prof, "-->", sched[room].get_time(day)[time].get_prof())
##            print(course, "-->", sched[room].get_time(day)[time].get_course())
            
        return check
        #check if the slot chosen is in conflict with the other prof and flowchart
        #this function will check if the target and chosen slot can be swapped
                        
    
    def check_course_room(self, coursecode, target):

        room = ""
        
        for x in range(0, len(coursecode)):
            #print(coursecode[x])
            if coursecode[x][0] == target.get_course:
                room = coursecode[x][1]
                break
        return room
                
    # Schedule function
    def schedule_timetabling(self, courseCode, List_prof, tabulist, Classroom, partition, combination, flowCourse):
        # matrix
        #print("test")
        schedules = []
##        schedules = self.fill_sched(courseCode, List_prof, Classroom, partition, combination)
        schedules = self.fill_schedv2(courseCode, combination, Classroom, partition)
        #self.printschedule(schedules)
        # change it into Object instead of matrix
        ClassroomList = []
        self.matrix_to_Object(schedules, ClassroomList)
        self.scoringFunction(tabulist, ClassroomList)
        flag = True
        while flag:
            self.improveSchedule(ClassroomList, flowCourse, partition, courseCode)
            self.scoringFunction(tabulist, ClassroomList)
            # if condition
            # quit the loop

            flag = False

        #--------------------------------End Long term stuff-------------------------
        #tabulist.print_short()
        print("size: ",tabulist.sizeShort())
        

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

    def get_FlowCourse_count(self, courseArray, ClassroomList, timeslot, arrayCount, flowCourse):
        for perClass in range(0, len(ClassroomList)):
            courseArray.append(ClassroomList[perClass].get_monday_time()[timeslot].get_course())
            courseArray.append(ClassroomList[perClass].get_tuesday_time()[timeslot].get_course())
            courseArray.append(ClassroomList[perClass].get_wednesday_time()[timeslot].get_course())
            courseArray.append(ClassroomList[perClass].get_thursday_time()[timeslot].get_course())
            courseArray.append(ClassroomList[perClass].get_friday_time()[timeslot].get_course())
            
        for perCourse in flowCourse:
            arrayCount.append(courseArray.count(perCourse))

    def improveSchedule(self, ClassroomList, flowCourse, partition, courseCode):
        # fix the course, ensure that there where no conflict in course for students
        for timeslot in range(0, 6):
            courseArray = []
            # check the courseArray, if the course appear more once
            arrayCount = []
            self.get_FlowCourse_count(courseArray, ClassroomList, timeslot, arrayCount, flowCourse)
            # assume every class is 1.5 hrs
            counter = 0
            while( arrayCount.count(0) < len(flowCourse) -2 ):
                if arrayCount[counter] > 0:
                    #randomly choose a course
                    #if random.randint(0, 2) > 0:
                    #not randomly
                    if True == True:
                        for perClass in range(0, len(ClassroomList)):
##                            if flowCourse[counter] == ClassroomList[perClass].get_monday_time()[timeslot].get_course():
##                            # array[room, day, slot], scheule, partition, courseCode, (0(random),1(not random), flowCourse)
##                                self.move_course([ perClass, ,],)
##                                arrayCount[counter] -= 2
                            if flowCourse[counter] == ClassroomList[perClass].get_tuesday_time()[timeslot].get_course():
                                self.move_course([[ perClass, 1, timeslot]], ClassroomList, partition, courseCode, 0, flowCourse)
                                arrayCount[counter] -= 2
                            if flowCourse[counter] == ClassroomList[perClass].get_wednesday_time()[timeslot].get_course():
                                self.move_course([[ perClass, 2, timeslot]], ClassroomList, partition, courseCode, 0, flowCourse)
                                arrayCount[counter] -= 2
##                            if flowCourse[counter] == ClassroomList[perClass].get_thursday_time()[timeslot].get_course():
##                                arrayCount[counter] -= 1
##                            if flowCourse[counter] == ClassroomList[perClass].get_friday_time()[timeslot].get_course():
##                                arrayCount[counter] -= 1
                counter = counter + 1
                if counter > (len(arrayCount) - 1):
                    counter = 0
                    self.get_FlowCourse_count(courseArray, ClassroomList, timeslot, arrayCount, flowCourse)
                    
    def scoringFunction(self, tabulist, ClassroomList):
        # -------------------------------Scoring function here------------------------
        #--------------------------------End of Scoring function ---------------------

        print("class before putting in tabu list")
        ClassroomList[0].print_all()
        if tabulist.checkshort(ClassroomList):
            print("check short is true")
            tabulist.enqueueShort(copy.deepcopy(ClassroomList))
            tabulist.short[0][0].print_all()
        # -------------------------------Long term stuff-------------------------------
            #-----------------------Checking-------------------

            #---------------------End---------------------------
        if tabulist.checkLong(ClassroomList):
            tabulist.enqueueLong(copy.deepcopy(ClassroomList))
                
    def count_room(self, room):
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
##                        print(sched[0][room], "none")
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
##                        print(sched[0][room], "none")
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





