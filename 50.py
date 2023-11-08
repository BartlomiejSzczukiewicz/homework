def sum(n):
    sum = 0
    for i in range (0,n+1):
        sum += i
    return sum

if __name__ == '__main__':
    print(sum(4))