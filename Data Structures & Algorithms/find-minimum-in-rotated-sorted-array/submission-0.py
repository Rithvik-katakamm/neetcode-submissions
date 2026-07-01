class Solution:
    def findMin(self, nums: List[int]) -> int:
        # code
        # init hte high and low pointers
        left = 0
        right = len(nums) - 1 
        # while left < right
        while left < right:
            # calcualte mid
            mid = (left + right) // 2
            # check if niddle number is greater than right
            if nums[mid] > nums[right]:
                # move left to mid + 1 
                left = mid + 1 
            # if not
            else:
                # move the right pointer to middle
                right = mid 
        # return the left element
        return nums[left]