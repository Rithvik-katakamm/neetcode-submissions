import numpy as np 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # pointers

        #example: [-1,0,3,2,6,9,10]

        low = 0 
        high = len(nums) - 1 

        while low <= high:

            mid = (low + high) //2

            if nums[mid] == target:
                return mid 

            elif target > nums[mid]:
                low = mid + 1 
            
            else:
                high = mid - 1 

        return -1 