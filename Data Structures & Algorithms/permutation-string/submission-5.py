class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # code 
        # edge case 
        if len(s1) > len(s2):
            return False 
        # init an array 
        s1map, window = 26 * [0], 26 * [0]
        matches = 0
        left = 0 
        # lets calibrate the freq couht in the freq arrays. 
        for i in range(len(s1)):
            s1map[ord(s1[i]) - ord('a')] += 1 
            window[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if s1map[i] == window[i]:
                matches += 1 

        # expand the window to the right
        for right in range(len(s1), len(s2)):

            if matches == 26:
                return True 
        
            idx = ord(s2[right]) - ord('a')
            window[idx] += 1 

            if s1map[idx] == window[idx]:
                matches += 1 
            elif s1map[idx] + 1 == window[idx]: # overshot by one 
                matches -= 1
        
            # remove the left idx
            idx = ord(s2[left]) - ord('a')
            window[idx] -= 1 

            if s1map[idx] == window[idx]:
                matches += 1 
            elif s1map[idx] - 1 == window[idx]: # undershot by one 
                matches -= 1 

            # increment left
            left += 1

        return matches == 26
            
            



        