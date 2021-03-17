"""
CS 2420
Gino Mangini
main.py
"""

from course import Course
from courselist import CourseList

def main():

    """main implementation, builds linked list from data"""

    cc_list = [] # list of Courses
    course_list = CourseList()

    with open("data.txt", "r") as file:

        for line in file:
            var = line.split(",")
            # creating a list full of Course data types
            cc_list.append(Course(int(var[0]), var[1], int(var[2]), float(var[3])))

    for i in range(len(cc_list)):
        course_list.insert(cc_list[i])

    course_list.__str__()

if __name__ == "__main__":
    main()
