def f(binary_number):
    for digit in binary_number:
        if digit != '0' and digit != '1':
            return False
    return True
        
if __name__ == '__main__':
    print(f('101'))
    print(f('11010310101'))