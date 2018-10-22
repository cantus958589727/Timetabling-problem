import time

class ExtraSchedule(Schedule):

    def __init__(self, timeSched, courseName, profName, dates):
        Schedule.__init__(self, timeSched, courseName, profName
        self.dates = dates

    def getDates(self):
        return self.dates
                        
