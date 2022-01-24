import classes
from tkinter import *

courseList = []
with open("courses.csv", "r") as filestream:
    for line in filestream:
        current_line = line.split(";")
        courseList.append(classes.Courses(current_line[0], current_line[1], current_line[2],
                                          current_line[3], current_line[4], current_line[5],
                                          current_line[6].rstrip("\n")))

curriculum = []
curriculum.append(classes.Days('Monday'))
curriculum.append(classes.Days('Tuesday'))
curriculum.append(classes.Days('Wednesday'))
curriculum.append(classes.Days('Thursday'))
curriculum.append(classes.Days('Friday'))


busyList = []
with open("busy.csv", "r") as f:
    for line in f.readlines():
        busyList.append(line.split(";"))


serviceCourses = []
with open("service.csv", "r") as f:
    for line in f.readlines():
        serviceCourses.append(line.split(";"))

classRooms = []
with open("classroom.csv", "r") as filestream:
    for line in filestream:
        current_line = line.split(";")
        classRooms.append(classes.Classes(current_line[0], current_line[1]))

def decide_days(day):
    if day == 'Monday':
        return 0

    if day == 'Tuesday':
        return 1

    if day == 'Wednesday':
        return 2

    if day == 'Thursday':
        return 3

    if day == 'Friday':
        return 4
    else:
        return -1

    
def get_collision_morning(day, course):
    flag = False

    if day.morning.big1 == True and day.morning.bigClassroom1Course.get_year() == course.get_year():
        flag = True

    if day.morning.big2 == True and day.morning.bigClassroom2Course.get_year() == course.get_year():
        flag = True

    if day.morning.small1 == True and day.morning.smallClassroom1Course.get_year() == course.get_year():
        flag = True

    if day.morning.small2 == True and day.morning.smallClassroom2Course.get_year() == course.get_year():
        flag = True

    return flag


def get_collision_afternoon(day, course):
    flag = False

    if day.afternoon.big1 == True and day.afternoon.bigClassroom1Course.get_year() == course.get_year():
        flag = True

    if day.afternoon.big2 == True and day.afternoon.bigClassroom2Course.get_year() == course.get_year():
        flag = True

    if day.afternoon.small1 == True and day.afternoon.smallClassroom1Course.get_year() == course.get_year():
        flag = True

    if day.afternoon.small2 == True and day.afternoon.smallClassroom2Course.get_year() == course.get_year():
        flag = True

    return flag


def is_busy_morning(course, index, busy):
    flag = False
    for i in range(len(busy)):
        busyTimeSlotDayIndex = decide_days(busy[i][1])
        time = busy[i][2].rstrip("\n")
        if course.get_instructor() == busy[i][0] and index == busyTimeSlotDayIndex and time == "Morning":
            flag = True
            break

    return flag


def is_busy_afternoon(course, index, busy):
    flag = False

    for i in range(len(busy)):
        busyTimeSlotDayIndex = decide_days(busy[i][1])
        time = busy[i][2].rstrip("\n")
        if course.get_instructor() == busy[i][0] and index == busyTimeSlotDayIndex and time == "Afternoon":
            flag = True
            break

    return flag


