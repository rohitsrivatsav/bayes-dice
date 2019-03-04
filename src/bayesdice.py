# from random import choice
# import numpy as np


# class BayesDice:
#     def __init__(self):
#         self.dice = 0
#         self.dices = [4, 6, 8, 12, 20]
#         self.prob = {}
#         self.dice_nums = {4: [l for l in range(1, 5)], 6: [l for l in range(1, 7)], 8: [l for l in range(1, 9)], 12: [l for l in range(1, 13)], 20: [l for l in range(1, 21)]}

#     def choose_die(self):
#         self.dice = choice(self.dices)
#         print("selected dice ")
#         print(self.dice)
#         return self.dice

#     def roll_die(self):
#         print("rolled dice ")
#         c = choice([l for l in range(self.dice + 1)])
#         print(c)
#         return c

#     def update_priors(self, roll):
#         for dice, values in self.dice_nums.items():
#             if(roll in values):
#                 p = 1 / len(values)
#                 self.prob[dice] = p
#             else:
#                 self.prob[dice] = 0.0
#         print(self.prob)

#         # self.prob.append(roll)
import random


class BayesDice:
    # ------------------------------------------------------------ #
    def __init__(self):
        self.dice = [4, 6, 8, 12, 20]
        self.data = {die: 0.20 for die in self.dice}
    # ------------------------------------------------------------ #

    def choose_die(self):
        self.die = random.choice(self.dice)
    # ------------------------------------------------------------ #

    def roll_die(self):
        return random.randint(1, self.die)
    # ------------------------------------------------------------ #

    def update_priors(self, roll):
        print('before update:', self.data)
        denominator = list(map(lambda die: (0 if roll > die else (1 / die)) * self.data[die], self.dice))
        self.data = {self.dice[i]: numerator / sum(denominator) for i, numerator in enumerate(denominator)}
        self.debug(roll, denominator)
    # ------------------------------------------------------------ #

    def debug(self, roll, denominator):
        print('die:', self.die, 'roll:', roll)
        print('denominator:', denominator)
        print('data:', self.data)
        print('sum of priors:', sum(self.data.values()))
        print('sum of denominator:', sum(denominator))
        print('-' * 50)
    # ------------------------------------------------------------ #
