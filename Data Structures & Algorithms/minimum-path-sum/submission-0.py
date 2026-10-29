class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #only down or right
        rows = len(grid)
        cols = len(grid[0])
        memo = {}
        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            if r==rows-1 and c==cols-1:
                return grid[r][c]
            res = float('inf')
            if r+1<rows:
                res = min(res, dfs(r+1,c))
            if c+1<cols:
                res = min(res, dfs(r,c+1))
            memo[(r,c)] = grid[r][c]+res
            return memo[(r,c)]
        return dfs(0,0)