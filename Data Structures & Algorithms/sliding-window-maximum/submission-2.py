class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #can lazy delete from heap
        heap = []
        heapq.heapify_max(heap)
        seeing = dict()
        for i in range(k):
            heapq.heappush_max(heap,nums[i])
            seeing[nums[i]] = seeing.get(nums[i],0)+1
        ans = [heap[0]]
        l = 0
        for i in range(k, len(nums)):
            seeing[nums[i]] = seeing.get(nums[i],0)+1
            seeing[nums[l]]-=1
            if seeing[nums[l]]==0:
                del seeing[nums[l]]
            heapq.heappush_max(heap,nums[i])
            while heap and heap[0] not in seeing:
                heapq.heappop_max(heap)
            ans.append(heap[0])
            l+=1
        return ans

