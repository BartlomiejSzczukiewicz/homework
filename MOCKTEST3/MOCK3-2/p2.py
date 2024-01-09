import re
def f(x,y,d):
    arr = []
    if x<y:
        for i in range(x,y):
            arr.append(x)
            x+=1
        arr.append(x)
    else:
        for i in range(y,x):
            arr.append(y)
            y+=1
        arr.append(y)
    for element in arr:
        if re.match(d,str(element)):
            return True
    return False


print(f(10,15,"14"))  #True
print(f(100,120,"11"))  #True
print(f(205,210,"04"))  #False
