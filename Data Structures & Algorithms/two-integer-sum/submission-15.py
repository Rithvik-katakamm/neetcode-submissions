class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # understand 
        # input: nums -> [], target -> int
        # expected output: [i,j] 
        # where i and j are idx of nums that add up to targer


        ''' brute force '''

        # code
        # init the hashmao 
        hashy = {}
        # loop through the list 
        for i in range(len(nums)):
            # calc compliment 
            compli = target - nums[i]
            # if compliment in map
            if compli in hashy:
                #return compliment idx and curr idx
                return[hashy[compli], i]
            # if not 
            else:
                # add compli to hashy and the idx as val 
                hashy[nums[i]] = i 
        return []