class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        visited = [[False for _ in range(C)] for _ in range(R)]
        dirs = [(1,0),(-1,0),(0,-1),(0,1)]
        def dfs(r,c):
            visited[r][c] = True
            perim = 0
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if nr<0 or nr>=R or nc<0 or nc>=C: perim+=1
                elif grid[nr][nc]==0:
                    perim+=1
                elif not visited[nr][nc] and grid[nr][nc]==1:
                    visited[nr][nc] = True
                    perim+=dfs(nr,nc)
            return perim
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    return dfs(r,c)
