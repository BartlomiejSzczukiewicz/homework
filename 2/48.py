def f(product_code):
    # Check if the input has exactly 4 digits
    if len(product_code) != 4 or not product_code.isdigit():
        return False

    # Extract the first three digits and the fourth control digit
    first_three_digits = int(product_code[:3])
    control_digit = int(product_code[3])

    # Calculate the expected control digit based on the rules
    expected_control_digit = (first_three_digits % 7)

    # Compare the expected control digit with the provided control digit
    return control_digit == expected_control_digit

if __name__ ==  '__main__':
    print(f("1082"))  
