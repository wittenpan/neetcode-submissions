class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #can dfs, not seeing a way to precompute
        adj = defaultdict(list)
        for i, (a,b) in enumerate(equations):
            adj[a].append((b,values[i]))
            adj[b].append((a,1/values[i]))
        res = []
        for u, v in queries:
            stk = [(u,1)]
            found = False
            visited = set()
            if u not in adj or v not in adj:
                res.append(-1)
                continue
            while stk:
                node, currval = stk.pop()
                if node==v:
                    res.append(currval)
                    found = True
                    break
                for nei, val in adj[node]:
                    if nei not in visited:
                        stk.append((nei,currval*val))
                        visited.add(nei)
            if not found:
                res.append(-1)
        return res
