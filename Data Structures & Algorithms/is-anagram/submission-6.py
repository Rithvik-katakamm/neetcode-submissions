class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return self.chars(s) == self.chars(t)



    def chars(self, string):

        hashy = {}

        for i in string:
            hashy[i] = i

        return hashy 
        