class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # code 
        # example: [1,7,2,5,4,7,3,6]

        # init the pointer, area, max area
        left = 0
        right = len(heights) - 1
        min_height = 0 

        area,max_area = 0,0

        # dance with the 2 pointers
        while left < right: 
            # calculate breadth
            breadth = right - left
            # min height 
            min_height = min(heights[left], heights[right])
            # calculate area
            area = min_height * breadth
            # calc max area 
            max_area = max(area, max_area)
            # if the left wall is smaller than the right wall 
            if heights[left] < heights[right]: 
                # move to the next left wal
                left += 1
            # or if right wall is smaller than the left wall
            elif heights[left] > heights[right]:
                # move to the next right wall 
                right -= 1
            # edge case
            else: 
                left += 1

        # return max area
        return max_area  