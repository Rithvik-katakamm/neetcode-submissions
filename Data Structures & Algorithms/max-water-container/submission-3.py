class Solution:
    def maxArea(self, heights: List[int]) -> int:
       # Understand:
       # input - heights
       # each number represents a height 
       # find the max amount of water that can be stored. 

       # Approuch:
       # lets use the 2 pointer approuch for efficency 
       # lets caclulate the area for the current 2 bars we are pointing too using the min of the 2 heights
       # lets move the pointer pointing to the smaller bar 
       # keep track of the max area the entire time 
       
       # code:
       # init the 2 pointers, max area, area  
       left, right, max_area, area = 0,len(heights)-1,0,0
       # sweep through the list
       while left < right:
           # calc breadth, area, max area, min_hi
           breadth = right - left
           min_hi = min(heights[left], heights[right])
           area = min_hi * breadth 
           max_area = max(area, max_area)
           # move the smaller pointer# 
           if heights[left] < heights[right]:
               left += 1
           elif heights[left] > heights[right]:
               right -= 1
           else:
               left += 1  
       # return max area 
       return max_area
 