class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #if greater, we move down, if less, we move left
        #another method is we do bs on n*m and convert to the indices.
        rows = len(matrix)
        cols = len(matrix[0])
        ptr = [0, cols-1]
        while ptr[0]<rows and ptr[1]>=0:
            mid = matrix[ptr[0]][ptr[1]]
            if mid==target:
                return True
            elif mid>target:
                ptr[1]-=1
            else:
                ptr[0]+=1
        return False