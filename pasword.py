def f(password):
    if len(password)<6:
        return False
    for i in password:
        if password.count(i)>1:
            return False
    return True

if __name__ == '__main__':
    print(f("book123"))
    print(f("A2water3"))
    print(f("qwerty"))