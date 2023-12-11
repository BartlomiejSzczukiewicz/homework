def f(subjects):
    counter = 0
    for grades in subjects.values():
        suma = sum(grades)
        average = suma/len(grades)
        subject_list = list(subjects.keys())
        subjects.update({subject_list[counter]:average})
        counter += 1
    return max(subjects, key=subjects.get)
        

print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))