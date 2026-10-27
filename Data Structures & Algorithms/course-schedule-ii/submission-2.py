class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #we want to generate a topological sort, ideally with kahns
        indegree = [0]*numCourses
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            indegree[u]+=1
            adj[v].append(u)
        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return res if len(res)==numCourses else []