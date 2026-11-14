class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashy = {}

        for word in strs:
            count = 26 * [0]

            for char in word:
                idx = ord(char) - ord('a')
                count[idx] += 1 
            count = tuple(count)
            
            if count in hashy:
                hashy[count].append(word)
            else:
                hashy[count] = [word]

        return list(hashy.values())
                
            



        