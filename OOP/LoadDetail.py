class LoadDetail(object):
    def __init__(self, Course, STime,Room):
        self.Course= Course
        if(STime=="7:30"):
            self.STime = 730
        elif(STime == "9:15"):
            self.STime = 915
        elif(STime == "11:00"):
            self.STime = 1100
        elif(STime == "12:45"):
            self.STime = 1245
        elif(STime == "2:30"):
            self.STime = 1430
        elif(STime == "4:15"):
            self.STime = 1615
        self.Room = Room
      #  self.ETime = ETime
    def get_Course(self):
        return self.Course
    def get_STime(self):
        return self.STime
    def get_Room(self):
        return self.Room
#    def get_ETime(self):
#        return self.ETime