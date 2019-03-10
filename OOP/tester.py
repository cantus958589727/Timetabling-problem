from Classroom import*
from TimeSchedule import*
from tabulist import*
from DBconnect import*
from DataManipulator import*
from GUI import *

print("START")
#[ Department, Term, Year ]
UserInput = []
frame = GUI(UserInput)

tabu_list = tabulist()
DBConnect = DBconnect()
DM = DataManipulator()

classified_rooms = DBConnect.getRoomsFromDB()
##print(classified_rooms)
Lecs = DM.InstantiateMultipleClassrooms(classified_rooms[0])
Labs = DM.InstantiateMultipleClassrooms(classified_rooms[1])

print(Lecs)
print(Labs)

labels = []
schedules = []

ClassRoomList = []
ClassRoomList.append(labels)

ClassRoomList[0].extend(Lecs)
ClassRoomList[0].extend(Labs)

ClassRoomList.append(schedules)

ClassRoomList = DM.prepareScheduleHolder(ClassRoomList)

print(ClassRoomList)

TimeSlot_scheduler = TimeSchedule()

ListOfAdeptC = []
ListOfBegC = []

course_id = DBConnect.getCourseIdFromDB(UserInput[2], UserInput[1])
course_id = DBConnect.getCleanOneTuple(course_id)
print("course_id : ")
print(course_id)

Coursecode = DBConnect.getCourseCodeFromDB(course_id)
Coursecode = DBConnect.getCleanOneTuple(Coursecode)

List_prof = DBConnect.getProfFromDB(Coursecode)
List_prof = DBConnect.getCleanOneTuple(List_prof)

DBConnect.getProfPrefFromDb(List_prof, ListOfAdeptC, ListOfBegC)

print(ListOfAdeptC)
print(ListOfBegC)
#matrix = TimeSlot_scheduler.fill_sched(Coursecode, List_prof)
#print(matrix)

print(List_prof)
print(Coursecode)
print(len(ClassRoomList[0]))
print(len(ClassRoomList[1]))

TimeSlot_scheduler.schedule_timetabling(Coursecode, List_prof, tabu_list, ClassRoomList[0])

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
