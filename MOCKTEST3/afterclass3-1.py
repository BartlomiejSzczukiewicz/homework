arr = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
 ("Jackson","Peter"),("Johnson","Rick"),
 ("Lewis","Terry"),("Clarke","Robin")]

func = lambda x: x[0][0] == 'J'
result = list(filter(func,arr))
print(result)