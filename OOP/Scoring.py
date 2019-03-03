# Scoring

class Scoring(object):
    # def __int__(self):
    #   self.
    #---------------------------------Need to change something here, not yet done-------------------------------------||
    def gapYScoring(sched, score):
        for x in range(0, len(sched)):
            tempScore = 1
            prevCheck = False
            currCheck = False
            perfect = True
            multiplier = 1
            for y in range(0, len(sched[x])):
                ##            print(y)
                if (y == 0):
                    if (not (sched[x][y][0] == "")):
                        prevCheck = True
                else:
                    if (not (sched[x][y][0] == "")):
                        currCheck = True
                    else:
                        currCheck = False

                    if (not (currCheck) and prevCheck and tempScore == 1):
                        ##                    print("T, F")
                        tempScore -= multiplier
                    elif (not (prevCheck) and currCheck and tempScore <= 0):
                        ##                    print("F, T")
                        score += tempScore
                        multiplier += 1
                        perfect = False
                    elif (not (currCheck) and not (prevCheck) and tempScore <= 0):
                        ##                    print("F, F")
                        tempScore -= multiplier
                    elif (currCheck and prevCheck):
                        ##                    print("T, T")
                        if (tempScore <= 0):
                            tempScore = 1

                    prevCheck = currCheck

            if (perfect):
                score += 1

        ##        print("current score: ", score)

        return score

    def checkNhoursNunits(self, MainMatrix):
        # global variable
        countert = 1
        counterw = 1
        # here we put what day have violated our contraints
        # 0 = none, 1 = prof, 2 = course, 3 for both
        daycounter = [0, 0, 0, 0]

        # temp name
        proflist = {}

        for y in range(0, len(MainMatrix)):
            for x in range(0, len(MainMatrix[y])):
                proflist[MainMatrix[y][x][1]] = 0

        # check if tuesday = thursday
        # countert = 2
        # same goes to wednesday and friday

        # for tuesday and thursday
        for y in range(0, countert):
            proflisttime = {}
            for x in range(0, len(MainMatrix[y])):
                proflisttime[MainMatrix[y][x][1]] = 0
            for x in range(0, len(MainMatrix[y])):
                # check the unit if its 5 or more
                prof = MainMatrix[y][x][1]
                unit = proflist[prof]
                unit = unit + 3
                proflist[prof] = unit
                # add time to prof
                time = 1.5
                time += proflisttime[prof]
                proflisttime[prof] = unit

        # in the future check if there are contraints being violated so that we could skip the wednesday and friday checking

        # for wednesday and friday
        for y in range(0, countert):
            proflisttime = {}
            for x in range(0, len(MainMatrix[y + 1])):
                proflisttime[MainMatrix[y + 1][x][1]] = 0
            for x in range(0, len(MainMatrix[y + 1])):
                # check the unit if its 5 or more
                prof = MainMatrix[y + 1][x][1]
                unit = 3
                unit += proflist[prof]
                proflist[prof] = unit
                print(proflist[prof])
                # add time to prof
                time = 1.5
                time += proflisttime[prof]
                proflisttime[prof] = time

        print(proflist[MainMatrix[0][1][1]])
        print(proflist[MainMatrix[0][1][1]])
        print(proflist[MainMatrix[0][1][1]])

