def f(fnc, prods):
    return ','.join([fnc(prod) for prod in prods])

# Przykładowe wywołania funkcji z podanymi lambdami
prods = ["water", "cheese", "tomato"]
fnc1 = lambda x: "id:" + x[:2]
fnc2 = lambda x: (x[0] + x[-1]).upper()

result1 = f(fnc1, prods)
result2 = f(fnc2, prods)

print(result1, result2)

