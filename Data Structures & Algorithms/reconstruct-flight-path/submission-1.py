class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #construct eulerian path
        #use every edge at least once from JFK
        #guarenteed eulerian path, and we know the start point (JFK)
        #hierholzer's algorithm
        adj = defaultdict(list)
        tickets.sort(reverse=True)
        for u, v in tickets:
            adj[u].append(v)
        currPath = ["JFK"]
        circuit = []
        while len(currPath)>0:
            currNode = currPath[-1]
            #check if remaining node in adj list
            if len(adj[currNode])>0:
                #find next node in path
                nextNode = adj[currNode].pop()
                #push to the currPath stack
                currPath.append(nextNode)
            else:
                #no remaining neigbors, we push to circuit
                circuit.append(currPath.pop())
        circuit.reverse()
        return circuit
            

        