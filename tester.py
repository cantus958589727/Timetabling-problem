from Classroom import*
from TimeSchedule import*

C1 = Classroom('G201')

ClassRoomList = []
ClassRoomList.extend([C1])

TimeSlot_scheduler = TimeSchedule()

TimeSlot_scheduler.random_schedule(ClassRoomList, 'Bean')
print(ClassRoomList[0].get_monday_time()[0].get_prof())
print(ClassRoomList[0].get_monday_time()[1].get_prof())
print(ClassRoomList[0].get_monday_time()[2].get_prof())
print(ClassRoomList[0].get_monday_time()[3].get_prof())


# ------------------------Tips------------------------
# access get monday timeslot index 0 timeslot get prof
# print(C1.get_monday_time()[0].get_prof())
# print(ClassRoomList[0].get_monday_time()[0].get_time())
