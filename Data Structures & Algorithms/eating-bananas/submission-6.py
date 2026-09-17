class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # input: piles[i] = number of bananas, i = pile
        # h = no of hours to eat banana 

        low = 1
        high = max(piles)


        while low < high:
            k = (low + high) // 2
            hours = sum(math.ceil(p/k) for p in piles)


            if hours <= h:
                high = k 
            else:
                low = k + 1


        return low


            

