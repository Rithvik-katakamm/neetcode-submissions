class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # understand 
        # input -> heights = []
        # output -> max_area = int 

        # code 
        # init 2 pointers 
        left = 0 
        right = len(heights) - 1
        max_area = 0
        #while left is less than right 
        while left < right: 
            # calc area 
            length = min(heights[left], heights[right])
            breadth = right - left
            area = length * breadth 
            # compare to current max 
            max_area = max(area,max_area)
            # move the smaller pointer
            if heights[left] < heights[right]:
                left += 1 
            else:
                right -= 1
        # return m
        return max_area
