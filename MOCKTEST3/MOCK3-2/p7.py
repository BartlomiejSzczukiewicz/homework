
arr = [[3,4,2,1],
       [2,2,2,0],
       [5,0,0,5],
       [4,7,0,2],
       [0,2,0,0]]

def f(arr2D):
    arr1 = []
    temp = list(zip(*arr2D))
    for element in temp:
        arr1.append(sum(element))
    for i in arr1:
        if arr1.count(i) > 1:
            return True
    return False

print(f([[3,4,2],[5,1,6]]))  #True
print(f([[3,4,2],[5,1,7]]))  #False
print(f([[3,4],[5,1],[4,7]]))  #True
print(f([[3,4],[5,9],[4,7]])) # False
