class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        #range sum queries with static obviously prefix sum, but how
        self.prefix = [[0 for _ in range(self.cols+1)] for _ in range(self.rows+1)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.prefix[i+1][j+1] = self.prefix[i][j+1]+self.prefix[i+1][j]+self.matrix[i][j]-self.prefix[i][j]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+1][col2+1]-self.prefix[row1][col2+1]-self.prefix[row2+1][col1]+self.prefix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)