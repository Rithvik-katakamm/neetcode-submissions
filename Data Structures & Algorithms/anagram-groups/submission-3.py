class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashy = {}
        # loop through the list 
        for i in strs:
            # create a count list 
            freq_list = self.freq_list(i)
            if freq_list in hashy:
                hashy[freq_list].append(i)
            else:
                hashy[freq_list] = [i]
            
        # return a list of the values 
        return list(hashy.values())
    def freq_list(self, s):
        count = [0] * 26

        for letter in s:
            count[ord(letter) - ord('a')] += 1
        
        return tuple(count) 
