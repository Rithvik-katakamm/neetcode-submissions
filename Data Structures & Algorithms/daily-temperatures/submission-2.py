class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Understand 
        # we have a list temperature
        # where temperature[i] is the tempeature on ith day
        # expected return is a list (result) 
        # where result[i] is the number of days after which a warmer day appears 

        # code 
        # init 
        result = []
        # fix the first number
        for i in range(len(temperatures)):
            count = 0
            found = False 
            # iteratre through every number after the fixed number
            for j in range(i+1, len(temperatures)):
                count += 1
                # if a temp higher than current number is found then append the count 
                if temperatures[j] > temperatures[i]:
                    result.append(count)
                    found = True  
                    break
            # if not found append 0
            if not found:
                result.append(0)
        # return the result 
        return result