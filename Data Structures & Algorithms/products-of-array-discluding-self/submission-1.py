class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # set prod
        prod = 1
        res1 = [0] * len(nums)
        res2 = [0] * len(nums)
        res = [0] * len(nums)
        # run through the list and bnuild left prod
        for i in range(len(nums)):
            res1[i] = prod 
            prod *= nums[i]
        # reset prod 
        prod = 1 
        # build right prod list
        for i in range(len(nums)-1,-1,-1):
            res2[i] = prod
            prod *= nums[i]
        # multiple both the lists into new lists.
        for i in range(len(res1)):
            res[i] = res1[i] * res2[i]

        return res  