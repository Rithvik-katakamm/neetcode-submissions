class Solution:
    def isValid(self, s: str) -> bool:
        # input -> string that contains set of brackets 

        # stack: last in first out. 

        # code 
        # init stack
        stack = []
        # define a lookup table for closing brackets
        closing = {
            ']':'[',
            '}':'{',
            ')':'('
        }

        # s = '[]'
        # parse the string
        for brac in s:
            # if the stack is not empty and we see a closinig brac
            if brac in closing:
                if stack and closing[brac] == stack[-1]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(brac)
            
            

        # if stack is empty return true else false
        return not stack
        