class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # understand: 
        # input: s -> string, k --> int 
        # k is the max number of repetitions
        # expected return:  variable -> int 
        # where variable is thr len of the longest substring with one reccurring letter

        ''' sliding window ''' 

        # code
        # init
        left = 0 
        best = 0 
        seen = {} 
        max_freq = 0 
        # expand the window 
        for right in range(len(s)):
            # cache the char
            char = s[right]
            # hasmap for seen 
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1 
            # figure out what numbers occur the most 
            max_freq = max(max_freq, seen[char])
            # reduce the window when winlen - most freq nunmber is more than k
            while (right - left + 1) - max_freq > k:
                seen[s[left]] -= 1 
                left += 1
            # store the best window length
            best = max(best, right - left + 1) 
        # return best 
        return best 
