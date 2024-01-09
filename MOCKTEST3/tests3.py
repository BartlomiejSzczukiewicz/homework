arr = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

func = lambda x: x>2
above = list(filter(func,arr))
average = sum(above)/len(above)
print(round(average,2))
