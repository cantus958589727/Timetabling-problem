from LoadDetail import*
class ProfLoad(object):
    def __init__(self, ID,MaxLoad):
        self.ID = ID
        self.name = ""
        self.prefferedtime = []
        self.subjects = []
        
        self.MaxLoad = MaxLoad
        self.M = []
        self.T = []
        self.W = []
        self.H = []
        self.F = []
    def add(self,course,day):
        if(day=='M'):
            self.M.append(course)
        elif(day=='T'):
            self.T.append(course)
        elif(day=='W'):
            self.W.append(course)
        elif(day=='H'):
            self.H.append(course)
        elif(day=='F'):
            self.F.append(course)
    def addTime(self, time):
        if(time == "0730-0900"):
            self.prefferedtime.append(730)
        elif(time == "0915-1045"):
            self.prefferedtime.append(915)
        elif(time == "1100-1230"):
            self.prefferedtime.append(1100)
        elif(time == "1245-0215" or time == "1245-1415"):
            self.prefferedtime.append(1245)
        elif(time == "0230-0400" or time == "1430-1600"):
            self.prefferedtime.append(1430)
        elif(time == "0415-0545" or time == "1615-1745"):
            self.prefferedtime.append(1615)
    def overload(self):
        
        if(len(self.T)+len(self.W)>12):
            return 1
        else:
            return 0
    def consecutive(self):
        currenthours=0
        for x in range (0, len(self.M)-1):
            if (self.M[x+1].get_STime()-self.M[x].get_STime()==145):
                currenthours+=1.5
                if(currenthours>4.5):
                    return 1
            else:
                currenthours=0
        currenthours=0
        for x in range (0, len(self.T)-1):
            if (self.T[x+1].get_STime()-self.T[x].get_STime()==145):
                currenthours+=1.5
                if(currenthours>4.5):
                    return 1
            else:
                currenthours=0
        currenthours=0
        for x in range (0, len(self.W)-1):
            if (self.W[x+1].get_STime()-self.W[x].get_STime()==145):
                currenthours+=1.5
                if(currenthours>4.5):
                    return 1
            else:
                currenthours=0
        currenthours=0
        for x in range (0, len(self.H)-1):
            if (self.H[x+1].get_STime()-self.H[x].get_STime()==145):
                currenthours+=1.5
                if(currenthours>4.5):
                    return 1
            else:
                currenthours=0
        currenthours=0
        for x in range (0, len(self.F)-1):
            if (self.F[x+1].get_STime()-self.F[x].get_STime()==145):
                currenthours+=1.5
                if(currenthours>4.5):
                    return 1
            else:
                currenthours=0
        return 0
        
    def getPrefferedCorrect(self):
        total = 0
        for x in range (0, len(self.M)):
            if(self.M[x].get_STime() in self.prefferedtime):
                total +=1
        for x in range (0, len(self.T)):
            if(self.T[x].get_STime() in self.prefferedtime):
                total +=1
        for x in range (0, len(self.W)):
            if(self.W[x].get_STime() in self.prefferedtime):
                total +=1
        for x in range (0, len(self.H)):
            if(self.H[x].get_STime() in self.prefferedtime):
                total +=1
        for x in range (0, len(self.F)):
            if(self.F[x].get_STime() in self.prefferedtime):
                total +=1
        return total
    def getPrefferedTime(self):
        return self.prefferedtime
    def GetM(self):
        return self.M
    def GetT(self):
        return self.T
    def GetW(self):
        return self.W
    def GetH(self):
        return self.H
    def GetF(self):
        return self.F
    def GetProf(self):
        return self.ID
    def sort(self):
        for x in range (0, len(self.M)):
            for y in range (0, len(self.M)-1):
                if (self.M[y].get_STime()>self.M[y+1].get_STime()):
                    temp = self.M[y]
                    self.M[y] = self.M[y+1]
                    self.M[y+1] = temp
        for x in range (0, len(self.T)):
            for y in range (0, len(self.T)-1):
                if (self.T[y].get_STime()>self.T[y+1].get_STime()):
                    temp = self.T[y]
                    self.T[y] = self.T[y+1]
                    self.T[y+1] = temp
        for x in range (0, len(self.W)):
            for y in range (0, len(self.W)-1):
                if (self.W[y].get_STime()>self.W[y+1].get_STime()):
                    temp = self.W[y]
                    self.W[y] = self.W[y+1]
                    self.W[y+1] = temp
        for x in range (0, len(self.H)):
            for y in range (0, len(self.H)-1):
                if (self.H[y].get_STime()>self.H[y+1].get_STime()):
                    temp = self.H[y]
                    self.H[y] = self.H[y+1]
                    self.H[y+1] = temp
        for x in range (0, len(self.F)):
            for y in range (0, len(self.F)-1):
                if (self.F[y].get_STime()>self.F[y+1].get_STime()):
                    temp = self.F[y]
                    self.F[y] = self.F[y+1]
                    self.F[y+1] = temp
    def checkConflict(self,day):
        conflicts = 0
        if(day=='M'):
             for x in range (0, len(self.M)-1):
                if(self.M[x].get_STime()==self.M[x+1].get_STime()):
                    conflitcs +=1
        if(day=='T'):
             for x in range (0, len(self.T)-1):
                if(self.T[x].get_STime()==self.T[x+1].get_STime()):
                    conflitcs +=1
        if(day=='W'):
             for x in range (0, len(self.W)-1):
                if(self.W[x].get_STime()==self.W[x+1].get_STime()):
                    conflitcs +=1
        if(day=='H'):
             for x in range (0, len(self.H)-1):
                if(self.H[x].get_STime()==self.H[x+1].get_STime()):
                    conflitcs +=1
        if(day=='F'):
             for x in range (0, len(self.F)-1):
                if(self.F[x].get_STime()==self.F[x+1].get_STime()):
                    conflitcs +=1
    def PrintLoad(self,day):
        print("prof: "+str(self.ID))
        if(day=='M'):
            print("monday")
            for x in range (0, len(self.M)):
                print(str(self.M[x].get_STime())+" : "+str(self.M[x].get_Course())+" "+str(self.M[x].get_Room()))
        elif(day == 'T'):   
            print("tuesday")
            for x in range (0, len(self.T)):
                print(str(self.T[x].get_STime())+" : "+str(self.T[x].get_Course())+" "+str(self.T[x].get_Room()))
        elif(day == 'W'):          
            print("wednesday")
            for x in range (0, len(self.W)):
                print(str(self.W[x].get_STime())+" : "+str(self.W[x].get_Course())+" "+str(self.W[x].get_Room()))
        elif(day == 'H'):          
            print("thursday")
            for x in range (0, len(self.H)):
                print(str(self.H[x].get_STime())+" : "+str(self.H[x].get_Course())+" "+str(self.H[x].get_Room()))
        else:       
            print("friday")
            for x in range (0, len(self.F)):
                print(str(self.F[x].get_STime())+" : "+str(self.F[x].get_Course())+" "+str(self.F[x].get_Room()))
         