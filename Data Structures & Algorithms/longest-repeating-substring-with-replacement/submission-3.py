class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # understand: 
        # input: s -> string, k --> int 
        # k is the max number of repetitions
        # expected return:  variable -> int 
        # where variable is thr len of the longest substring with one reccurring letter

        ''' sliding window ''' 

        # code
        # init left, best, max_freq, seen 
        left = 0
        best = 0 
        seen = {}
        max_freq = 0 
        # loop through the list with right
        for right in range(len(s)):
            # build the hashmap 
            if s[right] in seen:
               seen[s[right]] += 1 
            else:
                seen[s[right]] = 1
            max_freq = max(max_freq, seen[s[right]])
            # ask if the wid_len - max_freq > k 
            if (right - left + 1) - max_freq > k: 
                # remove a count from the left index of seen
                seen[s[left]] -= 1 
                left += 1 
            # calc best len
            best = max(best, right-left+1)
        # return best 
        return best 


