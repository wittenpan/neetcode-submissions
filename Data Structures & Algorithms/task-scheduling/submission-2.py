class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #ideally you want to take task with most counts first
        cts = Counter(tasks)
        cts = [count for count in cts.values()]
        print(cts)
        heapq.heapify_max(cts)
        cooldown = deque()
        time = 0
        while cts or cooldown:
            if not cts:
                time = max(time, cooldown[0][0])
            #pop out of cooldown queue
            while cooldown and cooldown[0][0]<=time:
                _, ct = cooldown.popleft()
                heapq.heappush_max(cts,ct)
            #process task
            if cts:
                taskcount = heapq.heappop_max(cts)
                taskcount-=1
                if taskcount>0:
                    cooldown.append((time+n+1,taskcount))
            time+=1
        return time
