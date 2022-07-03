# 1) Create an aleatoire list of heads (H) and tails (T) values
# 2) Check if there is a streak in the list
# 3) Repeat 10 000 times
# 4) Determine the percentage of coin flips containing a streak of six
# heads or tails a row

import random

# Create a function that flip the coin and return the value head or tails


def coin_flip():
    coin_flip = random.randint(0, 1)
    if coin_flip == 0:
        coin_flip = 'H'
    else:
        coin_flip = 'T'

    return coin_flip

# Create a list that recuperate 100 random value (head tail)
# Check if there is a streak in the list


coin_list = []
number_of_streaks = 0
last_flip = ''
six_in_a_row = 0
number_of_rolls = 10000

for element in range(number_of_rolls):
    head_tail = coin_flip()
    coin_list.append(head_tail)
    if last_flip == head_tail:
        number_of_streaks = number_of_streaks + 1
    else:
        number_of_streaks = 1
    last_flip = head_tail
    if number_of_streaks == 6:
        six_in_a_row += 1
        number_of_streaks = 1

# Determine the percentage of coin flips containing a streak of six
# heads or tails a row

frequence_of_streaks = six_in_a_row / number_of_rolls
print(f'Chance of streak : {frequence_of_streaks*100} %')
