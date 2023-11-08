import math

even = 0
number = 0
digit_sum = 0

def f(number, even):
    number = str(input("imput a number: "))
    for digit in len(number):
        if digit.isdigit():
            digit_sum += int(digit)
    return number, even

f(number, even)
print(digit_sum)
