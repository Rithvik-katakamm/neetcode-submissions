class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Understand 
        # input: nums -> list, target -> int 
        
        # code 
        # init left and right pointer. 
        left = 0 
        right = len(nums) - 1
        # while left is less than right
        while left <= right:
            # cal mid
            mid = (left + right) // 2
            # check if mid is the target
            if nums[mid] == target:
                return mid
            # check if left is less than right 
            if nums[left] <= nums[mid]:
                # check if the target is in between left and mid 
                if nums[left] <= target < nums[mid]:
                    # move right pointer left
                    right = mid - 1 
                # if not
                else:
                    # move the left pointer right
                    left = mid + 1 
            # if not 
            else: 
                # check if the target is between mid and high
                if nums[mid] < target <= nums[right]:
                    # move pointer right
                    left = mid + 1
                # if not 
                else:
                    # move pointer left
                    right = mid - 1  
        # return not found
        return -1