class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init 
        prod = 1 
        res = []
        for i in nums:
            res.append(prod)
            prod *= i

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= prod 
            prod *= nums[i]

        return res
            