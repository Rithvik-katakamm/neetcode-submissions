class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # understandL
        # input: nums, target
        # output: i, j where i and j are indices that add up to target. 

        # code:
        # init hashmap 
        hashy = {}
        # loop through nums
        for i in range(len(nums)):
            # calculate the compliment of the curr num
            comp = target - nums[i] 

            if comp in hashy:
                return [hashy[comp], i]
            else:
                hashy[nums[i]] = i