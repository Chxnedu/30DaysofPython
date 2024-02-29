# Data Types

print("Hello"[2])

# a string cannot be added to an int and vice versa
num = 74
print("a string cant mix with a " + num)

# to make them work together, use type casting to change the data type
num = 74
new_num = str(num)
print("a string can now mix with " + new_num)
# you can also use it for different data types like converting int to float and vice versa

# Code Challenge
two_digit_number = input("Give me a 2 digit number\n")
print(int(two_digit_number[0]) + int(two_digit_number[1]))
# Or you could do it with a lot of variables 
first_num = two_digit_number[0]
second_num = two_digit_number[1]
result = int(first_num) + int(second_num)
print(result)

# Code Challenge 2: BMI Calculator
height = float(input("What is your height in metres?:"))
weight = float(input("What is your weight in kilos?:"))
formula = weight / (height ** 2)
bmi = int(formula)
print(bmi)

# For easy conversion without using type casting, you can use an F-string
num = 4
print(f"the number is {num}")

# To round a number, use the "round()" function
num1 = 34.567
num2 = 23.8675
result = num1 * num2
print(round(result, 2))

# Code Challenge 3: Life Calculator
current_age = int(input("What is your current age?:"))
death_age = 90
years_left = death_age - current_age
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")