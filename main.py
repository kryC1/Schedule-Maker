import classes
from tkinter import *

courseList = []
with open("courses.csv", "r") as filestream:
    for line in filestream:
        current_line = line.split(";")
        courseList.append(classes.Courses(current_line[0], current_line[1], current_line[2],
                                          current_line[3], current_line[4], current_line[5], current_line[6].rstrip("\n")))

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
