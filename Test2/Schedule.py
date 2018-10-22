import time

class Schedule:
    
    # Constructor
    def __init__(self, timeSched, courseName, profName):
        #Array contains timeslots/values = 7:30, 9:00, etc.
        self.timeSched = timeSched
        self.courseName = courseName
        self.profName = profName

    #methods / functions
    def getCourseName(self):
        return self.courseName

    def getProfName(self):
        return self.profName

    def getTimeSched(self):
        return self.timeSched


        
