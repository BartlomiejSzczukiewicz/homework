import json

def f(years, course):
    with open('data.json', 'r') as file:
        data = json.load(file)
        eligible_students = 0
        
        for student in data:
            if student['age'] >= years:
                for course_data in student['studies']['courses']:
                    if course_data['name'] == course:
                        grade_sum = sum(course_data['grades'])
                        grade_average = grade_sum / len(course_data['grades'])
                        if grade_average >= 4:
                            eligible_students += 1
                            break  
            
        return eligible_students

num_eligible_students = f(21, "statistics")
print(f"The number of eligible students is: {num_eligible_students}")
