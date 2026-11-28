class Solution:
    def isValid(self, s: str) -> bool:
        
        # example: s = '[{()}]'

        stack = []

        bracket = {
            ')':'(',
            ']':'[',
            '}':'{'
        }


        for i in s:
            if i in bracket:
                if stack and stack[-1] == bracket[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)


        return not stack

        