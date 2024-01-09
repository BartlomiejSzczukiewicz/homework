def f(d):
    passangers = 0
    counter = 0
    result = 0
    for value in d.values():
        counter += 1
        passangers += value
    average = passangers/counter
    for i in d.values():
        if i>average:
            result += 1
    return result


print(f({"LO231":150,"BA787":120,"NZ15":30})) #2
print(f({"LO231":150,"BA787":20,"NZ15":30}))  #1
