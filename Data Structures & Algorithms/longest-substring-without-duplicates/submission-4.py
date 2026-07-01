class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # undersrtand
        # input: s -> string 
        # find the length if the longest substrong in s witout repetition 
        # expected output: len -> int

        # code 
        # init 
        left = 0 
        best = 0 
        seen = set()
        # expand the window 
        for right in range(len(s)):
            char = s[right]
            # reduce the window unti; we remove the duplicate.
            while char in seen:
                seen.remove(s[left])
                left += 1 
            # update best length
            seen.add(char)
            best = max(best, right - left + 1)
        # return best 
        return best