class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profit = w
        projects = sorted(zip(capital, profits))
        i = 0
        heap = []
        taken = 0
        while taken<k:
            while i<len(projects) and profit>=projects[i][0]:
                heapq.heappush_max(heap,projects[i][1])
                i+=1
            if heap:
                consuming = heapq.heappop_max(heap)
                profit+=consuming
            taken+=1
        return profit