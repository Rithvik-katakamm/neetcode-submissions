class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # understand 
        # input: s -> string 
        # return the len of the longest substring in s without duplicates 
        # expected return: max_len -? int

        ''' sliding window '''

        # code 
        left = 0
        seen = set()
        best = 0 

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left]) 
                left += 1
            seen.add(s[right])
            best = max(best, right - left + 1)

        return best
