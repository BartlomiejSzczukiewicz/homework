def f(detector):
    temp = 0
    for person in detector:
        if person == "+":
            temp = temp + 1
        else:
            temp = temp - 1
        if temp > 3:
            print('true')
            return True
    if temp < 3:
        print('false')
        return False

f("+-++++++--")
f("+-+-+-+-")