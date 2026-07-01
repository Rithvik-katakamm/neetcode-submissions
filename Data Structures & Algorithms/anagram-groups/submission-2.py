class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Understand: 
        # strs = ["act","pots","tops","cat","stop","hat"]
        # output = [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        # Approach:
        # lets use a hashmap to store the sorted letters of the word
        # we will add all he unique elements as keys and their respective 
        # words as values 

        # Steps:
        # init a hashmap 
        mappy = {}
        # loop through the list
        for word in strs: 
            # sort the letters in the current word
            letters = ''.join(sorted(word))
            # if letters match append it to the value of the key it matchs 
            if letters in mappy:
                mappy[letters].append(word)
            # else append the current word as the first element in value of the key
            else: 
                mappy[letters] = [word]
        # returned stiched list of values
        return list(mappy.values()) 