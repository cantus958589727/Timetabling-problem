# Time scheduling
import random

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

    def matrix_to_Object(self, schedule, Classroom):
        # include monday else No monday *** this maybe wrong so will change in the future
        schedule.insert(0, [])
        if len(schedule) > 5:
            schedule.pop()
            list.append(schedule[0])
            for x in schedule[0]:
                Classroom.available_room_set_prof_m(x[1])
                Classroom.available_room_set_course_m(x[0])
        # -----------------------------------PLEASE REMEMBER TO FIX THIS------------------------------------------------
        # if not more than 4 it doesnt include monday ** for now lets just assume that all schedules are aligned by date
        # tuesday
        for x in schedule[1]:
            Classroom.available_room_set_prof_t(x[1])
            Classroom.available_room_set_course_t(x[0])

        for x in schedule[2]:
            Classroom.available_room_set_prof_w(x[1])
            Classroom.available_room_set_course_w(x[0])

        for x in schedule[3]:
            Classroom.available_room_set_prof_h(x[1])
            Classroom.available_room_set_course_h(x[0])

        for x in schedule[4]:
            Classroom.available_room_set_prof_f(x[1])
            Classroom.available_room_set_course_f(x[0])

    # Schedule function
    def schedule_timetabling(self, courseCode, List_prof, tabulist, Classroom, partition):
        # matrix
        schedules = []
        schedules = self.fill_sched(courseCode, List_prof)
        # change it into Object instead of matrix
        self.matrix_to_Object(schedules, Classroom)
        # -------------------------------Scoring function here------------------------
        #--------------------------------End of Scoring function ---------------------

        if tabulist.checkshort(Classroom):
            tabulist.enqueueShort(Classroom)
        # -------------------------------Long term stuff-------------------------------
            #-----------------------Checking-------------------

            #---------------------End---------------------------
        if tabulist.checkLong(Classroom):
            tabulist.enqueueLong(Classroom)
        #--------------------------------End Long term stuff-------------------------

        tabulist.print_all()

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

    def count_room(self, room):
        counter = 0
        for x in room:
            counter = counter + len(x)

        return counter

    def choose_day(self, room):
        chosenindex = 0
        for x in (1, len(room)):
            if(len(room[chosenindex]) < len(room[x])):
                chosenindex = x
                
        return chosenindex

    def insert_course(self, courseCombination, sched, targetroom, targetday):
        pass
## this function checks if the course is in conflict with the same time and the same prof with other rooms
## returns a true/false value

    def getSpecificCourseList(self, cCombinations, coursename):
## this function gets the combination of a specific list of a specific coursecode
## call chooseRandomCourseCombi
## returns a list of specificCourseCombinationList
        specificList = []
        for x in range(0, len(cCombinations)):
            current = cCombinations[x][0] ## access the coursename cCombinations[x][0] is not final
            if(current == coursename):
                specificList = cCombinations[x]
                random.shuffle(specificList)
                break

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
            
            insertflag = 0
            courseCountPrevious = 0
            ## room = per room
            
            ## assuming currentCourse[0][0] is type of room
            ## lecture rooms
            if(currentCourse[0][0] == "Lecture"):
                for room in range(0, partition)):
                    ##if course inserted successfully, stop searching for available rooms
                    if(insertflag == 1):
                        break
                    ##if current room has no course, insert
                    elif(count_room(sched[1][room]) == 0):
                        chosen_day = self.choose_day(sched[1][room])
                        randSpecificList = self.getSpecificCourseList(cCombinations, currentCourse)
                        for i in randSpecificList :
                            if(insert_course(i, sched, room, chosen_day)):
                                insertflag = 1
                                sched[1][room][chosen_day].append(i)
                                
                        if(insertflag != 1):
                            ##if last class still conflict, insert
                            sched[1][room][chosen_day].append(randSpecificList[len(randSpecificList)])
                    ##if previous room has course
                    elif(courseCountPrevious != 0):
                        ## if previous room has greater course count, then insert 
                        if(courseCountPrevious > count_room(sched[1][room])):
                            chosen_day = self.choose_day(sched[1][room])
                            randSpecificList = self.getSpecificCourseList(cCombinations, currentCourse)
                            for i in randSpecificList :
                                if(insert_course(i, sched)):
                                    insertflag = 1
                                    sched[1][room][chosen_day].append(i)
                                    
                            if(insertflag != 1):
                                ##if last class still conflict, insert
                                sched[1][room][chosen_day].append(randSpecificList[len(randSpecificList)])
                        ## if previous room has less than or equal the current, move to the next room
                        else:
                            courseCountPrevious = count_room(sched[1][room])
                            
                    ##if previous room is not 0
                    else:
                        courseCountPrevious = count_room(sched[1][room])
                    #roomlec loop ends here
                        
                ## if not inserted, insert it at first lec room
                if(insertflag != 1):
                    chosen_day = self.choose_day(sched[1][0])
                    randSpecificList = self.getSpecificCourseList(cCombinations, currentCourse)
                for i in randSpecificList :
                    if(insert_course(i, sched)):
                        insertflag = 1
                        sched[1][0][chosen_day].append(i)
                #lecture if statement ends here
                        
            elif(currentCourse[0][0] == "Laboratory"):
                #room lab loop
                for room in range(partition, len(sched)):
                    ##if course inserted successfully, stop searching for available rooms
                    if(insertflag == 1):
                        break
                    ##if current room has no course, insert
                    elif(count_room(sched[1][room]) == 0):
                        chosen_day = self.choose_day(sched[1][room])
                        randSpecificList = self.getSpecificCourseList(cCombinations, currentCourse)
                        for i in randSpecificList :
                            if(insert_course(i, sched)):
                                insertflag = 1
                                sched[1][room][chosen_day].append(i)

                        if(insertflag != 1):
                            ##if last class still conflict, insert
                            sched[1][room][chosen_day].append(randSpecificList[len(randSpecificList)])
                    ##if previous room has course
                    elif(courseCountPrevious != 0):
                        ## if previous room has greater course count, then insert 
                        if(courseCountPrevious > count_room(sched[1][room])):
                            chosen_day = self.choose_day(sched[1][room])
                            randSpecificList = self.getSpecificCourseList(cCombinations, currentCourse)
                            for i in randSpecificList :
                                if(insert_course(i, sched)):
                                    insertflag = 1
                                    sched[1][room][chosen_day].append(i)
                                    
                            if(insertflag != 1):
                                ##if last class still conflict, insert
                                sched[1][room][chosen_day].append(randSpecificList[len(randSpecificList)])
                        ## if previous room has less than or equal the current, move to the next room
                        else:
                            courseCountPrevious = count_room(sched[1][room])
                            
                    ##if previous room is not 0
                    else:
                        courseCountPrevious = count_room(sched[1][room])
                    #roomlab loop ends here
                        
                ## if not inserted, insert it at first lab room
                if(insertflag != 1):
                    chosen_day = self.choose_day(sched[1][parition])
                    randSpecificList = self.getSpecificCourseList(cCombinations, currentCourse)
                for i in randSpecificList :
                    if(insert_course(i, sched)):
                        insertflag = 1
                        sched[1][parition][chosen_day].append(i)
                #laboratory if statement ends here
                    
            #currentcourseloop continues here
                
            #currentcourseloop ends here
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





