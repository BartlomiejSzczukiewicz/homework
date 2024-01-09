def f(n):
    arr = []
    arr2 = []
    str_n = str(n)
    for digit in str_n:
        arr.append(digit)
    for digit in arr:
        if int(digit)%2 != 0:
            arr2.append(int(digit))
    if not arr2:
        return -1
    return max(arr2) - min(arr2)
    

print(f(10852))
print(f(7235973))
print(f(4388))
print(f(846206))