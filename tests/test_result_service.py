import unittest

from services.result_service import get_formatted_student_result


class TestStudentResultService(unittest.TestCase):

    def test_calculates_total_percentage_and_grade(self):
        marks_data = [
            ("Amit", 101, "Python", 90, 100),
            ("Amit", 101, "Statistics", 80, 100),
            ("Amit", 101, "SQL", 85, 100)
        ]

        result = get_formatted_student_result(marks_data)

        self.assertEqual(result["total_marks"], 255)
        self.assertEqual(result["total_max_marks"], 300)
        self.assertEqual(result["percentage"], 85.0)
        self.assertEqual(result["grade"], "A")
        self.assertEqual(result["result"], "PASS")

    def test_empty_marks_returns_none(self):
        result = get_formatted_student_result([])

        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()