class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # code
        # init the number of rows, and len of each row
        m = len(matrix)
        n = len(matrix[0])
        # init the high low pointers 
        low = 0 
        high = (m*n) - 1
        # while thw low poointer is less than the high pointer
        while low <= high:
            # calculate mid
            mid = (low + high) // 2 
            # calculate which row mid is in
            mid_row = mid // n 
            # calc which index mid is at
            mid_idx = mid % n 
            # if mid number is less than the target
            if matrix[mid_row][mid_idx] < target:
                # move the low pointer up
                low = mid + 1
            # or if the mid number is greater than the target
            elif matrix[mid_row][mid_idx] > target:
                # move the high pointer down 
                high = mid - 1 
            # else if both are equal
            else: 
                # return true
                return True
        # if we make it out of thw loop then return False 
        return False 