def f(number, even):
    number_str = str(number)
    total_sum = 0 

    for digit in number_str:
        if even and int(digit) % 2 == 0:
            total_sum += int(digit)
        elif not even and int(digit) % 2 != 0:
            total_sum += int(digit)

    return total_sum

if __name__ == '__main__':
    print(f(3124, False))
    print(f(3124, True))