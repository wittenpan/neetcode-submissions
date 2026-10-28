class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #dijkstras (cost, r, c)
        rows = len(heights)
        cols = len(heights[0])
        best = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        best[0][0] = 0
        pq = [(0, 0, 0)] # curr effort
        dirs = [(1,0), (-1, 0), (0,1), (0,-1)]
        while pq:
            cost, r, c = heapq.heappop(pq)
            if r==rows-1 and c==cols-1:
                return cost
            if cost>best[r][c]:
                continue
            for dr, dc in dirs:
                nr, nc = dr+r, dc+c
                if 0<=nr<rows and 0<=nc<cols:
                    max_effort = max(abs(heights[r][c]-heights[nr][nc]), cost)
                    if max_effort<best[nr][nc]:
                        heapq.heappush(pq, (max_effort,nr,nc))
                        best[nr][nc] = max_effort
        return float('inf')