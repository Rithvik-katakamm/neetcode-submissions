class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         #input: nums -> list, target 
         # output = [first_number_idx. second_number_idx]

         # solution:

         # hashmap
         comp = {}

         # loop 
         for i,num in enumerate(nums):
            compli = target - num
            if num in comp:
                return [comp[num], i]
            else:
                comp[compli] = i
            