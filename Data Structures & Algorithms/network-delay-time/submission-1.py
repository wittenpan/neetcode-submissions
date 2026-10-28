class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #is this dijkstras as well? i.e. max of best[all]??
        
        adj = [[] for _ in range(n)]
        best = [float('inf') for _ in range(n)]
        best[k-1] = 0
        for u, v, t in times:
            adj[u-1].append((v-1,t))
        pq = [(0,k-1)] #cost, node
        while pq:
            cost, node = heapq.heappop(pq)
            if cost>best[node]:
                continue
            for nei, weight in adj[node]:
                next_cost = weight+cost
                if next_cost<best[nei]:
                    heapq.heappush(pq,(next_cost,nei))
                    best[nei] = next_cost
        print(best)
        ans = max(best)
        return ans if ans!=float('inf') else -1
        
