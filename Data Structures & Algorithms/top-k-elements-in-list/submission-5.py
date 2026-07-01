class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # init 
        hashy = {}

        # create a freq map for each number \
        for number in nums:
            hashy[number] = hashy.get(number, 0) + 1
        # bucket sort the frequnecies 
        freq_list = [[] for _ in range(len(nums)+1)]
        
        for number, count in hashy.items():
            freq_list[count].append(number)
        # walk the freq list backward and append k freq
        result = []
        for freq in range(len(freq_list) - 1, 0, -1):
            for n in freq_list[freq]:
                result.append(n)

            if len(result) == k:
                return result
        # return result 
        return result