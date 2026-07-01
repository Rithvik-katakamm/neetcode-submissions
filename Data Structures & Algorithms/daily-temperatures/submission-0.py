class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Understand 
        # we have a list temperature
        # where temperature[i] is the tempeature on ith day
        # expected return is a list (result) 
        # where result[i] is the number of days after which a warmer day appears 

        # approuch (brute force) 
        # init 
        result = []
        # fix the number parse through the rest 
        # example: [30,38,30,36,35,40,28]
        for i in range(0,len(temperatures)):
            count = 0
            found = False
            for j in range(i+1, len(temperatures)):
                count += 1 
                if temperatures[i] < temperatures[j]:
                    # append that to the list, if not append 0
                    result.append(count)
                    found = True 
                    break
            if not found:
                result.append(0)
        # return the result 
        return result 