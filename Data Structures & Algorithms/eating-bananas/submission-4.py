class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Understand
        # input -> piies - list[int], h -> int 
        # piles is a list of piles of bananas, where, piles[i] is no of bananas 
        # h is the numbers of hours one has to eat all the bananas in a pilr
        # eating rate per hour = k 
        # expected return min value of k such that we can eat all the bananas in h time 

        # code
        # set the lowest rate and the highest 
        low = 1 
        high = max(piles)
        # while low is less than or equal to high
        while low <= high:
            hours = 0 
            # calculate eating rate k 
            k = (low + high) // 2 
            # calculate total hours with current rate of eating 
            hours += sum(math.ceil(p/k) for p in piles)
            # if the total hours is less than or equal to h
            if hours <= h:
                res = k
                # we move the right pointer left
                high = k - 1
            # if no
            else:
                # move left pointer right
                low = k + 1 

        return res