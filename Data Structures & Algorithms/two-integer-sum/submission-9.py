class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         # lets find the compliment of the current number we are on and then see if it exists in the lst 

         # solution: 
          
        comp_map = {}

        # loop through list 
        for i,number in enumerate(nums):
            compliment = target - number
            if number in comp_map: 
                return [comp_map[number],i]
            else:
                comp_map[compliment] = i
        return []