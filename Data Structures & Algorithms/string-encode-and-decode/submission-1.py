class Solution:

    def encode(self, strs: List[str]) -> str:
        # lets init a single string
        s = ''
        # lets walk through each word in the list
        for word in strs:
            # lets append the length, a # and the word to encode the string 
            s += str(len(word)) + '#' + word
        # lets return the encoded string. 
        return s 

    def decode(self, s: str) -> List[str]:
        # lets init the result list
        res = []
        # lets start at the start of the string
        i = 0 
        while i < len(s):
            j = i
            # lets move a second pointer till we hit #
            while s[j] != '#':
                j += 1 
            # lets extract the int
            length = int(s[i:j])
            # lets slice the list from the first letter to the last letter and append the word to res
            word = s[j+1:j+1+length] 
            res.append(word)
            # lets move i to the end of the word
            i = j + 1 + length

        # return the resulting list 
        return res