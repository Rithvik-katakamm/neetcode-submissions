class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # understand
        # input: s
        # return the len of the longest substring in s without repeating a char
        # all chars in this substring must be unique 
        # expected return: len(max_substring) 

        ''' sliding window '''

        # code 
        # init 
        left = 0 
        seen = set()
        max_len = 0 
        # expand the right window 
        for right in range(len(s)):
            # cache the char 
            char = s[right]
            # while current char is in seen
            while char in seen:
                # remove left char 
                seen.remove(s[left])
                # move left forward
                left += 1 
            # add char to seen
            seen.add(char)
            # store mac len
            max_len = max(max_len, right - left + 1)
        # return max len
        return max_len