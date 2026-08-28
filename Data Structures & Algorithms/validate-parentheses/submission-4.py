class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        key = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for char in s:
            if char not in key:
                stack.append(char)
            elif stack and key[char] == stack[-1]:
                stack.pop()
            else:
                 return False

        return not stack
