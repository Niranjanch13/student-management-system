#validation.py
import re




def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_not_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please enter a valid value.")
        
        
def get_email_input(prompt):
    while True:
        email = input(prompt).strip()
        if not email:
            print("Email cannot be empty")
            continue
        
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
            
        if re.match(pattern, email):    
            return email
        
        print("Invalid email format. Please enter a valid email address.")
        
        
def get_marks_input(prompt):
    while True:
        try:
            marks = int(input(prompt))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100. Please enter a valid value.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
def get_positive_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Value must be a positive integer. Please enter a valid value.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
def get_valid_marks(prompt,max_marks):
    while True:
        try:
            marks = float(input(prompt))
            if marks < 0 or marks > max_marks:
                print(f"Marks must be between 0 and {max_marks}.")
                continue
            return marks
        except ValueError:
            print("Invalid input. Please enter a valid number.")