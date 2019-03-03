from Classroom import*

class DataManipulator(object):

    def __init__(self):
        pass
    
    def InstantiateMultipleClassrooms(self, classroom):
        classrooms = []
        for x in classroom:
            classrooms.append(x)

        return classrooms
