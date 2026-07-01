class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # UNDERSTAND 
        # input: ["act","pots","tops","cat","stop","hat"]
        # output:  [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        # Approach
        # use a hashmap where the keys are sorted words from strs and the values are 
        # lists of the strings that match the sorted letters  
        # return a stiched together list of the values after visiting all the strs
        
        # Steps 
        # init a hashmap
        don = {}
        # loop through the list
        for word in strs:  
            # sort the letters of the word
            letters = "".join(sorted(word))
            # add sorted letters a key to the map, along with the word as a value
            if letters in don:
                don[letters].append(word)
            else: 
                don[letters] = [word]
        # return the values of the map as a stiched lists of lists 
        return list(don.values())
        # complexity 
        # time - n*k log k 
        # space - n*k

