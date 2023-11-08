def f(name):

    acronym = name[0]

    for i in range (len(name)):
        if name[i] == ' ':
            acronym += name[i+1]
    return acronym

if __name__ == '__main__':
    print(f("For Your Information"))