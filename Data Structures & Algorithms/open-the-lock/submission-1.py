class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #minimum total turns, so bfs.
        visited = set(deadends)
        if "0000" in visited:
            return -1
        q = deque([("0000",0)])
        #neis within one turn
        def neighbors(node):
            res = []
            arr = [char for char in node]
            for i in range(4):
                copy1 = arr.copy()
                copy2 = arr.copy()
                num1 = int(node[i])+1
                num2 = int(node[i])-1
                if num2==-1:
                    copy2[i]="9"
                else:
                    copy2[i]=str(num2)
                if num1==10:
                    copy1[i]="0"
                else:
                    copy1[i]=str(num1)
                res.append("".join(copy1))
                res.append("".join(copy2))
            return res
        while q:
            for _ in range(len(q)):
                node, dist = q.popleft()
                if node==target: return dist
                for nei in neighbors(node):
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, dist+1))
        return -1
                
