# Programming the Hangman game
import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
guess = input("Guess a letter from the word. ").lower()

for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")

display = []
for letter in chosen_word:
    display.append("_")

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if guess == letter:
        display[position] = letter
print(display)

