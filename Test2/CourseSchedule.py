import time

class CourseSchedule(Schedule):

    def __init(self, timeSched, courseName, profName, days):
        Schedule.__init__(self, timeSched, courseName, profName)
        self.days = days

    def getDays(self):
        return days
