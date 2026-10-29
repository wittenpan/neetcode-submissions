class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #dp[i][j] = lip from that point
        rows = len(matrix)
        cols = len(matrix[0])
        memo = {}
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            res = 0
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and matrix[nr][nc]>matrix[r][c]:
                    res = max(res, dfs(nr,nc))
            memo[(r,c)] = 1+res
            return 1+res
        ans = 0
        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r,c))
            
        return ans