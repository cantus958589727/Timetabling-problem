from TimeSlot import*


class Classroom(object):
    # initiate
    def __init__(self, room_number):
        self.__room_number = room_number
        self.__monday = None
        self.__tuesday = None
        self.__wednesday = None
        self.__thursday = None
        self.__friday = None

        self.set_time_slot()    

    # set time slot
    def set_time_slot(self):
        day = 1
        T =[[for x in range(0,5)] for x in range(0,6)]

        for x in range(0,5):
            T[x].extend(TimeSlot("7:30"))
            T[x].extend(TimeSlot("9:15"))
            T[x].extend(TimeSlot("11:00"))
            T[x].extend(TimeSlot("12:45"))
            T[x].extend(TimeSlot("2:30"))
            T[x].extend(TimeSlot("4:15"))
            
        self.__monday = T[0]
        self.__tuesday = T[1]
        self.__wednesday = T[2]
        self.__thursday = T[3]
        self.__friday = T[4]

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
