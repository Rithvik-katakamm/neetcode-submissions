class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init product, res 
        prod = 1 
        res = []
        # first pass through nums 
        for i in range(len(nums)):
            # append product to the result list
            res.append(prod)
            # update product
            prod *= nums[i]
        # second pass through nums from the back
        prod = 1 
        for i in range(len(nums) - 1, -1, -1): 
            # append running product to result (multiplu with existing val, do not replace)
            res[i] *= prod
            # update product
            prod *= nums[i] 
        
        # return res 
        return res 