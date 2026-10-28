
from utils.result_calculator import calculate_result


def get_formatted_student_result(marks_data):
    result = calculate_result(marks_data)

    if result is None:
        return None

    return {
        "total_marks": result["total_marks"],
        "total_max_marks": result["total_max_marks"],
        "percentage": round(result["percentage"], 2),
        "grade": result["grade"],
        "result": result["result"]
    }

