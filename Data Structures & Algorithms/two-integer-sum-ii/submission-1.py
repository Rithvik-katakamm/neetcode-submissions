class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Understand:
        # input: numbers -> list, target -> int
        # find out the indicies of the 2 numbers that add up to target 
        # index starts at 1 
        # numbers are sorted: [1,2,3,4]
        # must use O(1) space 

        # approuch:
        # 2 pointer
        
        # code:
        # init 2 pointers 
        left = 0 
        right = len(numbers) - 1 
        # loop through numbers 
        # example [1,2,3,4], target = 6
        while left < right: 
            # add the poninted numbers 
            add = numbers[left] + numbers[right]
            # return indices if the sum equal to target
            if add == target:
                return [left+1, right+1]
            # if not, check if its greater or less
            elif add < target:
                # update accordingly
                left += 1 
            else: 
                right -= 1 
        # return empty string if we make it out
        return []