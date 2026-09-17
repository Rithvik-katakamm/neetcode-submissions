class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # input: piles[i] = number of bananas, i = pile
        # h = no of hours to eat banana
        
        low =  1 
        high = max(piles)

        while low <= high:
            k = (low + high) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)

            if hours == h:
                return k 

            elif hours > h:
                low = k + 1

            else: 
                high = k - 1
