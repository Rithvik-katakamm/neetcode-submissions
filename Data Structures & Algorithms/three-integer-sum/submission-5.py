class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
         # init a pointer i, output\
         i = 0 
         output = []
         # cache the len (just got funzies)
         n = len(nums)
         # sort the list
         nums.sort()
         # loop through list
         while i < n - 2:
            left = i + 1 
            right = n - 1 
            # loop thought again with 2 other pointers 
            while left < right:
                # add the left and right nums 
                add = nums[left] + nums[right]
                triplet = [nums[i], nums[left], nums[right]]
                # check if solution is -nums[i]
                if add == -nums[i]:
                    # if it is and does not exist in output add it 
                    if triplet not in output:
                        output.append(triplet)
                # if sum is greater than - nums[i]
                if add > -nums[i]:
                    # move the right pointer inward
                    right -= 1 
                # if not move the left pointer right 
                else:
                    left += 1 
            # increment i
            i += 1 
         # return the output
         return output 