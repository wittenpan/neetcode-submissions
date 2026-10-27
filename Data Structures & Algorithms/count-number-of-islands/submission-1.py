class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        dirs = [(1,0),(-1,0),(0,-1),(0,1)]
        def dfs(r, c):
            visited[r][c] = True
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=="1" and not visited[nr][nc]:
                    visited[nr][nc] = True
                    dfs(nr,nc)
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]=="1" and visited[r][c]==False):
                    dfs(r,c)
                    islands+=1
        return islands