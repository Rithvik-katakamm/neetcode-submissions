class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

         
        # code
        # init 
        anagram = {}
        # read the list of strs
        for word in strs:
            chars = {} 
            # read the string
            for char in word: 
                # dev a hashmap
                if char not in chars:
                    chars[char] = 0
                chars[char] += 1
            # make the hash map a tuple and key
            key = tuple(sorted(chars.items()))
            # if the key is not present in another hashmap
            if key not in anagram:
                #init
                anagram[key] = []
            # add the word 
            anagram[key].append(word)

        # return list of values
        return list(anagram.values())