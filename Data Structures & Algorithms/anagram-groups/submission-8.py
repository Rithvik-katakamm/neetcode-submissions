class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # input shape: strs -> list of strings
        # exoected output shape: list of lists of strings. 

        # code 
        # init hashmap for grouping anagrams and counting chars. 
        hashy = {}
        # read the list
        for word in strs: 
            chars = {}
            # read the word 
            for char in word:
                # dev a freq map of chars
                if char not in chars:
                    chars[char] = 1
                else:
                    chars[char] += 1 
            # define that as key
            key = tuple(sorted(chars.items()))
            # if the key is new
            if key in hashy:
                # add it to the hashmap 
                hashy[key].append(word) 
            else:
                hashy[key] = [word]

        # return the values of our new hashmap as a list
        return list(hashy.values()) 