from TimeSlot import*


class Classroom(object):
    # initiate
    def __init__(self, room_number):
        self.__room_number = room_number
        self.__monday = []
        self.__tuesday = []
        self.__wednesday = []
        self.__thursday = []
        self.__friday = []

        self.set_time_slot()    

    # set time slot
    def set_time_slot(self):
        t = []

        for y in range(0, 5):
            t1 = []
            for x in range(0, 5):
                t1.extend([TimeSlot('7:30')])
                t1.extend([TimeSlot("9:15")])
                t1.extend([TimeSlot("11:00")])
                t1.extend([TimeSlot("12:45")])
                t1.extend([TimeSlot("2:30")])
                t1.extend([TimeSlot("4:15")])
            t.append(t1)
            
        self.__monday = t[0]
        self.__tuesday = t[1]
        self.__wednesday = t[2]
        self.__thursday = t[3]
        self.__friday = t[4]

    # getter
    def get_monday_time(self):
        return self.__monday

    def get_tuesday_time(self):
        return self.__tuesday

    def get_wednesday_time(self):
        return self.__wednesday

    def get_thursday_time(self):
        return self.__thursday

    def get_friday_time(self):
        return self.__friday

    def get_classroom_number(self):
        return self.__room_number

    def available_room_set_prof_mw(self, prof):
        found = False
        for x in range(0, 2):
            if self.__monday[x].get_prof() is None:
                self.__monday[x].set_prof(prof)
                self.__wednesday[x].set_prof(prof)
                found = True
                break
        if not found:
            return None

    def available_room_set_prof_th(self, prof):
        found = False
        for x in range(0, 5):
            if self.__tuesday[x].get_prof() is None:
                self.__tuesday[x].set_prof(prof)
                self.__thursday[x].set_prof(prof)
                found = True
                break
        if not found:
            return None

    def available_room_set_course(self, course):
        found = False
        for x in range(0, 5):
            if self.__monday[x].get_prof() is not None and self.__monday[x].get_course() is None:
                self.__monday[x].set_course(course)
                self.__friday[x].set_course(course)
                found = True
                break
        if not found:
            for x in range(0, 5):
                if self.__tuesday[x].get_course() is None and self.__tuesday[x].get_prof() is not None:
                    self.__tuesday[x].set_course(course)
                    self.__thursday[x].set_course(course)
                    found = True
                    break
        if not found:
            return None
        else:
            return True
