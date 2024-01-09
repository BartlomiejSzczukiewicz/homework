arr = [(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]

arr2 = []

for element in arr:
    element = list(element)
    element.remove(min(element))
    element.remove(max(element))
    arr2.append(element)
func = lambda x: sum(x)
result = list(map(func,arr2))
print(result)
        