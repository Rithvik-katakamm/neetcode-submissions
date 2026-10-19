class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return self.chars(s) == self.chars(t)



    def chars(self, string):

        hashy = {}

        for i in string:
            if i in hashy:
                hashy[i] += 1 
            else:
                hashy[i] = 0

        return hashy 
        