class Marks:
    def __init__(self, student_id, subject, marks, max_marks=100):
        self.student_id = student_id
        self.subject = subject
        self.marks = marks
        self.max_marks = max_marks
        
    def percentage(self):
        return (self.marks / self.max_marks) * 100
    
    
    