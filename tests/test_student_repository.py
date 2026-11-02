import unittest
from unittest.mock import patch, Mock

from repositories.student_repository import StudentRepository


class TestStudentRepository(unittest.TestCase):

    # 1. Add student successfully
    @patch("repositories.student_repository.add_student_to_db")
    def test_add_student(self, mock_add):
        student = Mock()
        mock_add.return_value = True
        result = StudentRepository.add(student)
        mock_add.assert_called_once_with(student)
        self.assertTrue(result)

    # 2. Add student failure
    @patch("repositories.student_repository.add_student_to_db")
    def test_add_student_failure(self, mock_add):
        student = Mock()
        mock_add.return_value = False
        result = StudentRepository.add(student)
        mock_add.assert_called_once_with(student)
        self.assertFalse(result)

    # 3. Get all students
    @patch("repositories.student_repository.display_students_from_db")
    def test_get_all_students(self, mock_display):
        expected_students = [Mock(), Mock()]
        mock_display.return_value = expected_students
        result = StudentRepository.get_all()
        mock_display.assert_called_once_with()
        self.assertEqual(result, expected_students)

    # 4. Get empty student list
    @patch("repositories.student_repository.display_students_from_db")
    def test_get_all_students_empty(self, mock_display):
        mock_display.return_value = []
        result = StudentRepository.get_all()
        mock_display.assert_called_once_with()
        self.assertEqual(result, [])

    # 5. Find student by roll number
    @patch("repositories.student_repository.search_student_by_roll_number")
    def test_find_by_roll_number(self, mock_search):
        expected_student = Mock()
        mock_search.return_value = expected_student
        result = StudentRepository.find_by_roll_number(101)
        mock_search.assert_called_once_with(101)
        self.assertEqual(result, expected_student)

    # 6. Student not found
    @patch("repositories.student_repository.search_student_by_roll_number")
    def test_find_student_not_found(self, mock_search):
        mock_search.return_value = None
        result = StudentRepository.find_by_roll_number(999)
        mock_search.assert_called_once_with(999)
        self.assertIsNone(result)

    # 7. Update student successfully
    @patch("repositories.student_repository.update_student_in_db")
    def test_update_student(self, mock_update):
        mock_update.return_value = True
        result = StudentRepository.update(101, "Rahul", "rahul@example.com")
        mock_update.assert_called_once_with(101, "Rahul", "rahul@example.com")
        self.assertTrue(result)

    # 8. Update student failure
    @patch("repositories.student_repository.update_student_in_db")
    def test_update_student_failure(self, mock_update):
        mock_update.return_value = False
        result = StudentRepository.update(999, "Rahul", "rahul@example.com")
        mock_update.assert_called_once_with(999, "Rahul", "rahul@example.com")
        self.assertFalse(result)

    # 9. Delete student successfully
    @patch("repositories.student_repository.delete_student_from_db")
    def test_delete_student(self, mock_delete):
        mock_delete.return_value = True
        result = StudentRepository.delete(101)
        mock_delete.assert_called_once_with(101)
        self.assertTrue(result)

    # 10. Delete student failure
    @patch("repositories.student_repository.delete_student_from_db")
    def test_delete_student_failure(self, mock_delete):
        mock_delete.return_value = False
        result = StudentRepository.delete(999)
        mock_delete.assert_called_once_with(999)
        self.assertFalse(result)

    # 11. Student ID exists
    @patch("repositories.student_repository.student_id_exists")
    def test_student_id_exists(self, mock_exists):
        mock_exists.return_value = True
        result = StudentRepository.student_id_exists(1)
        mock_exists.assert_called_once_with(1)
        self.assertTrue(result)

    # 12. Roll number exists
    @patch("repositories.student_repository.roll_number_exists")
    def test_roll_number_exists(self, mock_exists):
        mock_exists.return_value = False
        result = StudentRepository.roll_number_exists(101)
        mock_exists.assert_called_once_with(101)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
