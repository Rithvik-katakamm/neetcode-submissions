class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Understand:
        # input - list called tokens
        # the list will have operations that looks like 
        # a b \operatior\
        # here our job is to build an algorithm that does the operation 
        # a \operator\ b

        # code 
        # init stack
        stack = []
        # loop through list 
        for tok in tokens:
            if tok in ('+', '-', '*', '/'):
                b = stack.pop()
                a = stack.pop()
                if tok == '+':
                    res = a + b 
                elif tok == '-':
                    res = a - b
                elif tok == '*':
                    res = a * b
                else:
                    res = int(a / b)
                stack.append(res)
            else:
                stack.append(int(tok))
        
        return stack[-1]
