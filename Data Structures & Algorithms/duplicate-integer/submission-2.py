class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Code
        # init 
        seen ={}
        # loop through numbers 
        for i in nums:
            # if number is in seen
            if i in seen: 
                # return true
                return True  
            # else add number
            else:
                seen[i] = 1 
        # if loop exit return false 
        return False 