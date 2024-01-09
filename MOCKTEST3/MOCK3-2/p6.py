def f(mnumbers):
    counter = 0
    arr = ['1','2','3','4','5','6','7','a','b','c','d','A','B','C','D','-','+']
    sign = ['-','+']
    signcount = 0
    for element in mnumbers:
        for char in element:
            if char in sign:
                signcount += 1
                if signcount > 1:
                    break
            if char not in arr:
                break
        counter += 1
    return counter

print(f(["A15","-31","7abC","+D1","-gH"]))  #5
print(f(["A05","-3+1","7ab8C","+D1","-22k"]))  #1
