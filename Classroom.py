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

    # set time slot
    def set_time_slot(self, monday, tuesday, wednesday, thursday, friday):
        self.__monday = monday
        self.__tuesday = tuesday
        self.__wednesday = wednesday
        self.__thursday = thursday
        self.__friday = friday

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
