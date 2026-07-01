class Solution:
    def findMin(self, nums: List[int]) -> int:
        # code 
        # init the left right pointers 
        left = 0
        right = len(nums) - 1
        # while low is less than right 
        while left < right:
            # calc mid 
            mid = (left + right) // 2 
            # if mid is greater than right 
            if nums[mid] > nums[right]:
                # move the left pointer
                left = mid + 1 
            # if not 
            else: 
                # move the right pointer 
                right = mid 
        # return the right most pointer 
        return nums[right]