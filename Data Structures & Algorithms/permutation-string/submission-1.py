class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # code 
        # init
        s1map = self.hashy(s1)
        left = 0 

        # slide through the list with         
        for right in range(len(s1), len(s2) + 1):
            window = s2[left:right]
            window_count = self.hashy(window)

            if window_count == s1map:
                return True 
            
            left += 1

        return False 


    def hashy(self, string):
        # code 
        hashy = {}

        for char in string:
            if char in hashy:
                hashy[char] += 1
            else:
                hashy[char] = 1
        
        return hashy
        

                