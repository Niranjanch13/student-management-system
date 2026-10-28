#student.py

class Student:
    def __init__(self, student_id, name, roll_number, email):
        self.student_id = student_id
        self.name = name
        self.roll_number = roll_number
        self.email = email

    def display_student(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Email:", self.email)
