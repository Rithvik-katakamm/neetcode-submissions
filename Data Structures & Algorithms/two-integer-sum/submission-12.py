class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # understand
        # input - nums-> array[int], target -> int
        # we need to find 2 indicies that add up to target 
        # expected return: [i,j]

        # code 
        # init pointer i,j 
        i = 0 
        # loop through list fixing one number
        for i in range(len(nums)):
            # loop through every other number in the list
            for j in range(i + 1, len(nums)):
                # add up numbers and see if they are equal to target
                add = nums[i] + nums[j]
                if add == target:
                    # if they are return indices
                    return[i,j] 
 