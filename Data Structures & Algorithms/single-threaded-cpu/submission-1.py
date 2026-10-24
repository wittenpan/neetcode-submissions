class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #shortest processing time : min heap keyed by (proc time, index)
        
        heap = []
        time = 0
        temp = []
        for i in range(len(tasks)):
            temp.append((tasks[i][0],tasks[i][1],i))
        temp.sort(key=lambda x: x[0])
        tasks = temp
        res = []
        i = 0
        while i < len(tasks) or heap:
            if i<len(tasks):
                time = max(time, tasks[i][0])
            #push avail tasks onto heap
            while i<len(tasks) and tasks[i][0]<=time:
                heapq.heappush(heap,(tasks[i][1],tasks[i][2]))
                i+=1
            if heap:
                processingTime, task = heapq.heappop(heap)
                time+=processingTime
                res.append(task)
        return res
            