class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Understand: 
        # the list is a valid arethmetic expression we must execute
        # seems like based on the example we apply the oparend that shows up after the number
        # to the answer of the previous expression 
        
        # approuch 
        # seems like a stack problem 
        # when we see a number we push it into the stack 
        # when we see an operand we pop out the 2 numbers in stack
        # apply the opparand to them 
        # push the result back to the stack 
        # on the last step return the top of the stack (result)

        # questions
        # how would i understand what is a number and what is an operand 
        # they are all strings 
        # how would i mention the last step case as hey pop off the only number in there

        # code 
        stack = []

        # loop through list 
        for i in tokens: 
            # if stack is not empty and token is a operand
            if i in {'+', '-', '*', '/'}:
                # pop off 2 numbers 
                num1 = stack.pop()
                num2 = stack.pop()
                # apply operand
                if i == '+':
                    res = num1 + num2 
                elif i == '-':
                    res = num2 - num1
                elif i == '*':
                    res = num1 * num2
                else:
                    res = int(num2/num1)   
                # push result back to stack
                stack.append(res) 
            # else 
            else: 
                # push number into the stack
                stack.append(int(i))
        # return top of stack
        return stack[-1]

        