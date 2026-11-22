class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # bucket sort 


        freq_map = {}
        
        for i in nums:
            if i in freq_map:
                freq_map[i] += 1 
            else:
                freq_map[i] = 1 

        bucket = [[] for _ in range(len(nums)+1)]

        for num, freq in freq_map.items():
            bucket[freq].append(num)

        res = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
            if len(res) == k:
                return res 

        