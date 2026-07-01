class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # lets make stones a max heap 
        stones = [-s for s in stones]
        heapq.heapify(stones)

        # lets smash some rocks together yeah
        while len(stones) > 1:
            # lets define x and y 
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            # now lets compare the 2 
            if x < y:
                heapq.heappush(stones, x - y )

        # return the result 
        return -stones[0] if stones else 0
