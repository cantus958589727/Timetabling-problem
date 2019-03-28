from Classroom import*
from TimeSchedule import*
from tabulist import*
from DBconnect import*
from DataManipulator import*
from GUI import *
import xlrd

print("START")
#[ Department, Term, Year ]
#UserInput = []
#frame = GUI(UserInput)

tabu_list = tabulist()
DBConnect = DBconnect()
DM = DataManipulator()

classified_rooms = DBConnect.getRoomsFromDB()
##print(classified_rooms)
Lecs = DM.InstantiateMultipleClassrooms(classified_rooms[0])
Labs = DM.InstantiateMultipleClassrooms(classified_rooms[1])

flowCourse = DBConnect.getFlowChartFromDB(2015)

print(Lecs)
print(Labs)

labels = []
schedules = []

ClassRoomList = []
ClassRoomList.append(labels)

ClassRoomList[0].extend(Lecs)
partition = len(ClassRoomList[0])
print("partition:", partition)
ClassRoomList[0].extend(Labs)
print(ClassRoomList[0][partition])

ClassRoomList.append(schedules)

ClassRoomList = DM.prepareScheduleHolder(ClassRoomList)


TimeSlot_scheduler = TimeSchedule()

ListOfAdeptC = []
ListOfBegC = []
courseSection = []

course_id = DBConnect.getCourseIdFromDB(2015, 1, courseSection)
course_id = DBConnect.getCleanOneTuple(course_id)
##print("course_id : ")
##print(course_id)


Coursecode = DBConnect.getCourseCodeFromDB(course_id)
print(len(Coursecode))
Coursecode = DBConnect.getTupleInArray(Coursecode)


List_prof = DBConnect.getProfFromDB(Coursecode)
##print("prof", List_prof)
List_prof = DBConnect.getCleanOneTuple(List_prof)

##print("prof", List_prof)
DBConnect.getProfPrefFromDb(List_prof, ListOfAdeptC, ListOfBegC)
combination = DBConnect.Arrange(List_prof, ListOfAdeptC, ListOfBegC, Coursecode)
##for x in range(0, len(Coursecode)):
##    print("Course " + str(x) + " : " + str(Coursecode[x]) )
##    print(combination[x])  


##print(ListOfAdeptC)
##print(ListOfBegC)
#matrix = TimeSlot_scheduler.fill_sched(Coursecode, List_prof)
#print(matrix)
##print(List_prof)
##print(Coursecode)
##print(ClassRoomList[1][0][0])
##print(len(ClassRoomList[1]))
Coursecode = DM.testClassroomType(Coursecode)
#print(Coursecode)
TimeSlot_scheduler.schedule_timetabling(Coursecode, List_prof, tabu_list, ClassRoomList, partition, combination, flowCourse)

#sArray = ['BIOINFO', 'Mr. Anish']
#TimeSlot_scheduler.random_schedule(ClassRoomList, 'Bean')
#sArray2 = ['COMPRO2' , 'S. Alain']
#sArray3 = ['COMPRO', 'Ms. Tessie']
#sArray4 = ['MACLERN', 'Ms.Courmtney']
#sArray5 = ['ADVDISC', 'S. Duke']
#SubMatrix = [sArray, sArray2, sArray3, sArray4, sArray5]
#SubMatrix2 = SubMatrix
#MainMatrix = []
#MainMatrix.append(SubMatrix)
#sArray = ['WEBAPDE', 'S. Stephen']
#sArray2 = ['MOBAPDE' , 'S. Miguel']
#sArray3 = ['TREDONE', 'Ms. Pia']
#SubMatrix = [sArray, sArray2, sArray3]
#MainMatrix.append(SubMatrix)
#MainMatrix.append(SubMatrix2)
#MainMatrix.append(SubMatrix)

print(len(ClassRoomList))


print("Schedule from csv")
input("Enter")

loc = ("AY1415T1-AY1718T2.xls")

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 


ClassroomListFromPast = []
RoomFromPast = []
CourseFromPast = []
ProfFromPast = []
dayFromPast = []
TimeFromPast = []
for i in range(799, 1125): 
    RoomFromPast.append(sheet.cell_value(i, 8))
