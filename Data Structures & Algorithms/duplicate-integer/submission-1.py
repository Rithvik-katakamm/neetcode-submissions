class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # input: nums
        # output: boolean

        # solution 
        # use a hashmap to store and lookup values we have seen before 

        seen = {}

        for i in nums: 
            if i in seen:
                return True  
            else:
                seen[i] = 1 
            

        # if you make it out of the loop 
        return False 