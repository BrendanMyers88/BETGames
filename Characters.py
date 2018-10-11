import random


class Player(object):

    def __init__(self, name, hp=20):
        self.name = name
        self.hp = hp
        self.level = 1
        self.strength = stat_roll(4, 6)

    def attack(self, target):
        if self.strength <= 0:
            roll = sum(roll_dice(1, 2))
            print("You hit {0} for {1} damage!".format(target.name, roll))
            target.hp -= roll
        elif 1 <= self.strength <= 5:
            roll = sum(roll_dice(1, 4))
            print("You hit {0} for {1} damage!".format(target.name, roll))
            target.hp -= roll
        elif 6 <= self.strength <= 10:
            roll = sum(roll_dice(1, 6))
            print("You hit {0} for {1} damage!".format(target.name, roll))
            target.hp -= roll
        elif 11 <= self.strength <= 15:
            roll = sum(roll_dice(1, 8))
            print("You hit {0} for {1} damage!".format(target.name, roll))
            target.hp -= roll
        elif 16 <= self.strength <= 20:
            roll = sum(roll_dice(2, 8))
            print("You hit {0} for {1} damage!".format(target.name, roll))
            target.hp -= roll


class Enemy(object):

    def __init__(self, name, hp=2):
        self.name = name
        self.hp = hp


class Troll(Enemy):

    def __init__(self, name):
        super().__init__(name=name, hp=20)


class DiceRoll(object):
    """
    Return a number of dice, each having the same number of sides.
    Example:    roll_dice(number, sides)
                roll_dice(2,6) = 2d6
        Arguments:
            1. number - The number of dice rolled.
            2. sides - The number of sides on the dice rolled.
    """

    def __init__(self, number, sides):
        self.number = number
        self.sides = sides

    def roll(self):
        return roll_dice(self.number, self.sides)


def roll_dice(number, sides):
    dice_result = []
    for dice in range(0, number):
        dice_result.append(random.randint(1, sides))
    return dice_result


def stat_roll(number, sides):
    dice_result = []
    for dice in range(0, number):
        dice_result.append(random.randint(1, sides))
    print("We'll drop the lowest roll, " + str(min(dice_result)))
    dice_result.remove(min(dice_result))
    print(str(dice_result) + " were your top 3 rolls, resulting in " + str(sum(dice_result)) + "!")
    return sum(dice_result)


Ted = Player('Ted', 20)
Trolly = Troll('Urgot')

print(Ted.name + " has " + str(Ted.strength) + " strength")
print(Trolly.name + " has " + str(Trolly.hp) + " hit points")
Ted.attack(Trolly)
print(Trolly.name + " has " + str(Trolly.hp) + " hit points")
