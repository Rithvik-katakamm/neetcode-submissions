class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Understand: \
        # input: unsort_nums -> list, k -> int 
        # expected output: kth largest element in the sorted version of the lit 
        # do it without sorting  

        # Approuc: 
        # since they are asking for the kth largest element lets use a max heap
        # we will start by heapifying the list (negate the list vals first)
        # then we will keep the length of the heap at k so the root will represent the kth largest element 
        
        # Code:
        # init a heap 
        heap = []
        # loop through nums where each val is negative
        for n in nums:
            # push this to the heap:
            heapq.heappush(heap, n) 
            # make sure the len of the heap is under k
            if len(heap) > k:
                heapq.heappop(heap)
        # return root value of the heap
        return heap[0]