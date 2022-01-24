from tkinter import *

class Classes:
  def __init__(self, cr_num, cr_name):
    self.cr_num = cr_num
    self.cr_name = cr_name
    
class Courses:
    def __init__(self, cr_id, cr_name, year, credit, c_or_e, d_or_s, instructor):
        self.courseCode = cr_id
        self.courseName = cr_name
        self.semesterYear = year
        self.credit = credit
        self.c_or_e = c_or_e
        self.d_or_s = d_or_s
        self.instructor = instructor
        self.isAssigned = False

    def get_c_or_e(self):
        return self.c_or_e

    def get_cr_id(self):
        return self.courseCode

    def get_year(self):
        return self.semesterYear

    def get_instructor(self):
        return self.instructor


class Instructor:
    def __init__(self, name):
        self.name = name


class TimeOfDay:
    def __init__(self, big1, big2, small1, small2):
        self.bigClassroom1Course = Courses
        self.bigClassroom2Course = Courses
        self.smallClassroom1Course = Courses
        self.smallClassroom2Course = Courses
        self.big1 = big1
        self.big2 = big2
        self.small1 = small1
        self.small2 = small2


class Days:
    def __init__(self, day):
        self.dayName = day
        self.morning = TimeOfDay(False, False, False, False)
        self.afternoon = TimeOfDay(False, False, False, False)
        
