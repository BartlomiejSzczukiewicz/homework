import re
def f():
    numString = '1234555325146555'
    fives = re.findall(r'5+', numString)
    len(max(fives))          # most repetitions

    return fives.count(max(fives))  # number of times most repetitions occurs

print(f())
