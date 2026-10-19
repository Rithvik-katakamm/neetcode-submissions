class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        for n in range(0, len(nums)):
            for l in range(n + 1, len(nums)):
                if nums[n] == nums[l]:
                    return True


        return False