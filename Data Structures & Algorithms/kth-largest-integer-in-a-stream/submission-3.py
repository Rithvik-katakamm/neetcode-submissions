class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # init k
        self.k = k 
        # init nums
        self.nums = nums 
        # heapify nums
        heapq.heapify(self.nums) 
        # reduce the len of nums to k so root becomes kth largest element 
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        # add int to the stream
        heapq.heappush(self.nums, val)
        # make sure len remains k 
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        # return the root of the heap
        return self.nums[0]




    



        
