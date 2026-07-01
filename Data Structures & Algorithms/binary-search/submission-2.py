class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # understand 
        # input: nums 
        # nums is sorted in ascending order. 
        # example [2,4,5,6,7,8,9]
        # target is an integer whose index we need to find or we return -1 
        # we must run the solution in log n time 
        # expected return is the index of target -> int 

        # code(
        # init a high low pointer 
        low = 0 
        high = len(nums) - 1 
        # loop through the list
        while low <= high: 
            # calculate middle term
            mid = (high + low)//2
            # if middle is target
            if nums[mid] == target: 
                # return index
                return mid 
            # elif middle is greater than target
            elif nums[mid] > target:  
                # move high pointer to middle - 1 
                high = mid - 1 
            # else when middle is less than target
            else: 
                # move the low pointer mid + 1
                low = mid + 1
        # if all else fails return -1 
        return -1    
         