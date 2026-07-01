class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # understand
        # input: s1 -> string, s2 -> string
        # we need to return if any permuation of s1 is in s2
        # expected return: boolean. 

        # code 
        # init left and right 
        left = 0 
        s1map = self.freq(s1)
        # slide the window with a fixed len of s1
        for right in range(len(s1), len(s2)+1):
            window = s2[left:right]
            window_count = self.freq(window)

            if window_count == s1map:
                return True

            left += 1 
        
        return False 

    def freq(self,chars):
        hashy = {}

        for char in chars:
            if char in hashy:
                hashy[char] += 1
            else:
                hashy[char] = 1
        
        return hashy 
