class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # input:
        # nums -> list, target -> int

        # expected output:
        # i, j -> ints (indices) such that
        # nums[i] + nums[j] == target

        #trival: brute force, read list twice (upper tri)

        # code
        # init a hash map to store compliments of seen nums
        seen = {}

        # read the list
        for i in range(0, len(nums)):
            # compute comp
            comp = target - nums[i]
            # if comp exists for curr number in hash
            if comp in seen:
                # return curr and stored index
                return [seen[comp], i] 

            # store curr num and idx in comp
            seen[nums[i]] = i


