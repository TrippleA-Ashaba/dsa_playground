"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Example 3:

Input: s = "leetcode", t = "code"
output: false

"""


# def is_anagram(s, t):    # O(n logn)
#     if len(s) != len(t):
#         return False
#     return sorted(s) == sorted(t)


def is_anagram(s, t):  # O(n)
    if len(s) != len(t):
        return False

    char_counter = {}

    for char in s:
        char_counter[char] = char_counter.get(char, 0) + 1

    for char in t:
        if char not in char_counter:
            return False
        char_counter[char] -= 1

        if char_counter[char] < 0:
            return False

    return all(count == 0 for count in char_counter.values())


if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))
    print(is_anagram("rat", "car"))
    print(is_anagram("leetcode", "ceodeelt"))
