class Solution:
    def isValid(self, s: str) -> bool:
        # understand 
        # input - s -> string
        # it consists of brackets we using for coding 
        # we need to figure out if s is a vlaid string or not 
        # a valid string here means every open bracet must be closed by the same bracket in order 
        # each opened bracket must be closed by the same type of bracket

        # Approuch 
        # use a stack to store opening bracets 
        # when we see a closing bracket in the list we compare it to the top element ih the stack 
        # if they match cool, if not well cool too but its not valid 
        
        # code 
        # init a stack 
        stack = []
        # create a hash map that has closing brackets as htey key and the opening bracket as the value for checking
        closing = {')':'(', ']':'[', '}':'{'}
        # loop through the list 
        for brac in s:
            # if we see a closing bracket
            if brac in closing and stack: 
                # pop off the top of the stack and see if it is the currusoponding opening bracket 
                top = stack.pop()
                if top != closing[brac]:
                    return False 
            # else push the char into the stack
            else: 
                stack.append(brac) 
        # returh true if er make it out
        if not stack:
            return True
        else: 
            return False 
        
        