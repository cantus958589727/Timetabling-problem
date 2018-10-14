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
        self.test()
        self.course_id = []

    # Schedule function
    @staticmethod
    def random_schedule(class_room_list, prof):
        for x in range(0, 4):
            class_room_list[0].available_room_set_prof_mw(prof)
        for x in range(0, 4):
            class_room_list[0].available_room_set_prof_th(prof)

    def test(self):
        self.course_id = ['1919', '1920']
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
