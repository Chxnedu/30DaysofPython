# Conditional Statements

# Code Challenge: Odd or Even number detector
number = int(input("What number do want to check?: "))
modulus = number % 2
if modulus == 1:
    print("It is an odd number")
else:
    print("It is an even number")


# Code Challenge 2: BMI Calculator 2.0
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


# Code Challenge 4: Pizza Program
print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M, L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
else:
    print("Kiamman use the options you were given!!")

print(f"Your final bill is ${bill}")


# Code Challenge 5: Love Calculator
print("Welcome to the Love Calculator")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

letter_T = name1.count("t") + name2.count("t")
letter_R = name1.count("r") + name2.count("r")
letter_U = name1.count("u") + name2.count("u")
letter_E = name1.count("e") + name2.count("e")
true_count = letter_T + letter_R + letter_U + letter_E

letter_L = name1.count("l") + name2.count("l")
letter_O = name1.count("o") + name2.count("o")
letter_V = name1.count("v") + name2.count("v")
letter_E2 = letter_E
love_count = letter_L + letter_O + letter_V + letter_E2

love_score = int(str(true_count) + str(love_count))
if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}, you go together like coke and mentos")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together!")
else:
    print(f"Your score is {love_score}")