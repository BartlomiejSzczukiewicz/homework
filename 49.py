def f(product_code):

    sum = 0

    first_digits = product_code[::2]
    int_first_digits = int(first_digits)
    int_first_digits = int(first_digits)

    while int_first_digits != 0:
        sum += int_first_digits%10
        int_first_digits = int_first_digits//10

    expected_digit = sum%7
    last_digit = product_code[3]
    int_last_digit = int(last_digit)

    if expected_digit == int_last_digit:
        return True
    else:
        return False
    
print(f("1082"))
print(f("1114"))
print(f("2035"))