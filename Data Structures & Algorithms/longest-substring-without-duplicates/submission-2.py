class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # understand 
        # input: s -> string 
        # return the len of the longest substring in s without duplicates 
        # expected return: max_len -? int

        ''' sliding window '''

        # code 
        # init the slow pointer and seen
        slow = 0
        seen = set() 
        best = 0
        # loop through the list 
        for fast in range(len(s)):
            # while the current letter is in seen
            while s[fast] in seen:
                # remove slow pointer from seen
                seen.remove(s[slow])
                # move slow forward 
                slow += 1 
            # add current number to seen
            seen.add(s[fast]) 
            # update the longest substring 
            best = max(best, fast - slow + 1)
        # return longest sub string 
        return best 