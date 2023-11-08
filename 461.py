def f(product_code):
    if len(product_code) != 4:
        return False

    first_digits = int(product_code[:2])
    fourth_digit = int(product_code[3])
    total = 0

    while first_digits > 0:
        total += first_digits % 10
        first_digits //= 10

    expected_digit = total % 7

    return expected_digit == fourth_digit

if __name__ == '__main__':
    print(f("2035"))
