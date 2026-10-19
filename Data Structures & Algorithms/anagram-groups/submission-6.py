class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # input shape:
        # strs = [strs, strs, strs]

        # code
        hashy = {}
        result = []

        for string in strs:
            # init 
            chars = {}
            #compute freq map for string†
            for s in string:
                if s in chars:
                    chars[s] += 1 
                else:
                    chars[s] = 1
            key = tuple(sorted(chars.items()))    


            if key in hashy:
                hashy[key].append(string)
            else:
                hashy[key] = [string]

        for i in hashy.values():
            result.append(i)


        return result 
                


        