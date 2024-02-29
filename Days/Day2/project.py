# A Tip Calculator
print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill?: $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
new_total = float((tip_percent / 100) * total_bill + total_bill)
people = int(input("How many people to split the bill? "))
each_person_pays = round(new_total / people, 2)
print(f"Each person should pay: ${each_person_pays}")
