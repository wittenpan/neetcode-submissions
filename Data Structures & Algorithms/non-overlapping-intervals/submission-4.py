class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key =lambda x:x[1])
        #greedily choose the interval with latest ending point
        i = 0
        n = len(intervals)
        prevEnd = intervals[0][1]
        res = 0
        for i in range(1, n):
            if prevEnd>intervals[i][0]:
                res+=1
            else:
                prevEnd = intervals[i][1]
        return res