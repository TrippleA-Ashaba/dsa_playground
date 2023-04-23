import random
import unittest

from secret_santa_code import secret_santa
from two_sum_code import two_sum


class TestTwoSum(unittest.TestCase):
    def test_two_sum_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        assert two_sum(nums, target) == (0, 1)

    def test_two_sum_2(self):
        nums = [3, 2, 4]
        target = 6
        assert two_sum(nums, target) == (1, 2)

    def test_two_sum_3(self):
        nums = [3, 3]
        target = 6
        assert two_sum(nums, target) == (0, 1)


class TestSecretSanta(unittest.TestCase):
    def test_secret_santa(self):
        players = ["Cartman", "Kyle", "Stan", "Kenny"]
        result = secret_santa(players)

        # Test that all players are paired
        assert len(result) == len(players)

        # Test that each player gives a gift once
        givers = [pair[0] for pair in result]
        assert all(givers.count(player) == 1 for player in players)

        # Test that each player receives a gift once
        receivers = [pair[1] for pair in result]
        assert all(receivers.count(player) == 1 for player in players)

        # Test that no player is paired with themselves
        assert all(pair[0] != pair[1] for pair in result)

        # Test that the pairings are random
        players_copy = players.copy()
        result_copy = result.copy()
        random.shuffle(players_copy)
        random.shuffle(result_copy)
        assert result != result_copy  # a few age cases


if __name__ == "__main__":
    unittest.main()