def assign_service_courses():
    for i in range(len(serviceCourses)):
        index = -1

        for j in range(len(courseList)):
            if courseList[j].courseCode == serviceCourses[i][0]:
                index = j
                break

        day = decide_days(serviceCourses[i][1])

        e_or_c = bool

        if courseList[index].get_c_or_e() == 'E':
            e_or_c = True
        else:
            e_or_c = False

        time = serviceCourses[i][2].rstrip("\n")
        if time == 'Afternoon':
            if e_or_c:
                if curriculum[day].afternoon.small1 == False:
                    curriculum[day].afternoon.small1 = True
                    courseList[index].isAssigned = True
                    curriculum[day].afternoon.smallClassroom1Course = courseList[index]

                elif curriculum[day].afternoon.small2 == False:
                    curriculum[day].afternoon.small2 = True
                    courseList[index].isAssigned = True
                    curriculum[day].afternoon.smallClassroom2Course = courseList[index]

                elif curriculum[day].afternoon.big1 == False:
                    curriculum[day].afternoon.big1 = True
                    courseList[index].isAssigned = True
                    curriculum[day].afternoon.bigClassroom1Course = courseList[index]

                elif curriculum[day].afternoon.big2 == False:
                    curriculum[day].afternoon.big2 = True
                    courseList[index].isAssigned = True
                    curriculum[day].afternoon.bigClassroom2Course = courseList[index]
            else:
                if curriculum[day].afternoon.big1 == False:
                    curriculum[day].afternoon.big1 = True
                    courseList[index].isAssigned = True
                    curriculum[day].afternoon.bigClassroom1Course = courseList[index]

                elif curriculum[day].afternoon.big2 == False:
                    curriculum[day].afternoon.big2 = True
                    courseList[index].isAssigned = True
                    curriculum[day].afternoon.bigClassroom2Course = courseList[index]

        elif time == 'Morning':
            if e_or_c:
                if curriculum[day].morning.small1 == False:
                    curriculum[day].morning.small1 = True
                    courseList[index].isAssigned = True
                    curriculum[day].morning.smallClassroom1Course = courseList[index]

                elif curriculum[day].morning.small2 == False:
                    curriculum[day].morning.small2 = True
                    courseList[index].isAssigned = True
                    curriculum[day].morning.smallClassroom2Course = courseList[index]

                elif curriculum[day].morning.big1 == False:
                    curriculum[day].morning.big1 = True
                    courseList[index].isAssigned = True
                    curriculum[day].morning.bigClassroom1Course = courseList[index]

                elif curriculum[day].morning.big2 == False:
                    curriculum[day].morning.big2 = True
                    courseList[index].isAssigned = True
                    curriculum[day].morning.bigClassroom2Course = courseList[index]
            else:
                if curriculum[day].morning.big1 == False:
                    curriculum[day].morning.big1 = True
                    courseList[index].isAssigned = True
                    curriculum[day].morning.bigClassroom1Course = courseList[index]

                elif curriculum[day].morning.big2 == False:
                    curriculum[day].morning.big2 = True
                    courseList[index].isAssigned = True
                    curriculum[day].morning.bigClassroom2Course = courseList[index]

                    
def assign_department_courses():
    for i in range(len(courseList)):
        if courseList[i].isAssigned == True:
            continue

        e_or_c = bool
        if courseList[i].get_c_or_e() == 'E':
            e_or_c = True
        else:
            e_or_c = False

        for index in range(5):
            if courseList[i].isAssigned == True:
                continue

            flag_morning = get_collision_morning(curriculum[index], courseList[i])
            flag_afternoon = get_collision_afternoon(curriculum[index], courseList[i])

            get_busy_morning = bool
            get_busy_afternoon = bool

            get_busy_morning = is_busy_morning(courseList[i], index, busyList)
            get_busy_afternoon = is_busy_afternoon(courseList[i], index, busyList)

            if flag_morning == True and flag_afternoon == True:
                continue

            if get_busy_morning == True and get_busy_afternoon == True:
                continue

            if flag_morning == False and get_busy_morning == False:
                if e_or_c:
                    if curriculum[index].morning.small1 == False:
                        curriculum[index].morning.small1 = True
                        courseList[i].isAssigned = True
                        curriculum[index].morning.smallClassroom1Course = courseList[i]

                    elif curriculum[index].morning.small2 == False:
                        curriculum[index].morning.small2 = True
                        courseList[i].isAssigned = True
                        curriculum[index].morning.smallClassroom2Course = courseList[i]

                    elif curriculum[index].morning.big1 == False:
                        curriculum[index].morning.big1 = True
                        courseList[i].isAssigned = True
                        curriculum[index].morning.bigClassroom1Course = courseList[i]

                    elif curriculum[index].morning.big2 == False:
                        curriculum[index].morning.big2 = True
                        courseList[i].isAssigned = True
                        curriculum[index].morning.bigClassroom2Course = courseList[i]
                else:
                    if curriculum[index].morning.big1 == False:
                        curriculum[index].morning.big1 = True
                        courseList[i].isAssigned = True
                        curriculum[index].morning.bigClassroom1Course = courseList[i]

                    elif curriculum[index].morning.big2 == False:
                        curriculum[index].morning.big2 = True
                        courseList[i].isAssigned = True
                        curriculum[index].morning.bigClassroom2Course = courseList[i]

            elif flag_afternoon == False and get_busy_afternoon == False:
                if e_or_c:
                    if curriculum[index].afternoon.small1 == False:
                        curriculum[index].afternoon.small1 = True
                        courseList[i].isAssigned = True
                        curriculum[index].afternoon.smallClassroom1Course = courseList[i]

                    elif curriculum[index].afternoon.small2 == False:
                        curriculum[index].afternoon.small2= True
                        courseList[i].isAssigned = True
                        curriculum[index].afternoon.smallClassroom2Course = courseList[i]

                    elif curriculum[index].afternoon.big1 == False:
                        curriculum[index].afternoon.big1 = True
                        courseList[i].isAssigned = True
                        curriculum[index].afternoon.bigClassroom1Course = courseList[i]

                    elif curriculum[index].afternoon.big2 == False:
                        curriculum[index].afternoon.big2 = True
                        courseList[i].isAssigned = True
                        curriculum[index].afternoon.bigClassroom2Course = courseList[i]
                else:
                    if curriculum[index].afternoon.big1 == False:
                        curriculum[index].afternoon.big1 = True
                        courseList[i].isAssigned = True
                        curriculum[index].afternoon.bigClassroom1Course = courseList[i]

                    elif curriculum[index].afternoon.big2 == False:
                        curriculum[index].afternoon.big2 = True
                        courseList[i].isAssigned = True
                        curriculum[index].afternoon.bigClassroom2Course = courseList[i]
                        
