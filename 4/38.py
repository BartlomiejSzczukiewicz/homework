def f(palindrome):
    expression = expression.lower()  
    expression = ''.join(expression.split()) 

    return expression == expression[::-1]