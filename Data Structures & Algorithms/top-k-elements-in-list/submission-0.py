class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = self.freq_count(nums)

        # access the nums in the list and push them into the heap 
        heap = []
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [element for freq, element in heap]
        
    def freq_count(self, arr): 
        freq_map = {}
        for n in arr:
            if n in freq_map:
                freq_map[n] += 1 
            else: 
                freq_map[n] = 1 
            
        return freq_map

        