class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        compli = {}

        for i in range(0, len(nums)):
            if nums[i] in compli:
                return [compli[nums[i]], i]
            compliment = target - nums[i]
            compli[compliment] = i

        
        