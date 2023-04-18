class Lesson:
    def __init__(self, date=None, subject=None):
        self.date = date
        self.subject = subject

    def add_attendance(self, student):
        pass


class Student:
    def __init__(self, name, registration):
        self.name = name
        self.registration = registration
