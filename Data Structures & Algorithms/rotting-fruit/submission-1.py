class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #keep ct of non rotten fruit at start. then while multi source bfs
        #q... we radiate outwards, and if rotten!=nonrotten fruit at start return -1 else return minutes
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]==2):
                    q.append((r,c))
        mins = 0
        while(q):
            for _ in range(len(q)):
                row, col = q.popleft()
                if row + 1 < rows and grid[row + 1][col] == 1:
                    q.append((row + 1, col))
                    grid[row+1][col]=2
                if row - 1 >= 0 and grid[row - 1][col] == 1:
                    q.append((row - 1, col))
                    grid[row-1][col]=2
                if col + 1 < cols and grid[row][col + 1] == 1:
                    q.append((row, col + 1))
                    grid[row][col+1]=2
                if col - 1 >= 0 and grid[row][col - 1] == 1:
                    q.append((row, col - 1))
                    grid[row][col-1]=2
            if(len(q)>0):
                mins+=1
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]==1):
                    return -1
        return mins