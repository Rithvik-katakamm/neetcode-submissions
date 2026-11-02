class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {
            ')':'(',
            ']':'[',
            '}':'{'
        }


        for brac in s:
            if brac in closing:
                if stack and stack[-1] == closing[brac]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(brac)

        return not stack 
