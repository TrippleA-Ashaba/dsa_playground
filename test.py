import random
import unittest

from secret_santa_code import secret_santa
from two_sum_code_1 import two_sum
from valid_parenth_code_2 import isValid
from best_time_buy_stock_4 import maxProfit
from valid_palindrome_5 import valid_palindrome


# Secret Santa
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


# ! 1. TwoSum
class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        assert two_sum([2, 7, 11, 15], 9) == (0, 1)

        assert two_sum([3, 2, 4], 6) == (1, 2)

        assert two_sum([3, 3], 6) == (0, 1)


#! 2. Valid Parentheses
class TestValidParentheses(unittest.TestCase):
    def test_valid_parenthesis(self):
        assert isValid("()[]{}") == True

        assert isValid("(]") == False

        assert isValid("]()") == False

        assert isValid("(]{}") == False

        assert isValid(" ") == False


# ! 4. Best time to buy and sell stock
class TestBestTimeBuyAndSell(unittest.TestCase):
    def test_best_time_buy_sell(self):
        assert maxProfit([7, 1, 5, 3, 6, 4]) == 5

        assert maxProfit([7, 6, 4, 3, 1]) == 0

        assert maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]) == 9


# ! 5. Valid Palindrome


class TestValidPalindrome(unittest.TestCase):
    def test_valid_palindrome(self):
        assert valid_palindrome("A man, a plan, a canal: Panama") == True

        assert valid_palindrome(" ") == True

        assert valid_palindrome("0P") == False

        assert valid_palindrome("race a car") == False


if __name__ == "__main__":
    unittest.main()
