class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #we keep a heap of size k.
        #i.e. if 1,2,3,3 arrive and k = 3
        #[2,3,3]
        #we add to a min heap, and pop [0] if size>k, then root is kth largest
        self.heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.heap,num)
            if len(self.heap)>k:
                heapq.heappop(self.heap)
    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        if len(self.heap)>self.k:
            heapq.heappop(self.heap)  
        return self.heap[0]  