dicte = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
arr =[]

for key,value in dicte.items():
    if value>0:
        arr.append(key)
print(arr)