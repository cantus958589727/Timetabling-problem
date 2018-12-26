class tabulist:
    # shoart = short-term tabulist
    # long = long-term tabulist
    def __init__(self):
        self.short = []
        self.long = []
        self.shortLen = 5

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
        for x in range(0, len(self.short)):
            if self.short[x] == schedule:
                return False
        return True

    def enqueueShort(self, schedule):
        self.short.insert(0, schedule)

    def dequeueShort(self):
        return self.short.pop()

    def sizeShort(self):
        return len(self.short)

    # -------------------------Check tabulist element-------------------

    def print_all(self):
        print("Short Term")
        for x in self.short:
            print(x)
        print("Long Term")
        for x in self.long:
            print(x)
