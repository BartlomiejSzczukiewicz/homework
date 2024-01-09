def f(fnc,res):
    return print(fnc1())

res = [95,90,20,50,70] 
fnc1 = lambda x: x>50
f(fnc1,res)  #25
fnc2 = lambda x: x>30 and x<90
f(fnc2,res)  #20
