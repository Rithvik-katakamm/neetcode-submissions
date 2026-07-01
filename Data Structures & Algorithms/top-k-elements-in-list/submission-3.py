class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashy = {}
        # create a freq map 
        for i in nums:
            hashy[i] = hashy.get(i,0) + 1
        # create and build a freq bucket
        freq_bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in hashy.items():
            freq_bucket[value].append(key)
        # walk the freq bucket from the back and append nums until we hit len k 
        result = []
        for i in range(len(freq_bucket) - 1, 0, -1):
            for number in freq_bucket[i]:
                result.append(number)
                if len(result) == k:
                    return result