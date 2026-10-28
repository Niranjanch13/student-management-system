# main.py
import logging
import logger_config

logger = logging.getLogger(__name__)

logger.info("Starting the Student Management System...")

from models.teacher import Teacher

from models.marks import Marks

import datetime

#from utils.result_calculator import calculate_result
from services.result_service import get_formatted_student_result

from repositories.student_repository import StudentRepository

from database import (
    add_marks_to_db,
    add_student_to_db,
    display_students_from_db,
    search_student_by_roll_number,
    update_student_in_db,
    delete_student_from_db,
    student_id_exists,
    roll_number_exists,
    get_attendance_summary,

    add_teacher_to_db,
    display_teachers_from_db,
    search_teacher_by_id,
    update_teacher_in_db,
    delete_teacher_from_db,
    
    add_attendance_to_db,
    display_student_attendance,
    get_student_marks,
    update_student_marks,
    delete_student_marks
)

from models.student import Student


from models.marks import Marks

from utils.validation import (
    get_integer_input,
    get_not_empty_input,
    get_email_input,
    get_marks_input,
    get_positive_integer_input,
    get_valid_marks
)

def add_student():

    while True:
        student_id = get_integer_input("Enter student ID: ")

        if student_id <= 0:
            print("Student ID must be greater than 0.")
            continue
        
        if StudentRepository.student_id_exists(student_id):
            print("Student ID already exists. Please enter a different ID.")
            continue

        break

    name = get_not_empty_input("Enter student name: ")

    while True:
        roll_number = get_integer_input(
            "Enter student roll number: "
        )

        if roll_number <= 0:
            print("Roll number must be greater than 0.")
            continue

        if StudentRepository.roll_number_exists(roll_number):
            print("Roll number already exists. Please enter a different roll number.")
            continue

        break

    email = get_email_input("Enter student email: ")

    student = Student(
        student_id,
        name,
        roll_number,
        email
    )

    add_student_to_db(student)

def display_students():
    StudentRepository.get_all()


def search_student():

    roll_number = get_integer_input(
        "Enter the roll number of the student to search: "
    )

    student = StudentRepository.search_by_roll_number(roll_number)

    if student:
        print("\n----- STUDENT FOUND -----")
        print("Student ID:", student[0])
        print("Name:", student[1])
        print("Roll Number:", student[2])
        print("Email:", student[3])
    else:
        print("Student not found.")


def update_student():

    roll_number = get_integer_input(
        "Enter the roll number of the student to update: "
    )

    student = StudentRepository.search_by_roll_number(roll_number)

    if student is None:
        print("Student not found.")
        return

    print("\n----- CURRENT STUDENT DETAILS -----")
    print("Student ID:", student[0])
    print("Name:", student[1])
    print("Roll Number:", student[2])
    print("Email:", student[3])

    print("\nEnter new details:")

    name = get_not_empty_input("Enter new name: ")
    email = get_not_empty_input("Enter new email: ")

    update_student_in_db(
        roll_number,
        name,
        email
    )


def delete_student():

    roll_number = get_integer_input(
        "Enter the roll number of the student to delete: "
    )

    success = StudentRepository.delete(roll_number)

    if success:
        print("Student deleted successfully!")
        
def attendance_report():
    student_id = get_integer_input("Enter student ID: ")
    summary = get_attendance_summary(student_id)

    if not summary or summary[0] == 0:
        print("No attendance records found")
        return
    
    total_days = summary[0]
    present_days = summary[1]   
    absent_days = summary[2]
    
    percentage= (present_days / total_days) * 100 
    
    print("\n----- ATTENDANCE SUMMARY -----")
    print("Student ID:", student_id)
    print("Total Classes:", total_days)
    print("Present:", present_days)
    print("Absent:", absent_days)
    print("Attendance Percentage:", round(percentage, 2), "%")


