from Classroom import*
from TimeSlot import*


T1 = TimeSlot("7:30")
T1.set_prof('dfhgjklhgfxhjklhgf')
T2 = TimeSlot("8:00")

monday = [T1, T2]

C1 = Classroom('G201')
C1.set_time_slot(monday, None, None, None, None)

# access get monday timeslot index 0 timeslot get prof
# print(C1.get_monday_time()[0].get_prof())
