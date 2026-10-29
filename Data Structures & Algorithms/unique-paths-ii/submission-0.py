class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        def dfs(r,c):
            if obstacleGrid[r][c]==1:
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            if r==m-1 and c==n-1:
                return 1
            res = 0
            if r+1<m:
                res+=dfs(r+1,c)
            if c+1<n:
                res+=dfs(r,c+1)
            memo[(r,c)] = res
            return res
        return dfs(0,0)