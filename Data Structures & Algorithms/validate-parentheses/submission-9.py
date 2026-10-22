class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        key = {
            ')':'(',
            ']':'[',
            '}':'{'

        }

        for i in s:
            if stack and i in key:
                stack.pop()
            else:
                stack.append(i)

        if not stack:
            return True
        else:
            return False

