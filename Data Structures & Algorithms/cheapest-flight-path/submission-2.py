class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, p in flights:
            adj[u].append((v,p))
        #dijkstras with cost, k, node
        #allowed k+1 edges to explore
        pq = [(0,0,src)]
        best = [[float('inf') for _ in range(k+2)] for _ in range(n)]
        best[src][0] = 0
        while pq:
            cost, edges, node = heapq.heappop(pq)
            if cost>best[node][edges] or edges>k+1:
                continue
            for nei, weight in adj[node]:
                new_cost = cost+weight
                if edges<k+1 and new_cost<best[nei][edges+1]:
                    best[nei][edges+1]=new_cost
                    heapq.heappush(pq,(new_cost,edges+1,nei))
        ans = min(best[dst])
        return ans if ans!=float('inf') else -1
