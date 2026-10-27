class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #No cycles.
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set([0])
        q = deque([0])
        parent = {0:-1}
        while q:
            node = q.popleft()
            for nei in adj[node]:
                if nei in visited and nei!=parent[node]:
                    return False
                elif nei not in visited:
                    visited.add(nei)
                    parent[nei] = node
                    q.append(nei)
        return len(visited)==n