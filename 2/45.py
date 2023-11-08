def f(expression):
    try:
        result = eval(expression)  # Use eval to evaluate the expression
        return result
    except:
        return None  # Handle any errors or invalid expressions

if __name__ == '__main__':
    print(f('2+5'))
    print(f('7-5'))
    print(f('2+5-2'))


