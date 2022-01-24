# Schedule-Maker
This program will assign a classroom and a time slot for each course in the curriculum using python.


# HOW TO USE
run the main.py


# Classrooms
You can arrange classrooms from classroom.cvs.
There are two type of rooms: big and small. Big for the mandatory classes and it doesn't matter for the elective courses assign the available one.
If there is not enough rooms add another room.


# Courses
Courses.csv contains all courses in the curriculum. Each line has 7 items separated by ‘;’, from left to right;
code of the course, name of the course, the year of the semester, credit, C: compulsory or E: Elective, D:
department or S: service, name of the instructor.
CENG104;COMPUTER PROGRAMMING II;1;6;C;D;OGR.GOR. YUSUF EVREN AYKAC

Service.csv contains time slot of service courses. Format of it as follows:
CHEM101;Tuesday;Morning


# Busy Time
Busy.csv contains the busy time slots for the respective instructor. You cannot assign a course to the
specified time slot. That is, for example, CENG104 should not be placed on Tuesday Morning according to
the below file.
OGR.GOR. YUSUF EVREN AYKAC;Tuesday;Morning
