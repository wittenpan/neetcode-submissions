class MedianFinder:

    def __init__(self):
        #keep two heaps, a min and max heap.
        #right heap is minheap, left heap is maxheap.
        #we push to rightheap, and if len(rightheap)>len(leftheap)+1, 
        #we pop from rightheap and push onto 
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        #when we push to the minheap, we want to first check if the minheap element is less than
        #the pushed element so that we move from swap then push
        #we want to maintain invariant that everything in the minheap>everything in maxheap.
        if self.minHeap and num>self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush_max(self.maxHeap, num)
        if len(self.maxHeap) > len(self.minHeap)+1:
            heapq.heappush(self.minHeap, heapq.heappop_max(self.maxHeap))
        if len(self.minHeap) > len(self.maxHeap)+1:
            heapq.heappush_max(self.maxHeap, heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap)>len(self.minHeap):
            return self.maxHeap[0]
        if len(self.minHeap)>len(self.maxHeap):
            return self.minHeap[0]
        return (self.maxHeap[0]+self.minHeap[0])/2.0
        