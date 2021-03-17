"""
Course List Linked List
"""

from course import Course
from recursioncounter import RecursionCounter

class CourseList:
    """linked list implementation"""
    def __init__(self):
        self.head = None

    def insert(self, course):
        """inserts new node at specified Course"""
        if isinstance(course, Course) is False:
            raise ValueError("Must be Course")

        self.head = self.insert_helper(self.head, course)

    def insert_helper(self, cursor, course):
        """recursive insertion on Course number"""
        RecursionCounter()
        if cursor is None: #BC1 points to null
            return course
        if cursor.number() < course.number(): #BC2 cursor value is less than course value
            cursor.next = self.insert_helper(cursor.next, course)
            return cursor # reset head to beginning of linked list
        course.next = cursor
        return course

    def remove(self, number):
        """removes Course from list by course number"""
        if isinstance(number, int) is False:
            raise ValueError("number must be int")

        self.head = self.remove_helper(self.head, number)

    def remove_helper(self, cursor, number):
        """recursive part of the remove function"""
        RecursionCounter()
        if cursor is None:
            return None
        if cursor.number() == number:
            return cursor.next
        cursor.next = self.remove_helper(cursor.next, number)
        return cursor

    def remove_all(self, number):
        """remove all instances of number"""
        self.head = self.remove_all_helper(self.head, number)

    def remove_all_helper(self, cursor, number):
        """recursive removal of all courses equal to number"""
        RecursionCounter()
        if cursor is None:
            return None
        cursor.next = self.remove_all_helper(cursor.next, number)
        if cursor.number() == number:
            return cursor.next
        return cursor

    def find(self, number):
        """finds a course by number"""
        if isinstance(number, int) is False:
            raise ValueError("number must be int")

        return self.find_helper(self.head, number)

    def find_helper(self, cursor, number):
        """recursively finds the course number and returns course"""
        RecursionCounter()
        if cursor.next is None:
            return -1
        if cursor.number() == number:
            return cursor
        else:
            return self.find_helper(cursor.next, number)

    def size(self):
        """returns the number of Courses in the list"""
        counter = 0
        if self.head is None:
            return counter
        else:
            return self.size_helper(self.head, counter)

    def size_helper(self, cursor, counter):
        """recursive counter of number of courses in linked list"""
        RecursionCounter()
        counter += 1
        if cursor.next is not None:
            return self.size_helper(cursor.next, counter)
        else:
            return counter

    def calculate_gpa(self):
        """calculates the GPA for courses -- grade points / total credits"""
        if self.head is None:
            return 0
        
        total_credits = self.get_credits(self.head)
        total_grade = self.get_grade_points(self.head)
        return (total_grade / total_credits)

    def get_grade_points(self, cursor):
        """returns the total grade points for each class by credit hour and gpa"""
        RecursionCounter()
        if cursor is None:
            return 0.0
        else:
            return (cursor.grade() * cursor.credit_hr()) + self.get_grade_points(cursor.next)

    def get_credits(self, cursor):
        """returns total number of credits for each Course"""
        RecursionCounter()
        if cursor is None:
            return 0.0
        return cursor.credit_hr() + self.get_credits(cursor.next)

    def is_sorted(self):
        """returns True is course list is sorted and False if not"""
        if self.head is None:
            return True
        return self.is_sorted_helper(self.head)

    def is_sorted_helper(self, cursor):
        """recursive sorter, returns True or False"""
        RecursionCounter()
        if cursor.next is None:
            return True
        elif cursor.number() > cursor.next.number():
            return False
        else:
            return self.is_sorted_helper(cursor.next)

    def __str__(self):
        """returns string version of all courses in list"""
        print("Current List: (" + str(self.size()) + ")")
        return self.__str__helper(self.head)

    def __str__helper(self, cursor):
        """recursive printing of each course"""
        print(cursor)
        if cursor.next is None:
            print("\nCumulative GPA:", round(self.calculate_gpa(), 3))
            print("\n")
        else:
            return self.__str__helper(cursor.next)

    def __iter__(self):
        """returns self & creates method"""
        self.cursor = self.head
        return self

    def __next__(self):
        """iterator stepping through values"""
        if self.cursor is None:
            raise StopIteration
        else:
            cursor = self.head
            self.cursor = self.cursor.next
            return cursor
