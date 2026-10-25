class Solution:
    def reorganizeString(self, s: str) -> str:
        #like task scheduler
        #we want to take the most frequent and 2nd most freq at once.
        chars = Counter(s)
        heap = []
        for k, v in chars.items():
            heapq.heappush_max(heap,(v,k))
        print(heap)
        res = []
        while heap:
            cnt1, chr1 = heapq.heappop_max(heap)
            cnt2, chr2 = 0, None
            if heap:
                cnt2, chr2 = heapq.heappop_max(heap)
            cnt1-=1
            cnt2-=1
            res.append(chr1)
            if chr2: res.append(chr2)
            if cnt1>0:
                heapq.heappush_max(heap,(cnt1,chr1))
            if cnt2>0:
                heapq.heappush_max(heap,(cnt2,chr2))
        for i in range(len(res)-1):
            if res[i]==res[i+1]:
                return ""
        return "".join(res)