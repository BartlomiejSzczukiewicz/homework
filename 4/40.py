def f(number):
    number_str = str(number)
    digit_count = {}

    for digit in number_str:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1

    total_sum = 0
    for digit, count in digit_count.items():
        if count > 1:
            total_sum += int(digit) * count

    return total_sum

if __name__ == '__main__':
    print(f(1223334444))
