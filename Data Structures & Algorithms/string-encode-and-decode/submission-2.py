class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        # parse the list
        for word in strs:
            # append the len(word) + # +  word to a single string 
            res += str(len(word)) + '#' + word
        # return the single string 
        return res 

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0
        j = 0 
        
        # parse through the chars 
        while i < len(s):
                # slice the list according to the start and end length
            while s[j]!= '#':
                j += 1 
                # example: s = 4#word3#app
            length = int(s[i:j]) 
            i = j + 1 
            word = s[i: j + 1 + length]
            i = j + 1 + length 
            j = i
            # append the word to a new list 
            res.append(word) 
        # return the new list 
        return res


