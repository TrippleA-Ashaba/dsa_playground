import unittest
from two_sum_code import two_sum
from secret_santa_code import secret_santa


class TwoSumTest(unittest.TestCase):
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


# class SecretSantaTest(unittest.TestCase):
#     def setUp(self):
#         self.players=['Cartman','Kyle','Stan','Kenny','Butters','Greg']

#     def test_secret_santa(self):
#         result=[]


if __name__ == "__main__":
    unittest.main()
