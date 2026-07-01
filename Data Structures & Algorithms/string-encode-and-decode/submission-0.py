class Solution:
    # UNDERSTAND 
    # write an encode function that encodes a string 
    # wrtie a functions that decodes the encoded stromg back to the original
    

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            new_char = str(len(s)) + '#' + s
            res.append(new_char)

        return ''.join(res)

        
    def decode(self, s: str) -> List[str]:
        res = [] 
        i = 0 

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1 

            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]
            res.append(word)

            i = j + 1 + length 

        return res

