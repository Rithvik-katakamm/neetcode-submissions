class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.freq_count(s) == self.freq_count(t)

    def freq_count(self, string: str) -> dict:
        count = {}

        for i in string:
            if i in count:
                count[i] += 1 
            else:
                count[i] = 1 

        return count
