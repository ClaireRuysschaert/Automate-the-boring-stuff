import random

print("Welcome to Rock paper scissors !")
print("""
Please choose one of the 3 :
1) Rock
2) Paper
3) Scissors

""")



player_wants_to_play = True
number_of_wins = 0
number_of_losses = 0
number_of_ties = 0

while player_wants_to_play:

    user_selection = int(input("Your choice : "))
    while user_selection not in range(1, 4) :
        print("Please enter a number between 1 and 3")
        user_selection = int(input("Your choice : "))

    ai_choice = random.random(1,3)

    if ai_choice == user_selection:
        number_of_ties += 1
        print("égalité parfaite !")

    else:
        