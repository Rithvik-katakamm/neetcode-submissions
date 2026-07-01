class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Understand:
        # input - heights
        # pick the container with the mnost water (area)
        # area = height x breadth 
        # breath here would be step count
        # output - max area 

        # approuch
        # so we have to calculate area at every point 
        # this means the max height can onlu be as much as the bar we are calculating from 
        # breadth is step count 
        # lets first use the curr height as max possible height
        # but the height used for calculation will be the one that is smallest 
        # and breadth keeps growing per step count...holy fuck i think i solved it

        # code
        # init breadth, area, max area
        breadth = 0 
        max_area, area = 0, 0
        # outer loop: till fixed height in range of len(heigths)
        for height_idx in range(0, len(heights)): 
            # init breadth 
            breadth = 0 
            # inner: till curr height is in range of len(heights)
            for curr_height_idx in range(height_idx + 1, len(heights)):
                # increment breadth 
                breadth += 1 
                # which height is smaller?
                min_height = min(heights[height_idx], heights[curr_height_idx])
                # area = height x b=readth
                area = min_height * breadth 
                # keep track of max height 
                max_area = max(area, max_area)
        # return max height 
        return max_area