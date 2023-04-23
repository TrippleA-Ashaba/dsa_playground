"""
SECRET SANTA

Given a list of players, pair up players do that:

1. Each player gives a gift once
2. Each player receives a gift once
3. Players cannot give or receive to themselves
4. Selections must be random

Example input: ['Cartman','Kyle','Stan','Kenny','Butters']
Example output: [['Cartman', 'Stan'], ['Kyle', 'Cartman'], ['Stan', 'Kyle'], 
                ['Kenny', 'Butters'], ['Butters', 'Kenny']]

"""


import copy
from random import shuffle
import collections


def secret_santa(players):
    giver = copy.deepcopy(players)
    shuffle(giver)
    result = []
    for i, player in enumerate(players):
        if player != giver[i]:
            result.append([player, giver[i]])
        else:
            i += 1
    if len(result) != len(players):
        return secret_santa(players)
    return result


if __name__ == "__main__":
    players = ["Cartman", "Kyle", "Stan", "Kenny", "Butters", "Greg"]
    print(secret_santa(players))
