arr = [1,2,3,4,5,6,7,8,9,10,11,12]
func = lambda x: x%2==0 and x%3 ==0
result = list(filter(func,arr))
print(result)