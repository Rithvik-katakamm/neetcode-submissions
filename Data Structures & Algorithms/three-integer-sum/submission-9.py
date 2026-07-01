class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
          # define the fixed pointer, output
          i = 0 
          output = []
          # sort the list
          nums.sort() #O(n log n)
          # loop through the list with a fixed point 
          for i in range(0, len(nums) - 2): # O(n^2)
            # define the 2 pointers 
            left = i + 1 
            right = len(nums) - 1 
            # define the target 
            target = -nums[i]
            # if i points at a number more than 0
            if nums[i] > 0:
                # break the loop get out
                break
            # if i is more than 0 and it pointers at the same num it did before
            if i > 0 and nums[i] == nums[i-1]:
                # continue the loop from the top 
                continue
            # while the first pointer is less than the second
            while left < right: 
                # add the nums they point too
                add = nums[left] + nums[right] 
                # if they add up to the target
                if add == target:
                    # append all 3 nums pointed at to the output
                    output.append([nums[i], nums[left], nums[right]])
                    # now move the left and right pointers to point at different numbers 
                    left += 1 
                    right -= 1
                    # while the condtion still holds
                    while left < right and nums[left] == nums[left - 1]:
                        # move left if it points at the same number as before
                        left += 1 
                    # same for the right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                # if they add up to more than the target 
                elif add > target:
                    # move the right pointer 
                    right -= 1 
                # if they add up to less than the target
                else:
                    # move the left pointer 
                    left += 1 
          # return the ouput 
          return output
                

