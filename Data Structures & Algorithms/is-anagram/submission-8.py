class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return self.chars(s) == self.chars(t)



    def chars(self, string):

        hashy = {}

        for i in range(0,len(string)):
            if string[i] in hashy:
                hashy[string[i]] += 1
            else:
                hashy[string[i]] = 0

        return hashy 
        