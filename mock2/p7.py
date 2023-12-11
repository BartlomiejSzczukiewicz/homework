import re

def f(arr):
    counter = 0
    for i in arr:
        if len(i) >= 4 and len(i) <= 12:
            matches = re.search("[^a-z0-9_]",i)
            if not matches:
                counter += 1
    return counter

print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))  

#lowercase letters, numbers and the underscore character. 