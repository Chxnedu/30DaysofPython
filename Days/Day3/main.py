# Conditional Statements

# Code Challenge: Odd or Even number detector
#number = int(input("What number do want to check?: "))
#modulus = number % 2
#if modulus == 1:
#    print("It is an odd number")
#else:
#    print("It is an even number")

# Code Challenge 2: BMI Calculator 2.0
"""
height = float(input("What is your height in metres?:"))
weight = float(input("What is your weight in kilos?:"))
formula = weight / (height ** 2)
bmi = float(round(formula, 1))
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are OBESE!")
else:
    print(f"Your BMI is {bmi}, you are CLINICALLY OBESED!!! HIT THE GYM!!")
"""
# Code Challenge 3: Leap Year Checker
year = int(input("What Year do you want to check?: "))
if year % 4 != 0:
    print("It is not a leap year.")
elif year % 100 != 0:
    print("It is a leap year.")
elif year % 400 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year.")