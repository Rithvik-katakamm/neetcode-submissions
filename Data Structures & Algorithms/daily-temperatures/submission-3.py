class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Understand 
        # we have a list temperature
        # where temperature[i] is the tempeature on ith day
        # expected return is a list (result) 
        # where result[i] is the number of days after which a warmer day appears 

        # code (monotonic stack)
        # init the stack, results
        stack = []
        results = [0] * len(temperatures)
        # loop through the temperatures 
        for idx in range(len(temperatures)):
            # while stack is non empty and the top is smaller than current number
            while stack and temperatures[stack[-1]] < temperatures[idx]:
                # pop the index, calculate count, push into result[poppedidx]
                poppedidx = stack.pop()
                count = idx - poppedidx
                results[poppedidx] = count 
            # push i inot stack 
            stack.append(idx)
        # result 
        return results