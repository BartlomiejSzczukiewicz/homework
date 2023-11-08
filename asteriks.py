def f(n):
    temp = '*'
    for i in range (0,n):
        if n == 1:
            return temp
        else:
            temp += '/*'
    return temp
print(f(1))
print(f(5))