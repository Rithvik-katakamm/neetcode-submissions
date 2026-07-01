class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # init 
        hashy = {}
        # loop through the list
        for word in strs: 
            count = [0] * 26
            # Loop through the chars in the list
            for char in word:
                # create a count list
                count[ord(char) - ord('a')] += 1 
            # make the count list a tuple 
            count = tuple(count)
            # append the word to the matching tuple
            if count in hashy:
                hashy[count].append(word)
            else:
                hashy[count] = [word]
        # return the balues of the hash map as a list 
        return list(hashy.values())
            