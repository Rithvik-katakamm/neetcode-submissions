class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # "understand
        # input: piles -> list, h -> int 
        # piles[i] is number of bananas, h i s time limit
        # output least time to eat the bananas (k)

        # code 
        # init low high pointers 
        low = 1
        high = max(piles)
        # init result = high
        result = high 
        # while low is less than or equal to high
        while low <= high: 
            # figure out what mid is 
            mid = (low + high) // 2 # eating rate 
            # then for mid how long does it take koko to eat all the bananas
            hours = sum(math.ceil(p/mid) for p in piles)
            # is this hours less than than h?  
            if hours <= h:
                # lowest time is now mid 
                result = mid 
                # move the high left 
                high = mid - 1 
                # if not 
            else:
                # move the eating speed up
                low = mid + 1
        # return the result 
        return result
            

        