class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(cap):
            curr = cap
            days_needed = 1
            for weight in weights:
                if curr<weight:
                    curr = cap
                    days_needed+=1
                curr-=weight
            return days_needed<=days
        l, r = max(weights), sum(weights)
        ans = 0
        while l<=r:
            mid = (l+r)//2
            if check(mid):
                r = mid-1
                ans = mid
            else:
                l = mid+1
        return ans