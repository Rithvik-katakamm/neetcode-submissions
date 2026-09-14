class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        low = 0 
        high = m * n 

        while low <= high: 
            mid = (low + high) // 2 

            row = mid // m 
            column = mid % n 
            
            if matrix[row][column] == target:
                return True 

            elif matrix[row][column] > target: 
                high = mid - 1 
                
            else: 
                low = mid + 1 

        return False 
