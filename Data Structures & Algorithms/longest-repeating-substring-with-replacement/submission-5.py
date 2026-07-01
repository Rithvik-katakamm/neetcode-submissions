class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # understand 
        # input: s -> string, k -> int
        # where s is the input string, k is the max number of replacements 
        # expected return: len(max_substring)
        # where substring has unique chars after at most k replacements 

        ''' sliding window '''

        # code 
        # init 
        left = 0 
        seen = {}
        max_freq = 0 
        best = 0 
        # expand the window
        for right in range(len(s)):
            char = s[right] 
            # add element to seen (freq map)
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1 
            # calc most recc char
            max_freq = max(max_freq, seen[char])
            # if the window_len - most recc char > k
            if (right - left + 1) - max_freq > k:
                # reduce the count of seen[left] by 1
                seen[s[left]] -= 1 
                # push left 
                left += 1 
            # calc best len
            best = max(best, right - left + 1) 
        # return best len
        return best