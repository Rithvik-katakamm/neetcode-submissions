class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closing = {']':'[', '}':'{', ')':'('}

        for char in s:
            if char not in closing:
                stack.append(char)
            elif char in closing and stack[-1] == closing[char]:
                stack.pop()
            else:
                return False

        return not stack