# Randomization and Lists
import random

# Code Challenge: Heads or Tails
"""
print("Welcome to Coin Toss Program")
luck = random.randint(0, 1)
if luck == 0:
    print("Heads")
else:
    print("Tails")
"""

# Code Challenge 2: Banker Roulette
"""
names_string = input("Give me everybodys names, separated by a comma. ")
names = names_string.split(", ")
list_length = len(names)
rand_name = random.randint(0, list_length - 1)
print(names[rand_name] + " is going to buy the meal today!")
# An easier way to do it is to use random.choice()
"""

# You can nest a list inside another list
fruits = ["carrot", "mango", "banana"]
vegetables = ["spinach", "guava", "avocado"]

combination = [fruits, vegetables]
print(combination)
