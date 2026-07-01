class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for index in range(len(nums)):

            compliment = target - nums[index]

            if compliment in seen:
                return [seen[compliment], index]
                break

            else:
                seen[nums[index]] = index




                
                 

