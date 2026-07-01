class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # code 
        # init a freq map 
        smap, tmap = self.freq(s), self.freq(t)
        # compare and return 
        return smap == tmap 

    def freq(self, string):
        hashy = {}
        for char in string:
            if char in hashy:
                 hashy[char] += 1
            else:
                 hashy[char] = 1 
        return hashy 