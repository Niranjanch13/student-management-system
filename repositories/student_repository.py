from database import (
    add_student_to_db,
    display_students_from_db,
    search_student_by_roll_number,
    update_student_in_db,
    delete_student_from_db,
    student_id_exists,
    roll_number_exists
)


class StudentRepository:

    @staticmethod
    def add(student):
        return add_student_to_db(student)

    @staticmethod
    def get_all():
        return display_students_from_db()

    @staticmethod
    def find_by_roll_number(roll_number):
        return search_student_by_roll_number(roll_number)

    @staticmethod
    def update(roll_number, name, email):
        return update_student_in_db(
            roll_number,
            name,
            email
        )

    @staticmethod
    def delete(roll_number):
        return delete_student_from_db(roll_number)

    @staticmethod
    def student_id_exists(student_id):
        return student_id_exists(student_id)

    @staticmethod
    def roll_number_exists(roll_number):
        return roll_number_exists(roll_number)