assign_service_courses()
assign_department_courses()

unAssigned = []
for i in range(len(courseList)):
    if courseList[i].isAssigned == False:
        unAssigned.append(courseList[i].courseName)

for i in range(len(classRooms)):
    crName = classRooms[i].cr_name
    crNumber = classRooms[i].cr_num
    print(crName.rstrip("\n") + " " + crNumber.rstrip("\n"))

if len(unAssigned) == 0:
    for i in range(len(curriculum)):
        if curriculum[i].morning.big1 == True:
            print(curriculum[i].dayName + " Morning bigClassroom1 " + curriculum[i].morning.bigClassroom1Course.get_cr_id())

        if curriculum[i].morning.big2 == True:
            print(curriculum[i].dayName + " Morning bigClassroom2 " + curriculum[i].morning.bigClassroom2Course.get_cr_id())

        if curriculum[i].morning.small1 == True:
            print(curriculum[i].dayName + " Morning smallClassroom1 " + curriculum[i].morning.smallClassroom1Course.get_cr_id())

        if curriculum[i].morning.small2 == True:
            print(curriculum[i].dayName + " Morning smallClassroom2 " + curriculum[i].morning.smallClassroom2Course.get_cr_id())

        if curriculum[i].afternoon.big1 == True:
            print(curriculum[i].dayName + " Afternoon bigClassroom1 " + curriculum[i].afternoon.bigClassroom1Course.get_cr_id())

        if curriculum[i].afternoon.big2 == True:
            print(curriculum[i].dayName + " Afternoon bigClassroom2 " + curriculum[i].afternoon.bigClassroom2Course.get_cr_id())

        if curriculum[i].afternoon.small1 == True:
            print(curriculum[i].dayName + " Afternoon smallClassroom1 " + curriculum[i].afternoon.smallClassroom1Course.get_cr_id())

        if curriculum[i].afternoon.small2 == True:
            print(curriculum[i].dayName + " Afternoon smallClassroom2 " + curriculum[i].afternoon.smallClassroom2Course.get_cr_id())
    else:
        print("There can't be a schedule under these conditions. Adding more classrooms can solve the problem.")
        print("\nCourses that remain unassigned\n--------------------------")
        for i in range(len(unAssigned)):
            print(unAssigned[i])
