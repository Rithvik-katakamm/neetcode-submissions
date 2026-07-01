class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # undersrtand
        # input: s -> string 
        # find the length if the longest substrong in s witout repetition 
        # expected output: len -> int

        # code 
        # init the slow and fast pointers
        slow = 0 
        seen = set()
        best = 0 
        # loop through 
        for fast in range(len(s)):
            while s[fast] in seen:
                seen.remove(s[slow]) 
                slow += 1 
            seen.add(s[fast])
            best = max(best, fast - slow + 1)
        return best 
