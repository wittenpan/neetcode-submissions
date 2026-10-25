class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        #same idea as reorg string, we want to optimally assign 
        #based on remaining freqs. if prev 2 are same char, then we pop again (if exist)
        #and put that one in
        heap = []
        if a>0:
            heap.append((a,'a'))
        if b>0:
            heap.append((b,'b'))
        if c>0:
            heap.append((c,'c'))
        heapq.heapify_max(heap)
        res = []
        while heap:
            cnt, letter = heapq.heappop_max(heap)
            if len(res)>=2 and letter==res[-1]==res[-2]:
                if heap:
                    cnt2, letter2 = heapq.heappop_max(heap)
                    res.append(letter2)
                    cnt2-=1
                    if cnt2>0:
                        heapq.heappush_max(heap,(cnt2,letter2))
                else:
                    break
                heapq.heappush_max(heap, (cnt,letter))
            else:
                res.append(letter)
                cnt-=1
                if cnt>0:
                    heapq.heappush_max(heap, (cnt,letter))
        return "".join(res)
