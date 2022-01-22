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