def main():

    while True:

        print("\n----- STUDENT MANAGEMENT SYSTEM -----")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
       
        print("\n----- TEACHER MANAGEMENT SYSTEM -----")
        print("6. Add Teacher")
        print("7. Display Teachers")
        print("8. Search Teacher")
        print("9. Update Teacher")
        print("10. Delete Teacher")
        
        print("\n----- ATTENDANCE MANAGEMENT SYSTEM -----")
        print("11. Mark Attendance")
        print("12. View Student Attendance")
        print("13. Attendance Report")
        print("14. Add Marks")
        print("15. View Student Marks")
        print("16. View Student Result")
        print("17. Update student Marks")
        print("18. Delete student Marks")
        print("\n----- EXIT -----")     
        print("19. Exit")

        choice = input("Enter your choice (1-19): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            add_teacher()

        elif choice == "7":
            display_teachers()

        elif choice == "8":
            search_teacher()

        elif choice == "9":
            update_teacher()

        elif choice == "10":
            delete_teacher()
            
        elif choice == "11":
            mark_attendance()
            
        elif choice == "12":
            view_student_attendance()
            
            
        elif choice == "13":
            attendance_report()
            
        elif choice == "14":
            add_marks()
            
        elif choice == "15":
            view_student_marks()

        elif choice == "16":
            view_student_result()

        elif choice == "17":
            update_marks()
            
        elif choice == "18":
            delete_marks()
            
        elif choice == "19":
            print("Exiting...")
            logger.info("Exiting the Student Management System...")
            break

        else:
            print("Invalid choice. Please try again.")

def add_teacher():
    teacher_id = get_integer_input("Enter teacher ID: ")
    name = get_not_empty_input("Enter teacher name: ")
    subject = get_not_empty_input("Enter subject taught: ")
    email = get_not_empty_input("Enter teacher email: ")

    teacher = Teacher(
        teacher_id,
        name,
        subject,
        email
    )

    add_teacher_to_db(teacher)
    
def display_teachers():
    display_teachers_from_db()
    
    
def search_teacher():
    teacher_id = get_integer_input(
        "Enter the ID of the teacher to search: "
    )

    teacher = search_teacher_by_id(teacher_id)

    if teacher:
        print("\n----- TEACHER FOUND -----")
        print("Teacher ID:", teacher[0])
        print("Name:", teacher[1])
        print("Subject:", teacher[2])
        print("Email:", teacher[3])
    else:
        print("Teacher not found.")
        
def update_teacher():
    teacher_id = get_integer_input(
        "Enter the ID of the teacher to update: "
    )

    teacher = search_teacher_by_id(teacher_id)

    if teacher is None:
        print("Teacher not found.")
        return

    print("\n----- CURRENT TEACHER DETAILS -----")
    print("Teacher ID:", teacher[0])
    print("Name:", teacher[1])
    print("Subject:", teacher[2])
    print("Email:", teacher[3])

    print("\nEnter new details:")

    name = get_not_empty_input("Enter new name: ")
    subject = get_not_empty_input("Enter new subject: ")
    email = get_not_empty_input("Enter new email: ")

    update_teacher_in_db(
        teacher_id,
        name,
        subject,
        email
    )
    
def delete_teacher():
    teacher_id = get_integer_input(
        "Enter the ID of the teacher to delete: "
    )

    success = delete_teacher_from_db(teacher_id)

    if success:
        print("Teacher deleted successfully!")
        
def mark_attendance():
    student_id = get_integer_input("Enter student ID: ")
    
    print("\nselect attendance status:")
    print("1. Present")
    print("2. Absent")
    
    choice=input("Enter your choice (1-2): ")
    
    if choice=="1":
        status="Present"    
    
    elif choice=="2":
        status="Absent"
    
    else:
        print("Invalid choice")
        return

    attendance_date = datetime.date.today()
    
    print("attendance_date:",attendance_date)
    
    add_attendance_to_db(student_id,attendance_date,status)

def view_student_attendance():
    student_id = get_integer_input("Enter student ID: ")
    display_student_attendance(student_id)

def add_marks():
    student_id = get_integer_input("Enter student ID: ")
    subject = get_not_empty_input("Enter subject: ")
    marks_value = get_marks_input("Enter marks obtained (0-100): ")

    marks= Marks(student_id, subject, marks_value)
    percentage = marks.percentage()

    add_marks_to_db(marks)

def view_student_marks():
    student_id = get_positive_integer_input("Enter student ID: ")
    marks_data = get_student_marks(student_id)

    if not marks_data:
        print("No marks records found for the student.")
        return

    print("\n----- STUDENT MARKS -----")
    
    total_marks=0
    total_max_marks=0
    
    for record in marks_data:
        name,roll_number,subject,marks,max_marks=record
        
        percentage = (marks / max_marks) * 100 
        
        print(f"Name: {name}, Roll Number: {roll_number}, Subject: {subject}, Marks: {marks}/{max_marks}, Percentage: {percentage:.2f}%")

    if total_max_marks > 0:
        overall_percentage = (total_marks / total_max_marks) * 100
        print("\n----- OVERALL RESULTS -----")
        print(f"Total Marks: {total_marks}/{total_max_marks}")
        print(f"Overall Percentage: {overall_percentage:.2f}%")
        

def view_student_result():
    student_id = get_positive_integer_input(
        "Enter Student ID: "
    )

    marks_data = get_student_marks(student_id)

    if not marks_data:
        print("No marks found for this student.")
        return

    result_data = get_formatted_student_result(marks_data)

    if result_data is None:
        print("Unable to calculate the result.")
        return

    name = marks_data[0][0]
    roll_number = marks_data[0][1]

    print("\n========== STUDENT RESULT ==========")
    print(f"Student Name: {name}")
    print(f"Roll Number: {roll_number}")

    print(
        f"Total Marks: {result_data['total_marks']}/"
        f"{result_data['total_max_marks']}"
    )

    print(f"Percentage: {result_data['percentage']:.2f}%")
    print(f"Grade: {result_data['grade']}")
    print(f"Result: {result_data['result']}")

    
def update_marks():
    student_id = get_positive_integer_input("Enter student ID: ")
    subject = get_not_empty_input("Enter subject: ")
    
    new_marks = get_valid_marks("Enter new marks obtained (0-100): ", 100)
    
    update_student_marks(student_id, subject, new_marks)
    
def delete_marks():
    student_id = get_positive_integer_input("Enter student ID: ")
    subject = get_not_empty_input("Enter subject: ")
    
    confirmation = input(f"Delete {subject} marks for student ID" f" {student_id}? (yes/no): ")
    if confirmation != "yes":
        print("Deletion cancelled.")
        return
    delete_student_marks(student_id, subject)
        
if __name__ == "__main__":
    main()