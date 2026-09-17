class Solution:
    def findMin(self, nums: List[int]) -> int:
         first = 0 
         last = len(nums) - 1 

         while first < last:
            mid =(first + last)// 2

            if nums[mid] >= first:
                low = mid + 1
            else:
                high = mid


         return high
