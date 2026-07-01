class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Understand 
        # we have a list temperature
        # where temperature[i] is the tempeature on ith day
        # expected return is a list (result) 
        # where result[i] is the number of days after which a warmer day appears 

        # code 
        # init a stack, results
        stack = []
        results = [0] * len(temperatures) 
        # loop through the temperatures list index wise
        for idx in range(len(temperatures)):
             # while the temp idx points at is larger than top of stack
            while stack and temperatures[idx] > temperatures[stack[-1]]:
                # pop the idx in stack 
                popped_idx = stack.pop()
                # calc delta of curr idx and poppped
                count = idx - popped_idx 
                # append result the results of popped idx
                results[popped_idx] = count 
            # append the curr idx to stack 
            stack.append(idx)
        # return the result list
        return results  
