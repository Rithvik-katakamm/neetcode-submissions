class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # understand 
        # input: nums -> [], target -> int
        # expected output: [i,j] 
        # where i and j are idx of nums that add up to targer


        ''' 2 pointer '''

        # code
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]