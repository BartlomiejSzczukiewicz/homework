'''''
test_results = [
    {"name":"Peter","result":27},
    {"name":"Anna","result":63},
    {"name":"Robert","result":92},
    {"name":"Paul","result":46},
    {"name":"Barbara","result":52}]


func = lambda x: x>50 and x<70

result =  list(filter(func,(s['result'] for s in test_results)))
print(result)
'''''
#przypomij sobie jak sie odwolywac do poszczegolnych elementow w dict

test_results = [
    {"name": "Peter", "result": 27},
    {"name": "Anna", "result": 63},
    {"name": "Robert", "result": 92},
    {"name": "Paul", "result": 46},
    {"name": "Barbara", "result": 52}
]

# Anonymous function for filtering
func = lambda student: 50 < student["result"] < 70

# Applying the filter function
filtered_students = list(filter(func, test_results))

# Preparing the display of filtered students
filtered_students_display = [{"name": student["name"], "result": student["result"]} for student in filtered_students]
