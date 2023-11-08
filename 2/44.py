def f(password):
    if len(password) < 6:
        return False
    
    unique_characters = set(password)

    # Check if the number of unique characters is at least 6
    if len(unique_characters) >= 6:
        return True
    else:
        return False

if __name__ == '__main__':
   
    print(f("password123"))
    print(f("abc12222"))
