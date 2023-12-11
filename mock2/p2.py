def f(arr):
    arr.sort()
    if arr[0] != arr[1]:
        return arr[0]
    else:
        return arr[len(arr)-1]

print(f([7,7,7,7,7,5,7,7]))
print(f([7,7,7,7,7,9,7,7]))