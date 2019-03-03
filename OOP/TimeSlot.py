# Time slot class


class TimeSlot(object):
    # create time slot
    def __init__(self, timeslot):
        self.__prof = None
        self.__course = None
        self.__time = timeslot

    # setter
    def set_prof(self, prof):
        self.__prof = prof

    def set_course(self, course):
        self.__course = course

    # getter
    def get_prof(self):
        return self.__prof

    def get_time(self):
        return self.__time

    def get_course(self):
        return self.__course
