class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a freq map 
        hashy = {}

        for i in nums:
            hashy[i] = hashy.get(i, 0) + 1 
        # bucket sort them 
        freq_list = [[] for _ in range(len(nums) + 1)]
        for number, count in hashy.items():
            freq_list[count].append(number)
        # walk the bicket sorted list from the reverse and append k results to the list 
        result = []
        for idx in range(len(freq_list) - 1, 0, -1):
            for num in freq_list[idx]:
                result.append(num)
                if len(result) == k:
                    return result 
 