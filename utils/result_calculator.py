def calculate_percentage(total_marks, total_max_marks):
    if total_max_marks <= 0:
        return 0
    
    return (total_marks / total_max_marks) * 100


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"
    
    
def calculate_result(marks_data):
    if not marks_data:
        return None
    
    total_marks=0
    total_max_marks=0
    all_subjects_passed=True
    
    for record in marks_data:
        marks = record[3]
        max_marks = record[4]
        
        if max_marks <= 0 or marks < 0 or marks > max_marks:
            raise ValueError("Invalid marks or max_marks value.")
        
        total_marks += marks
        total_max_marks += max_marks  
        
        if marks < max_marks * 0.4:
            all_subjects_passed = False   
            
    percentage = calculate_percentage(total_marks, total_max_marks)
    
    grade = calculate_grade(percentage)
    
    if  all_subjects_passed:
        result = "Pass" 
    else:
        result = "Fail"
        
    return {
        "total_marks": total_marks,
        "total_max_marks": total_max_marks,
        "percentage": percentage,
        "grade": grade,
        "result": result
    }