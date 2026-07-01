class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = self.buildmap(s)
        t_map = self.buildmap(t)

        return s_map == t_map
        
    def buildmap(self, string):
        hashmap = {} 

        for i in string:
            if i in hashmap:
                hashmap[i] += 1
            else: 
                hashmap[i] = 1 
        return hashmap

