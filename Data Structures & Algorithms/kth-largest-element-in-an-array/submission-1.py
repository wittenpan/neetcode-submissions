class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #sorting is easy and is nlogn
        #we can convert to heap and keep size k
        #adding and popping nlogk, minheap
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]
