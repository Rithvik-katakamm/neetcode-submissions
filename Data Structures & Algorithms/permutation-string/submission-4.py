class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        ''' sliding window ''' 

        # code
        # edge case 
        if len(s1) > len(s2):
            return False 
        # init 2 freq array
        s1map = [0] * 26 
        window = [0] * 26 
        left = 0
        # init the matches variable 
        matches = 0 
        # get the matches counter up to speed with first window 
        for i in range(len(s1)):
            s1map[ord(s1[i]) - ord('a')] += 1 
            window[ord(s2[i]) - ord('a')] += 1 
        
        for i in range(26):
            if s1map[i] == window[i]:
                matches += 1
        # slide the window right 
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True 
            
            idx = ord(s2[right]) - ord('a')
            window[idx] += 1
            # update the matches counter 
            if s1map[idx] == window[idx]:
                matches += 1
            elif s1map[idx] + 1 == window[idx]:
                matches -= 1 

            # remove the left element 
            idx = ord(s2[left]) - ord('a')
            window[idx] -= 1 

            if s1map[idx] == window[idx]:
                matches += 1
            elif s1map[idx] - 1 == window[idx]:
                matches -= 1 
            
            left += 1 
        
        # return if matches matches 26 
        return matches == 26
        