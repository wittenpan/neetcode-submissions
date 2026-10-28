class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #run bs on the answer space, grid[m-1][n-1] to max(grid)
        rows = len(grid)
        cols = len(grid[0])
        l, r = max(grid[rows-1][cols-1],grid[0][0]), max(max(row) for row in grid)
        def canReachBottom(time):
            q = deque([(0,0)])
            dirs = [(1,0),(-1,0),(0,1),(0,-1)]
            visited = set([(0,0)])
            while q:
                for _ in range(len(q)):
                    r,c = q.popleft()
                    if r==rows-1 and c==cols-1:
                        return True
                    for dr, dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and grid[nr][nc]<=time:
                            visited.add((nr,nc))
                            q.append((nr,nc))
            return False
        ans = 0
        while l<=r:
            mid = (l+r)//2
            if canReachBottom(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans
                
                    
