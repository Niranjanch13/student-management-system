import logging

logger = logging.getLogger(__name__)
import mysql.connector
import os
from models.teacher import Teacher
from models.marks import Marks
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def create_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    return connection


def get_all_students():
    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM students"
        cursor.execute(query)

        return cursor.fetchall()

    except mysql.connector.Error as error:
        print("Database error:", error)
        return []

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def add_student_to_db(student):
    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO students
            (student_id, name, roll_number, email)
            VALUES (%s, %s, %s, %s)
        """

        values = (
            student.student_id,
            student.name,
            student.roll_number,
            student.email
        )

        cursor.execute(query, values)
        connection.commit()
        logger.info("Student added to the database successfully.")
        print("Student added to the database successfully.")
        return True

    except mysql.connector.Error as error:
        if connection is not None and connection.is_connected():
            connection.rollback()   
        logger.exception("failed to add student to the database.")
        print("Database error:", error)
        return False

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def display_students_from_db():
    students = get_all_students()

    if not students:
        print("No students found.")
        return

    print("\n----- ALL STUDENTS -----")

    for student in students:
        print("Student ID:", student[0])
        print("Name:", student[1])
        print("Roll Number:", student[2])
        print("Email:", student[3])
        print("------------------------")


def search_student_by_roll_number(roll_number):
    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
            SELECT *
            FROM students
            WHERE roll_number = %s
        """

        cursor.execute(query, (roll_number,))

        return cursor.fetchone()

    except mysql.connector.Error as error:
        print("Database error:", error)
        return None

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def update_student_in_db(roll_number, name, email):
    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
            UPDATE students
            SET name = %s,
                email = %s
            WHERE roll_number = %s
        """

        values = (name, email, roll_number)

        cursor.execute(query, values)
        connection.commit()

        if cursor.rowcount > 0:
            print("Student updated successfully.")
            return True

        print("Student not found.")
        return False

    except mysql.connector.Error as error:
        print("Database error:", error)
        return False

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def delete_student_from_db(roll_number):
    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
            DELETE FROM students
            WHERE roll_number = %s
        """

        cursor.execute(query, (roll_number,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Student deleted successfully.")
            return True

        print("Student not found.")
        return False

    except mysql.connector.Error as error:
        print("Database error:", error)
        return False

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()
            
def add_teacher_to_db(teacher):
    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO teachers
            (teacher_id, name, subject, email)
            VALUES (%s, %s, %s, %s)
        """

        values = (
            teacher.teacher_id,
            teacher.name,
            teacher.subject,
            teacher.email
        )

        cursor.execute(query, values)
        connection.commit()

        print("Teacher added to the database successfully.")

    except mysql.connector.Error as error:
        print("Database error:", error)

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def get_all_teachers():
    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM teachers"

        cursor.execute(query)

        teachers = cursor.fetchall()

        return teachers

    except mysql.connector.Error as error:
        print("Database error:", error)
        return []

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def display_teachers_from_db():

    teachers = get_all_teachers()

    if not teachers:
        print("No teachers found.")
        return

    print("\n----- ALL TEACHERS -----")

    for teacher in teachers:

        print("Teacher ID:", teacher[0])
        print("Name:", teacher[1])
        print("Subject:", teacher[2])
        print("Email:", teacher[3])


def search_teacher_by_id(teacher_id):

    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
            SELECT *
            FROM teachers
            WHERE teacher_id = %s
        """

        cursor.execute(query, (teacher_id,))

        teacher = cursor.fetchone()

        return teacher

    except mysql.connector.Error as error:
        print("Database error:", error)
        return None

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def update_teacher_in_db(teacher_id, name, subject, email):

    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
            UPDATE teachers
            SET name = %s,
                subject = %s,
                email = %s
            WHERE teacher_id = %s
        """

        values = (
            name,
            subject,
            email,
            teacher_id
        )

        cursor.execute(query, values)

        connection.commit()

        if cursor.rowcount > 0:
            print("Teacher updated successfully.")
            return True

        else:
            print("Teacher not found.")
            return False

    except mysql.connector.Error as error:
        print("Database error:", error)
        return False

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def delete_teacher_from_db(teacher_id):

    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
            DELETE FROM teachers
            WHERE teacher_id = %s
        """

        cursor.execute(query, (teacher_id,))

        connection.commit()

        if cursor.rowcount > 0:
            print("Teacher deleted successfully.")
            return True

        else:
            print("Teacher not found.")
            return False

    except mysql.connector.Error as error:
        print("Database error:", error)
        return False

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()
            
def add_attendance_to_db(student_id, attendance_date, status):

    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

    
        check_query = """
            SELECT student_id
            FROM students
            WHERE student_id = %s
        """

        cursor.execute(check_query, (student_id,))

        student = cursor.fetchone()

        if student is None:
            print("Student not found.")
            return False

        # Insert attendance
        query = """
            INSERT INTO attendance
            (student_id, attendance_date, status)
            VALUES (%s, %s, %s)
        """

        values = (
            student_id,
            attendance_date,
            status
        )

        cursor.execute(query, values)

        connection.commit()

        print("Attendance marked successfully.")

        return True

    except mysql.connector.Error as error:

        print("Database error:", error)

        return False

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()
            
def get_student_attendance(student_id):

    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
            SELECT attendance_date,
            student_id,
            attendance_date,
            status
            FROM attendance
            WHERE student_id = %s
            order by attendance_date desc
        """

        cursor.execute(query, (student_id,))

        attendance = cursor.fetchall()

        return attendance

    except mysql.connector.Error as error:
        print("Database error:", error)
        return []

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()
            
def display_student_attendance(student_id):

    attendance = get_student_attendance(student_id)

    if not attendance:
        print("No attendance records found")
        return

    print("\n----- ATTENDANCE RECORDS -----")

    for record in attendance:
        
        print("Student ID:", record[0])
        print("Attendance Date:", record[1])
        print("Status:", record[2])
        print("-------------------------------")


def student_id_exists(student_id):
    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
            SELECT student_id
            FROM students
            WHERE student_id = %s
        """

        cursor.execute(query, (student_id,))
        
        return cursor.fetchone() is not None


    except mysql.connector.Error as error:
        print("Database error:", error)
        return False

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()
            
def roll_number_exists(roll_number):
    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
            SELECT roll_number
            FROM students
            WHERE roll_number = %s
        """

        cursor.execute(query, (roll_number,))
        
        return cursor.fetchone() is not None

    except mysql.connector.Error as error:
        print("Database error:", error)
        return False

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()
            
def get_attendance_summary(student_id):
    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
            SELECT
                COUNT(*) AS total_days,
                SUM(CASE WHEN status = 'Present' THEN 1 ELSE 0 END) AS present_days,
                SUM(CASE WHEN status = 'Absent' THEN 1 ELSE 0 END) AS absent_days
            FROM attendance
            WHERE student_id = %s

        """

        cursor.execute(query, (student_id,))

        result = cursor.fetchall()

        return result

    except mysql.connector.Error as error:
        print("Database error:", error)
        return None

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()
            
            

def add_marks_to_db(marks):
    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        # Check whether the student exists
        cursor.execute(
            "SELECT student_id FROM students WHERE student_id = %s",
            (marks.student_id,)
        )

        if cursor.fetchone() is None:
            print("Error: Student ID does not exist.")
            return False

        # Insert marks into the database
        query = """
            INSERT INTO marks
            (student_id, subject, marks, max_marks)
            VALUES (%s, %s, %s, %s)
        """

        values = (
            marks.student_id,
            marks.subject,
            marks.marks,
            marks.max_marks
        )

        cursor.execute(query, values)
        connection.commit()

        print("Marks added successfully!")
        return True

    except mysql.connector.IntegrityError:
        if connection is not None:
            connection.rollback()

        print(
            "Error: Marks for this student and subject "
            "may already exist."
        )
        return False

    except mysql.connector.Error as error:
        if connection is not None:
            connection.rollback()

        print(f"Database error: {error}")
        return False

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()


            
            
def get_student_marks(student_id):
    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
            SELECT s.name, s.roll_number, m.subject, m.marks, m.max_marks
            FROM marks m
            JOIN students s ON m.student_id = s.student_id
            WHERE m.student_id = %s
        """

        cursor.execute(query, (student_id,))

        results= cursor.fetchall()

        return results

    except mysql.connector.Error as error:
        print("Database error:", error)
        return []

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()
            
def update_student_marks(student_id, subject, new_marks):
    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
            UPDATE marks
            SET marks = %s
            WHERE student_id = %s AND subject = %s
        """

        cursor.execute(query, (new_marks, student_id, subject))



        if cursor.rowcount == 0:
            print("No matching marksrecord found.")
            return False
        
        connection.commit()

        print("Marks updated successfully.")
        return True

    except mysql.connector.Error as error:
        print("Database error:", error)
        return False

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()
            
def delete_student_marks(student_id, subject):
    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
            DELETE FROM marks
            WHERE student_id = %s AND subject = %s
        """

        cursor.execute(query, (student_id, subject))

        if cursor.rowcount == 0:
            connection.rollback()
            print("No matching marks record found.")
            return False
        
        connection.commit()

        print("Student Marks deleted successfully.")
        return True

    except mysql.connector.Error as error:
        if connection is not None:
            connection.rollback()
        print("Database error:", error)
        return False

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()