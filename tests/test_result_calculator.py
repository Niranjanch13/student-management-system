import unittest

from utils.result_calculator import (
    calculate_percentage,
    calculate_grade,
    calculate_result
)


class TestResultCalculator(unittest.TestCase):

    def test_calculate_percentage(self):
        result = calculate_percentage(85, 100)
        self.assertEqual(result, 85.0)

    def test_calculate_grade(self):
        self.assertEqual(calculate_grade(95), "A+")
        self.assertEqual(calculate_grade(85), "A")
        self.assertEqual(calculate_grade(75), "B")
        self.assertEqual(calculate_grade(65), "C")
        self.assertEqual(calculate_grade(55), "D")
        self.assertEqual(calculate_grade(40), "F")

    def test_calculate_result_pass(self):
        marks_data = [
            ("Amit", 101, "Python", 90, 100),
            ("Amit", 101, "Statistics", 80, 100),
            ("Amit", 101, "SQL", 85, 100)
        ]

        result = calculate_result(marks_data)

        self.assertEqual(result["total_marks"], 255)
        self.assertEqual(result["total_max_marks"], 300)
        self.assertEqual(result["grade"], "A")
        self.assertEqual(result["result"], "PASS")

    def test_calculate_result_fail(self):
        marks_data = [
            ("Amit", 101, "Python", 95, 100),
            ("Amit", 101, "Statistics", 35, 100),
            ("Amit", 101, "SQL", 95, 100)
        ]

        result = calculate_result(marks_data)

        self.assertEqual(result["grade"], "B")
        self.assertEqual(result["result"], "FAIL")

    def test_negative_marks(self):
        marks_data = [("Amit", 101, "Python", -10, 100)]

        with self.assertRaises(ValueError):
            calculate_result(marks_data)

    def test_marks_exceed_maximum(self):
        marks_data = [("Amit", 101, "Python", 110, 100)]

        with self.assertRaises(ValueError):
            calculate_result(marks_data)

    def test_zero_maximum_marks(self):
        marks_data = [("Amit", 101, "Python", 50, 0)]

        with self.assertRaises(ValueError):
            calculate_result(marks_data)

    def test_text_marks(self):
        marks_data = [("Amit", 101, "Python", "eighty", 100)]

        with self.assertRaises(ValueError):
            calculate_result(marks_data)

    def test_boolean_marks(self):
        marks_data = [("Amit", 101, "Python", True, 100)]

        with self.assertRaises(ValueError):
            calculate_result(marks_data)

    def test_invalid_record_structure(self):
        marks_data = [("Amit", 101, "Python", 85)]

        with self.assertRaises(ValueError):
            calculate_result(marks_data)

    def test_empty_marks(self):
        self.assertIsNone(calculate_result([]))


if __name__ == "__main__":
    unittest.main()