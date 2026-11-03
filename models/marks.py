class Marks:
    def __init__(self, student_id, subject, marks, max_marks=100):


        if not isinstance(marks, (int, float)) or isinstance(marks, bool):
            raise ValueError("Marks must be a number.")

        if not isinstance(max_marks, (int, float)) or isinstance(max_marks, bool):
            raise ValueError("Maximum marks must be a number.")

        if max_marks <= 0:
            raise ValueError("Maximum marks must be greater than zero.")

        if marks < 0 or marks > max_marks:
            raise ValueError("Marks must be between 0 and maximum marks.")

        self.student_id = student_id
        self.subject = subject
        self.marks = marks
        self.max_marks = max_marks

    def percentage(self):
        return (self.marks / self.max_marks) * 100

