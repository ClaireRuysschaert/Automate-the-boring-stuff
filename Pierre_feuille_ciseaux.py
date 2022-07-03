import random
# Display the name of the game
print("ROCK, PAPER, SCISSORS")
# Create variables that counts wins, losses and ties
numberOfWins = 0
numberOfLosses = 0
numberOfTies = 0

# Display the number of wins,losses and ties
print(f'{numberOfWins} Wins, {numberOfLosses} Losses, {numberOfTies} Ties')

player_wants_to_play = True

while player_wants_to_play:
    # Ask the player to choose a move
    while True:
        print('Enter a move : (r)ock, (p)aper, (s)cissors or (q)uit')
        playerNumber = input()
        if playerNumber == 'p':
            print('PAPER versus....')
        elif playerNumber == 'r':
            print('ROCK versus....')
        elif playerNumber == 's':
            print('SCISSORS versus...')
        elif playerNumber == 'q':
            player_wants_to_play = False
            break

        # Ask the computer a random number that correspond to p r or s
        randomNumber = random.randint(1, 3)
        if randomNumber == 1:
            randomNumber = 'r'
            print('ROCK')
        elif randomNumber == 2:
            randomNumber = 'p'
            print('PAPER')
        elif randomNumber == 3:
            randomNumber = 's'
            print('SCISSORS')

        # Display the score --> each score is different and generates a point
        # exemple : if randomnumber==playernumber, print('It is a tie!')
        if randomNumber == playerNumber:
            print('This is a tie!')
            numberOfTies = numberOfTies+1
        elif randomNumber == 'r' and playerNumber == 's':
            print("You loose!")
            numberOfLosses = numberOfLosses+1
        elif randomNumber == 'r' and playerNumber == 'p':
            print('You win!')
            numberOfWins = numberOfWins+1
        elif randomNumber == 'p' and playerNumber == 's':
            print('You win!')
            numberOfWins = numberOfWins+1
        elif randomNumber == 'p' and playerNumber == 'r':
            print("You loose!")
            numberOfLosses = numberOfLosses+1
        elif randomNumber == 's' and playerNumber == 'p':
            print("You loose!")
            numberOfLosses = numberOfLosses+1
        elif randomNumber == 's' and playerNumber == 'r':
            print('You win!')
            numberOfWins = numberOfWins+1
        print(f'{numberOfWins} Wins, {numberOfLosses} Losses, {numberOfTies} Ties')
