weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

heightinm = height/100
bmi = weight/heightinm**2

print("Your BMI index:", bmi)
if(bmi<= 24.9 and bmi>= 18.5 ):
    print("Correct weight: True")
else:
    print("Correct weight: False")

