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
        seen = {}
        max_window = float('-inf')
        max_freq = 0 
        # loop
        for right in range(len(s)):
            # cache window length 
            window_len = right - left + 1 
            # add value to freq map 
            if s[right] in seen:
                seen[s[right]] += 1
            else:
                seen[s[right]] = 1  
            # check if value freq is max freq
            if seen[s[right]] > max_freq:
                max_freq = seen[s[right]]
            # if window_len - max_freq > k:
            if (window_len - max_freq) > k:
                # remove a freq count of 1 from left
                seen[s[left]] -= 1 
                # push left forward (but what if the max_ freq now changes?)
                left += 1 
            # this is going to be ugly but im re calculating window len 
            window_len = right - left + 1 
            # update best window length 
            max_window = max(max_window, window_len)
        return max_window 