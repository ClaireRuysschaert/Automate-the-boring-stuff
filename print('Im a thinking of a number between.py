import random
random_number = random.randint(1, 20)  # variable random number
print('Im a thinking of a number between 1 and 20.')

for chosen_number in range (1, 7):  # Ask the player to make a guess 6 times
    print('Take a guess!')
    guess_number = int(input())

    if random_number > guess_number: # different situations
        print('Your guess is too low!')
    elif random_number < guess_number:
        print('Your guess is too high!')
    elif random_number == guess_number:
        print('Good job! You guessed my number in ' + str(chosen_number))
        break

else:
    print('Nope, the random number was ' + str(random_number))