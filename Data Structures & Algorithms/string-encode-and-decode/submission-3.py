class Solution: 
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':          # find end of the length digits
                j += 1
            length = int(s[i:j])        # digits between i and '#'
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length          # jump past this string
        return res