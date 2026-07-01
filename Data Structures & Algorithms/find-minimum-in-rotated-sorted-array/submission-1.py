class Solution:
    def findMin(self, nums: List[int]) -> int:
        # code
        # init left and right pointers
        left = 0
        right = len(nums) - 1 
        # while low is less than high 
        while left < right: 
            mid = (left + right) // 2 
            # if middle number is greater than right 
            if nums[mid] > nums[right]: 
                # move the left poitner
                left = mid + 1 
            # if not 
            else:
                # right = middle 
                right = mid 
        # return he convergence point 
        return nums[right]
