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
        max_freq = 0 
        max_window = 0 
        seen = {}

        for right in range(len(s)):
            # example s = 'XYYX'
            if s[right] in seen:
                seen[s[right]] += 1 
            else: 
                seen[s[right]] = 1

            max_freq = max(max_freq, seen[s[right]])

            if (right - left + 1) - max_freq > k:
                seen[s[left]] -= 1 
                left += 1
            
            max_window = max(max_window, right - left + 1)
        return max_window
             