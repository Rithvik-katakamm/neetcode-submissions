class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Understand
        # input: m X n 2D integer array matrix -> [[int]]
        # contraints: each now is in acessding order 
        # the last element of each row is greater than the first number of the next row
        # this tells me ifi stiched all the lists together they would be in accending order 
        # expected return: boolean

        # code
        # name the numbers of rows and len of each row \
        rows = len(matrix)
        col = len(matrix[0])
        # set the low and high pointers
        low = 0 
        high = (rows * col) - 1
        # while low is less than or equal to high 
        while low <= high: 
            # calculate mid
            mid = (low + high) // 2 
            # find the row of mid 
            mid_row = mid // col
            # find th index of mid
            col_mid = mid % col
            # fi target - mid retrun true 
            if target > matrix[mid_row][col_mid]:
                low = (col * mid_row) + col_mid + 1
            # now if mid is greater than target
            elif matrix[mid_row][col_mid] > target:
                # move the high pointer to mid - 1 
                high = (col * mid_row) + (col_mid - 1)
            # or if mid is less tha target
            elif target == matrix[mid_row][col_mid]:
                return True
        # if we make it out of the loop. 
        return False

