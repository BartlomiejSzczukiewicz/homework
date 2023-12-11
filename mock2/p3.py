def f(array2D):
    sum_rows = 0
    for i in range(0,len(array2D)-1):
        sum_row = sum(array2D[i])
        sum_column = list(zip(*array2D))
        if sum_row != sum(sum_column[i]):
            return False
    return True
print(f([[3,7,2],
         [4,2,5],
         [5,2,1]]))
print(f([[3,7,2],[4,2,5],[9,2,1]]))
