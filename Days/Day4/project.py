import random

# Rock Paper Scissors Game
player_choice = int(input("Make a choice. 0 for Rock, 1 for Paper, 2 for Scissors: "))
options = ["rock", "paper", "scissors"]
comp_choice = random.randint(0, 2)
if player_choice == 0:
    if comp_choice == 0:
        print("Computer chose " + options[comp_choice] + " it's a draw!")
    if comp_choice == 1:
        print("Computer chose " + options[comp_choice] + ", You lose!")
    if comp_choice == 2:
        print("Computer chose " + options[comp_choice] + ", You win!")
elif player_choice == 1:
    if comp_choice == 0:
        print("Computer chose " + options[comp_choice] + ", You win!")
    if comp_choice == 1:
        print("Computer chose " + options[comp_choice] + ", It's a draw!")
    if comp_choice == 2:
        print("Computer chose " + options[comp_choice] + ", You lose!")
elif player_choice == 2:
    if comp_choice == 0:
        print("Computer chose " + options[comp_choice] + ", You lose!")
    if comp_choice == 1:
        print("Computer chose " + options[comp_choice] + ", You win!")
    if comp_choice == 2:
        print("Computer chose " + options[comp_choice] + ", It's a draw!")
else:
    print("Kiamman follow the instructions, blast guy!")