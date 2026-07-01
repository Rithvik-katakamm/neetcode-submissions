class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # code 
        # init the stack 
        stack = []
        # loop thrxough the list
        for token in tokens: 
            # if element is a operator
            if token in {'+', '-', '*', '/'}:
                # pop 2 nums 
                right = stack.pop()
                left = stack.pop() 
                # perform the operation 
                if token == '+':
                    res = left + right
                elif token == '-':
                    res = left - right 
                elif token == '*':
                    res = left * right
                else: 
                    res = int(left/right)
                # append the reuslt to the stack
                stack.append(res) 
            # else
            else:
                # append the number to the stack
                stack.append(int(token))  
        # return top
        return stack[-1]