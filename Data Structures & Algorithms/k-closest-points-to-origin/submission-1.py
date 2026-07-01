class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Understand: 
        # input, points => a 2d array, k => a limit of points to return 
        # expected output: k number of points closest to the origin 

        # Approuch: 
        # cacluate the euclidian distance for each point 
        # append the euclidian distance along with the points to a heap 
        # make sure the len never exceeds k 
        # extract the points from the min heap corrilating the min distance 

        # code:
        # init a heap 
        heap = [] 
        # loop through the points list whilst unpacking 
        for x, y in points:
            # calculat e distance  
            dis = -(x**2 + y**2)
            # push it into the heap 
            heapq.heappush(heap, (dis, x, y))
            # keep the length below k 
            if len(heap) > k:
                heapq.heappop(heap)

        # return the points closest to the origin 
        return [[x,y] for dis, x, y in heap]