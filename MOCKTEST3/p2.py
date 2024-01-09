def f(x,y,digit):
    arr = []
    counter = 0
    if y>x:
        while x != y:
            arr.append(x)
            x += 1
        arr.append(x)
    elif x<y:
        while y != x:
            arr.append(y)
            y += 1
        arr.append(y) #oki mamy liste

    str_arr = []
    for element in arr:
        str_arr.append(str(element))
    for element in str_arr:
        for char in element:
            if char == str(digit):
                counter += 1
    return counter

print(f(10,15,1))
print(f(28,32,2))
print(f(100,105,6))
print(f(100,101,0))
