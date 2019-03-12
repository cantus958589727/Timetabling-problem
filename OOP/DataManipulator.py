from Classroom import*
import random

class DataManipulator(object):

    def __init__(self):
        pass
    
    def InstantiateMultipleClassrooms(self, classroom):
        classrooms = []
        for x in classroom:
            classrooms.append(x)

        return classrooms

    def prepareScheduleHolder(self, classroomlist):
        
        for x in classroomlist[0]:
            mainmatrix = []
            i = 0
            #instantiates monday - saturday array
            while(i < 6):
                i = i + 1
                submatrix = []
                mainmatrix.append(submatrix)

            classroomlist[1].append(mainmatrix)

        print(classroomlist)
        return classroomlist

    def testClassroomType(self, courseOffered):
        classType = ["Lecture", "Laboratory"]
        maincontainer = []
        for x in courseOffered:
            container = []
            container.append(x)
            container.append(random.choice(classType))
            maincontainer.append(container)

        return maincontainer
            
