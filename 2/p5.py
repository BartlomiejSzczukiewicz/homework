import math

def is_binary(binary_number):
    for digit in binary_number:
        if digit not in "01":
            return False
    return True

def f():
    binary_number = input("Input a binary number: ")
    if is_binary(binary_number):
        print("It's a valid binary number.")
        return True
    else:
        print("It's not a valid binary number.")
        return False

f()