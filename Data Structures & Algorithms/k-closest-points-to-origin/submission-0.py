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
        # loop throight points
        for x,y in points:
            # caluclate distance
            dist = -(x**2 + y**2)
            # append distance, x, y to the heap
            heapq.heappush(heap, (dist, x, y)) 
            # make sure the len remains under k 
            if len(heap) > k: 
                heapq.heappop(heap)
        # return the points as a list of lists 
        return [[x,y] for dist, x, y in heap]
