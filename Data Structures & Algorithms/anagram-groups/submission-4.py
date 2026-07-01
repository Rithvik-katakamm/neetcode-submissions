class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashy = {}
        # loop through the list 
        for word in strs:
            # convert the string into a count list 
            count = [0] * 26 
            for char in word:
                count[ord(char) - ord('a')] += 1 
            count = tuple(count)
            # append the count list as a key in a hashmap
            hashy[count] = hashy.get(count, [])
            hashy[count].append(word)
        # return the values of the hashmap as a list 
        return list(hashy.values())