class Solution:

    def arrange(self, word):
        return "".join(sorted(word))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}
        
        #building the hashmap
        for word in strs:

            if self.arrange(word) in hashmap:
                hashmap[self.arrange(word)].append(word)

            else:
                hashmap[self.arrange(word)] = [word]

        #the result
        return list(hashmap.values())

        