class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
         # init a pointer i, output 
         i = 0
         output = []
         # cache the len (nums)
         n = len(nums)
         # sort the list
         nums.sort()
         # fix i as a pointer that traverses until len nums - 2
         for i in range(0, n-2):
            # 2 pointer 2 sum 
            left = i + 1 
            right = n - 1 
            # loop through the list with these 2 pointers
            while left < right:
                # add the nums
                add = nums[left] + nums[right]
                # check if the sum is equal to -nums
                if add == -nums[i]:
                    # triplet 
                    triplet = [nums[i], nums[left], nums[right]]
                    # checek if the triplet is in the output 
                    if triplet not in output:
                        # add it to the output
                        output.append(triplet)
                # if add greater than -nums[i]
                if add < -nums[i]:
                    # move the left pointer 
                    left += 1
                else:
                    # move the right  
                    right -= 1 
         # return the output                
         return output

