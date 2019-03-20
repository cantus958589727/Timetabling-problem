from Classroom import*
import random

class DataManipulator(object):

    def __init__(self):
        pass

# Assuming these functions will retrieve an object type of the classroom/schedule
    def get_prof_total_day(self, day, my_dict):

        for timeslot in day:
            prof = timeslot.get_prof() 
            if prof is None:
               pass
            elif prof in my_dict:
                #set default units to 2
              my_dict[prof] += 2
            else:
              my_dict[prof] = 2
  
    def get_prof_total_classroom(self, classroom, dictionary):
        if dictionary is None:
            dict_profCount = dict()   
        else:
            dict_profCount = dictionary
            
        self.get_prof_total_day(classroom.get_monday_time(), dict_profCount)
        self.get_prof_total_day(classroom.get_tuesday_time(), dict_profCount)
        self.get_prof_total_day(classroom.get_wednesday_time(), dict_profCount)
        self.get_prof_total_day(classroom.get_thursday_time(), dict_profCount)
        self.get_prof_total_day(classroom.get_friday_time(), dict_profCount)
##        self.get_prof_total_day(classroom.get_saturday_time(), dict_profCount)
                                
        return dict_profCount
                                                 
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
            
