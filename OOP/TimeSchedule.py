# Time scheduling


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
    def schedule_timetabling(self, courseCode, List_prof, tabulist, Classroom):
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


    def fill_sched(self, courseCode, List_prof):
        subMatrix = []
        mainMatrix = []
        numOfSetCourses = 0

        if (len(courseCode) != len(List_prof)):
            return mainMatrix
        for x in range(0, len(courseCode)):
            container = [courseCode[x], List_prof[x]]
            if (len(subMatrix) < 6):
                subMatrix.append(container)
            else:
                mainMatrix.append(subMatrix)
                numOfSetCourses += len(subMatrix)
                subMatrix = []
                subMatrix.append(container)
        if (len(subMatrix) != 0):
            numOfSetCourses += len(subMatrix)
            emptyMatrix = ["", ""]
            while (len(subMatrix) < 6):
                subMatrix.append(emptyMatrix)
            mainMatrix.append(subMatrix)

            subMatrix = []

        for x in range(0, len(courseCode)):
            # based in the constraints, hours / units will be set as a condition here
            # to determine whether to add it to a thursday, friday or saturday sched
            container = [courseCode[x], List_prof[x]]
            if (len(subMatrix) < 6):
                subMatrix.append(container)
            else:
                mainMatrix.append(subMatrix)
                subMatrix = []
                subMatrix.append(container)

        if (len(subMatrix) != 0):
            emptyMatrix = ["", ""]
            while (len(subMatrix) < 6):
                subMatrix.append(emptyMatrix)
            mainMatrix.append(subMatrix)

        for x in range(0, numOfSetCourses):
            courseCode.pop(0)
            List_prof.pop(0)
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





