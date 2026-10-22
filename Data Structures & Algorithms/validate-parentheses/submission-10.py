class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in key:                          # closing bracket
                if stack and stack[-1] == key[c]:
                    stack.pop()
                else:
                    return False
            else:                                 # opening bracket
                stack.append(c)

        return not stack