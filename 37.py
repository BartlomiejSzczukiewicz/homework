def f(number,even):
   
   str_number = str(number)
   nr = ''
   sum_even = 0

   if even:
    for digit in str_number:
        if int(digit)%2 == 0:
           nr += digit
    int_nr = int(nr)       
    while int_nr != 0:
       sum_even += int_nr%10
       int_nr = int_nr//10
    return sum_even
   if even == False:
    for digit in str_number:
        if int(digit)%2 != 0:
           nr += digit
    int_nr = int(nr)       
    while int_nr != 0:
       sum_even += int_nr%10
       int_nr = int_nr//10
    return sum_even
   
print(f(3124,True))
print(f(3124,False))