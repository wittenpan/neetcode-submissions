class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        i = 0
        n = len(intervals)
        while i<n:
            cand_start, cand_end = intervals[i][0], intervals[i][1]
            while i+1<n and intervals[i+1][0]<=cand_end:
                cand_end = max(intervals[i+1][1],cand_end)
                i+=1
            res.append([cand_start,cand_end])
            i+=1
        return res