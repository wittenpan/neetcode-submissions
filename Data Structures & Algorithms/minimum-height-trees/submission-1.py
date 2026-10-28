class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #brute force for i in range(n):
        #heights = {} height -> [roots]
        #keep minheight var
        #at end return heights[minheight]
        #n^2
        #topological removal of leaves, until <=2 left. trim leaves 
        if n==1:
            return [0]
        degree= [0]*n
        adj = [[] for _ in range(n)]
        remaining = n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u]+=1
            degree[v]+=1
        q = deque()
        for i in range(n):
            if degree[i]==1:
                q.append(i)
        while q:
            if remaining<=2:
                return list(q)
            for _ in range(len(q)):
                node = q.popleft()
                remaining-=1
                for nei in adj[node]:
                    degree[nei]-=1
                    if degree[nei]==1:
                        q.append(nei)
        
        
                