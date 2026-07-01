class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: 
            return []

        # define the data structures needed (hashmap and heap)
        hashy = {}
        heap = []
        # lets create a frequency map from the nums list here
        for n in nums:
            if n in hashy:
                hashy[n] += 1 
            else: 
                hashy[n] = 1
        
        # now push the freq,value pair into the heap sort them in log n time 
        for value, freq in hashy.items():
            heapq.heappush(heap, (freq, value))

            # reduce the len of the heap to the values we need 
            if len(heap) > k:
                heapq.heappop(heap)
        
        # return the values of the heap 
        return [element for freq, element in heap]