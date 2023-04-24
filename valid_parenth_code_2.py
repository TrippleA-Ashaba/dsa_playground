"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

"""


def isValid(s):
    stack = list()

    if len(s) % 2 != 0 or s[0] not in [
        "(",
        "{",
        "[",
    ]:  # Odd numbered strings can't be valid
        return False

    for char in s:
        if char in ["(", "{", "["]:
            stack.append(char)
        elif char == ")" and len(stack) != 0 and stack[-1] == "(":
            stack.pop()
        elif char == "}" and len(stack) != 0 and stack[-1] == "{":
            stack.pop()
        elif char == "]" and len(stack) != 0 and stack[-1] == "[":
            stack.pop()
        else:
            return False

    return len(stack) == 0


if __name__ == "__main__":
    s = "()"
    print(isValid(s))

    s = "()[]{}"
    print(isValid(s))

    s = "(]"
    print(isValid(s))
