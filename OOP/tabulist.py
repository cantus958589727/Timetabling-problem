from DataManipulator import*

class tabulist:
    # shoart = short-term tabulist
    # long = long-term tabulist
    def __init__(self):
        self.short = []
        self.long = []
        self.shortLen = 5
        self.DM = DataManipulator()
        
    def emptyList(self):
        return self.short == []
        return self.long == []

    def checkListIsFull(self):
        if self.sizeShort() > self.shortLen:
            self.dequeueShort()

    # -------long term function-------
    def checkLong(self, schedule):
        for x in range(0, len(self.long)):
            if self.long[x] == schedule:
                return False
        return True

    def enqueueLong(self, schedule):
        self.long.insert(0, schedule)
        self.checkListIsFull()

    def dequeueLong(self):
        return self.long.pop()

    # --------short term function-------
    def checkshort(self, schedule):
##            tempList = []
##            for y in range(0, len(schedule)):
##                tempList.append(schedule[y])
##
##            for x in tempList:
##                print(x.print_all())
##            return True
        
##        for ClassList in self.short:
##            compareList = []
##            for classroom in range(0, len(ClassList)):
##                compareList.append(ClassList[classroom])
##            for x in compareList:
##                print(x.print_all())
##            input()
        if not self.sizeShort():
            return True
##        print("test")
##        for ClassList in self.short:
##            ClassList[0].print_all()
    
##        schedule[0].print_all()
##        self.short[0][0].print_all()
        if (self.DM.compareTwoSchedules(schedule, self.short[0])):
            print("IN")
            return True
        
##        for ClassList in self.short:
##            for classroom in range(0, len(ClassList)):
##                for x in range(0, 6):
##                    if ClassList[classroom].get_tuesday_time()[x].get_course() != schedule[classroom].get_tuesday_time()[x].get_course():
##                        return True
##                    if ClassList[classroom].get_wednesday_time()[x].get_course() != schedule[classroom].get_wednesday_time()[x].get_course():
##                        return True
        return False

    def enqueueShort(self, schedule):
        self.short.insert(0, schedule)

    def dequeueShort(self):
        return self.short.pop()

    def sizeLong(self):
        return len(self.long)
    
    def sizeShort(self):
        return len(self.short)

    # -------------------------Check tabulist element-------------------

    def print_all(self):
        print("Short Term")
        for x in self.short:
            for y in x:
                print(y.print_all())
        print("Long Term")
        for x in self.long:
            for y in x:
                print(y.print_all())

    def print_short(self):
        print("Short Term")
        for x in self.short:
            for y in x:
                print(y.print_all())
            input()
