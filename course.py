"""
creates course instance with the course number, course name,
credit hours, and grade point average. Validates to ensure that data is
correct.
"""

class Course:
    """creates a Course object with number, name, credit hr, and grade"""
    def __init__(self, number=0000, name="", credit_hr=0, grade=0.0):
        """instantiate Course object pointing to None"""
        self._number = number
        self._name = name
        self._credit_hr = credit_hr
        self._grade = grade
        self.next = None

        if (not isinstance(number, int)) or number < 0:
            raise ValueError("number must be int & pos")

        if not isinstance(name, str):
            raise ValueError("name must be str")

        if (isinstance(credit_hr, str)) or credit_hr < 0:
            raise ValueError("The entry must be float type and positive")

        if not isinstance(grade, float) or grade < 0.0 or grade > 4.0:
            raise ValueError("grade must be float & between 0.0-4.0")

    def number(self):
        """returns number"""
        return self._number

    def name(self):
        """returns name"""
        return self._name

    def credit_hr(self):
        """returns credit hour"""
        return self._credit_hr

    def grade(self):
        """returns grade"""
        return self._grade

    def __str__(self):
        """returns string of Course"""
        return "cs" + str(self._number) + " " + str(self._name) \
            + " Grade: " + str(self._grade) + " Credit Hours: " \
                + str(float(self._credit_hr))