for i in range(799, 1125): 
    CourseFromPast.append(sheet.cell_value(i, 1))
for i in range(799, 1125): 
    ProfFromPast.append(sheet.cell_value(i, 4))
for i in range(799, 1125): 
    dayFromPast.append(sheet.cell_value(i, 6))
for i in range(799, 1125): 
    TimeFromPast.append(sheet.cell_value(i, 7))


ClassListFromThePast = []
for Room in range(0, len(RoomFromPast)):
    if 'G' in RoomFromPast[Room]:
        flag = True
        Time = TimeFromPast[Room]
        day = dayFromPast[Room]
        course = CourseFromPast[Room]
        prof = ProfFromPast[Room]
        for x in ClassroomListFromPast:
            if x.get_classroom_number() == RoomFromPast[Room]:
                if '0730' in Time or '0800' in Time:
                    Time = 0
                elif '0915' in Time:
                    Time = 1
                elif '1100' in Time:
                    Time = 2
                elif '1245' in Time:
                    Time = 3
                elif '1430' in Time:
                    Time = 4
                elif '1615' in Time:
                    Time = 5
                else:
                    flag = False
                if flag:
                    if 'M' in day:
                        x.get_monday_time()[Time].set_prof(prof)
                        x.get_monday_time()[Time].set_course(course)
                    if 'T' in day:
                        x.get_tuesday_time()[Time].set_prof(prof)
                        x.get_tuesday_time()[Time].set_course(course)
                    if 'W' in day:
                        x.get_wednesday_time()[Time].set_prof(prof)
                        x.get_wednesday_time()[Time].set_course(course)
                    if 'H' in day:
                        x.get_thursday_time()[Time].set_prof(prof)
                        x.get_thursday_time()[Time].set_course(course)
                    if 'F' in day:
                        x.get_friday_time()[Time].set_prof(prof)
                        x.get_friday_time()[Time].set_course(course)
                    flag = False
                break
        if flag:
            classroom = Classroom(RoomFromPast[Room])
            if '0730' in Time or '0800' in Time:
                Time = 0
            elif '0915' in Time:
                Time = 1
            elif '1100' in Time:
                Time = 2
            elif '1245' in Time:
                Time = 3
            elif '1430' in Time:
                Time = 4
            elif '1615' in Time:
                Time = 5
            if 'M' in day:
                classroom.get_monday_time()[Time].set_prof(prof)
                classroom.get_monday_time()[Time].set_course(course)
            if 'T' in day:
                classroom.get_tuesday_time()[Time].set_prof(prof)
                classroom.get_tuesday_time()[Time].set_course(course)
            if 'W' in day:
                classroom.get_wednesday_time()[Time].set_prof(prof)
                classroom.get_wednesday_time()[Time].set_course(course)
            if 'H' in day:
                classroom.get_thursday_time()[Time].set_prof(prof)
                classroom.get_thursday_time()[Time].set_course(course)
            if 'F' in day:
                classroom.get_friday_time()[Time].set_prof(prof)
                classroom.get_friday_time()[Time].set_course(course)
            ClassroomListFromPast.append(classroom)
            
TimeSlot_scheduler = TimeSchedule()
PastScore = TimeSlot_scheduler.score(ClassroomListFromPast)
print(PastScore)


#print(len(TimeSlot_scheduler.course_id))

#TimeSlot_scheduler.random_schedule(ClassRoomList, 'Bean')
#print(ClassRoomList[0].get_monday_time()[0].get_prof())
#print(ClassRoomList[0].get_monday_time()[1].get_prof())
#print(ClassRoomList[0].get_monday_time()[2].get_prof())
#print(ClassRoomList[0].get_monday_time()[3].get_prof())

#print(ClassRoomList[0].get_monday_time()[0].get_course())
#print(ClassRoomList[0].get_monday_time()[1].get_course())

# ------------------------Tips------------------------
# access get monday timeslot index 0 timeslot get prof
# print(C1.get_monday_time()[0].get_prof())
# print(ClassRoomList[0].get_monday_time()[0].get_time())
