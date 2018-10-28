class Scheduler(object):

    def __int__(self):
        print("GOOD")

    def schedule(self):

        # test sample
        templist =[]
        templist.append([['Compro1'], ['prof1']])
        templist.append([['Compro2'], ['prof1']])
        templist.append([['Compro3'], ['prof3']])
        templist.append([['Compro4'], ['prof4']])
        templist.append([['Compro5'], ['prof5']])
        templist.append([['Compro6'], ['prof6']])

        templist2 = []
        templist2.append([['Compro1'], ['prof1']])
        templist2.append([['Compro2'], ['prof2']])
        templist2.append([['Compro3'], ['prof3']])
        templist2.append([['Compro4'], ['prof4']])
        templist2.append([['Compro5'], ['prof5']])
        templist2.append([['Compro6'], ['prof6']])

        # global variable
        countert = 1
        counterw = 1
        # here we put what day have violated our contraints
        # 0 = none, 1 = prof, 2 = course, 3 for both
        daycounter = [ 0, 0, 0, 0 ]

        # temp name
        proflist = {}
        for x in range( 0, len(templist) ):
            proflist[templist[x][1][0]] = 0
            proflist[templist2[x][1][0]] = 0

        # check if tuesday = thursday
        # countert = 2
        # same goes to wednesday and friday

        # for tuesday and thursday
        for y in range( 0, countert ):
            proflisttime = {}
            for x in range(0, len(templist)):
                proflisttime[templist[x][1][0]] = 0
            for x in range(0, len(templist)):
                # check the unit if its 5 or more
                prof = templist[x][1][0]
                unit = proflist[prof]
                unit = unit + 3
                proflist[prof] = unit
                # add time to prof
                time = 1.5
                time += proflisttime[prof]
                proflisttime[prof] = unit

        # in the future check if there are contraints being violated so that we could skip the wednesday and friday checking

        # for wednesday and friday
        for y in range( 0, countert ):
            proflisttime = {}
            for x in range(0, len(templist2)):
                proflisttime[templist2[x][1][0]] = 0
            for x in range(0, 6):
                # check the unit if its 5 or more
                prof = templist2[x][1][0]
                unit = 3
                unit += proflist[prof]
                proflist[prof] = unit
                print(proflist[prof])
                # add time to prof
                time = 1.5
                time += proflisttime[prof]
                proflisttime[prof] = time

        print(proflist[templist[0][1][0]])
        print(proflist[templist[0][1][0]])
        print(proflist[templist[0][1][0]])
