class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashy = {}
        for word in strs:
            key = self.freq_key(word)
            if key in hashy:
                hashy[key].append(word)
            else:
                hashy[key] = [word]

        return list(hashy.values())

    def freq_key(self, word: str):
        freq = {}

        for char in word:
            if char in freq:
                freq[char] += 1 
            else:
                freq[char] = 1 

        freq = sorted(freq.items())
        freq = tuple(freq)

        return freq


        