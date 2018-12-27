from Classroom import*
from TimeSchedule import*
from tabulist import*


tabu_list = tabulist()

C1 = Classroom('G201')

ClassRoomList = []
ClassRoomList.extend([C1])

TimeSlot_scheduler = TimeSchedule()

List_prof = ['Anish', 'Alain', 'Tessie', 'Courtney', 'Duke', 'Bean', 'kaka']
Coursecode = ['1111', '2222', '3333', '4444', '5555', '6666', '7777']
#matrix = TimeSlot_scheduler.fill_sched(Coursecode, List_prof)
#print(matrix)


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
