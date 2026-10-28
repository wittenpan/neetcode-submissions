class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #min spanning tree
        #prims or kruskals
        #n^2 to build adj list
        #manhattan dist from origin always the same - prev
        n = len(points)
        visited = [False] * n
        dist = [float('inf')] * n
        node, res, edges = 0,0,0
        while edges<n-1:
            visited[node]=True
            nextNode = -1
            x1, y1 = points[node]
            for i in range(n):
                if not visited[i]:
                    x2, y2 = points[i]
                    cost = abs(x1-x2)+abs(y1-y2)
                    dist[i] = min(dist[i],cost)
                    if nextNode==-1 or dist[i]<dist[nextNode]:
                        nextNode = i
            res+=dist[nextNode]
            node = nextNode
            edges+=1
        return res