class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # define the heap and a hashmap 
        hashy = {} 
        heap = []
        
        # lets first create a freq map 
        for n in nums:
            if n in hashy:
                hashy[n] += 1
            else:
                hashy[n] = 1

        # now lets parse through the freq map and append the (freq,num) in a min heap
        for num, freq in hashy.items():
            heapq.heappush(heap, (freq, num))

            # lets also make sure the heap is under k no of values 
            if len(heap) > k:
                heapq.heappop(heap)

        # return a list of the top k elements
        return [element for freq, element in heap]