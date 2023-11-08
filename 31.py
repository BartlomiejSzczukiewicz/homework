def f(x,y):
    counter = 0
    for i in range (x,y):
        if i%2 == 0 and i<0:
            counter += 1
    return counter

if __name__ == '__main__':
    print(f(-7,8))
    print(f(-1,11) )
