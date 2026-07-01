class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # UNDERSTAND:
        # input: stones -> list 
        # each value corr to the weight of ith stone 
        # this problem is us running a simulation 
        # we have 2 stones x and y which are the haviest in the list  
        # upon smash 
        # - if x == y, both are destroyed 
        # - if x < y, x is destroyed and y = y - x. vise versa

        # APPROUCH (+ data structure shopping)
        # compare the top2 elements 
        # if both are same remove both of them 
        # if they are not append the bigger num - the smaller num 
        # do this till the len of the list is one
        # data structure of choice = max heap (negative min heap) 
        
        # Code: 
        # make stones a max heap 
        stones = [-s for s in stones]
        heapq.heapify(stones)
        # loop through heap 
        while len(stones) > 1:
            # pop 2 nums
            x = heapq.heappop(stones)
            y = heapq.heappop(stones) 
            # compare them 
            if x < y:
                # push back the difference if one is greater than the other 
                heapq.heappush(stones, x - y)
        # return the num left over in the heap
        return -stones[0] if stones else 0


