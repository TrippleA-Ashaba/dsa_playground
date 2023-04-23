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


import random


def secret_santa(players):
    giver = players.copy()
    random.shuffle(giver)
    result = [[giver[i - 1], giver[i]] for i in range(len(giver))]

    # Check if any player is paired with themselves
    while any(pair[0] == pair[1] for pair in result):
        random.shuffle(giver)
        result = [[giver[i - 1], giver[i]] for i in range(len(giver))]
    return result


if __name__ == "__main__":
    players = ["Cartman", "Kyle", "Stan", "Kenny", "Butters", "Greg"]
    print(secret_santa(players))
