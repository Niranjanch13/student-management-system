class Teacher:
    def __init__(self, teacher_id, name, subject, email):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject
        self.email = email  
        
    def display_teacher(self):
        print("Teacher ID:", self.teacher_id)
        print("Name:", self.name)
        print("Subject:", self.subject)
        print("Email:", self.email)