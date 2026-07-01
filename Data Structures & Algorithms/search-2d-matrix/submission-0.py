class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Understand
        # input: m X n 2D integer array matrix -> [[int]]
        # contraints: each now is in acessding order 
        # the last element of each row is greater than the first number of the next row
        # this tells me ifi stiched all the lists together they would be in accending order 
        # expected return: boolean

        # lets do the brute force way first 
        
        # code
        # loop through the lists in the list 
        for i in matrix:
            # loop through the numbers in the list 
            for j in i:
                # if we find the target 
                if j == target:
                    # return true 
                    return True
        # if we exit return false 
        return False
