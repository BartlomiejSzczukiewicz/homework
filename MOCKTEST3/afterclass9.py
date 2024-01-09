arr = [508,500,512,499,492,511,503,476,501,509]

deviation = 0.02*500
func = lambda x: x<500 + deviation and x>500 - deviation

result = list(filter(func,arr))
print(result)