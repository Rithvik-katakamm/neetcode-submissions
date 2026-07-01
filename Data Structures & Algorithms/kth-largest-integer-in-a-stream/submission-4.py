class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # init the inputs as a member variables 
        self.k = k 
        self.nums = nums 
        
        # heapify that shit and make sure the len remains k 
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(nums)
        
    def add(self, val):
        # append the new element 
        heapq.heappush(self.nums, val)
        # check the len 
        if len(self.nums) > self.k: 
            heapq.heappop(self.nums)
        # return the root which is so cooly the kth largest element 
        return self.nums[0]
        

    



        
