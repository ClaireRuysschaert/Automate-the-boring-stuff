import zombiedice
import random


class Random_zombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # if there is only one dice roll, randomly choose to continue or stop
        
        while diceRollResults is not None:
            choice = random.randint(0,1)
            if choice == 0:
                diceRollResults = zombiedice.roll()
            else:
                break


class Until_two_brains:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # stops rolling after it has rolled two brains, else continue
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains >= 2:
                break
            else:
                diceRollResults = zombiedice.roll()


class Until_two_shotguns:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # stops rolling after it has rolled two shotguns, else continue
        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            if shotguns >= 2:
                break
            else:
                diceRollResults = zombiedice.roll()


class One_to_four:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # rolls one to four times but stops if there is 2 shotguns
        shotguns = 0
        dice_rolls = 0
        random_one_four = random.randint(1, 4)
        while diceRollResults is not None:
            dice_rolls += 1
            shotguns += diceRollResults['shotgun']
            if dice_rolls <= random_one_four:
                if shotguns >= 2:
                    break
                else:
                    diceRollResults = zombiedice.roll()
            else:
                break


class More_shotguns:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # stops rollins after it has rolled more shotguns than brains
        shotguns = 0
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']
            if brains < shotguns:
                break
            else:
                diceRollResults = zombiedice.roll()



zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 1 Shotgun', minShotguns=1),
    Random_zombie(name='Random Zombie'),
    Until_two_brains(name='Until Two Brains'),
    Until_two_shotguns(name='Until Two Shotguns'),
    One_to_four(name='One to Four'),
    More_shotguns(name='More shotguns than Brains')
)

zombiedice.runTournament(zombies=zombies, numGames=1000)
