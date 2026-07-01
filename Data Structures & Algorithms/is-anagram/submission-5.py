class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq_s = self.freq(s)
        freq_t = self.freq(t)

        return freq_s == freq_t
    
    def freq(self, strs):
        # code 
        # init the dict to be returned 
        hashy = {}

        for i in strs:
            if i in hashy:
                hashy[i] += 1 
            else:
                hashy[i] = 1 
        
        return hashy 