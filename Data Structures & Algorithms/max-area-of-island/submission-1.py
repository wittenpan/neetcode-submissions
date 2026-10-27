class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        dirs = [(1,0),(-1,0),(0,-1),(0,1)]
        def dfs(r, c):
            visited[r][c] = True
            res = 1
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    res+=dfs(nr,nc)
            return res
        best = 0
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]==1 and visited[r][c]==False):
                    best = max(best,dfs(r,c))
        return best