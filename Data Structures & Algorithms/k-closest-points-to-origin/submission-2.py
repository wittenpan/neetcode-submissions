class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = (x**2)+(y**2)
            heapq.heappush_max(heap,(distance, x, y))
            if len(heap)>k:
                heapq.heappop_max(heap)
        res = []
        while heap:
            _, x, y = heapq.heappop_max(heap)
            res.append([x,y])
        return res        