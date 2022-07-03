# start - 20h30-20h50
# Goal : Create and desplay a player's inventory with the number of things

from operator import inv
from typing import final


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    total_stuff = 0
    print('Inventory:')
    for keys, values in inventory.items():
        print(values, keys)
        total_stuff += values
    print('Total number of items: ' + str(total_stuff))

# Part 2 - Goal : Add a 'loot' to the inventary and display the uptated one


dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


# return a dictionary that reprensents the updated dictionary
def add_to_inventory(inventory: dict, dragon_loot: list):
    # for each loot, check if it is existing in the inventory
    # no = creation / yes = add
    print('Inventory:')
    for loot_object in dragon_loot:
        if loot_object in inventory.keys():
            inventory[loot_object] += 1
        else:
            inventory[loot_object] = 1
    return inventory


final_inventory = add_to_inventory(inventory, dragon_loot)
display_inventory(final_inventory)
