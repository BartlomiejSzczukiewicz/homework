def f(number):
    sum = 0
    string_number = str(number)
    for i in string_number:
        if string_number.count(i) > 1:
            sum += int(i)
    return sum

if __name__ == '__main__':
    print(f(230335))