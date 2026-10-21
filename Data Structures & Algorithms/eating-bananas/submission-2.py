class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #ub on bph will be max of piles, which lets you finish inexactly h hours based on constraints
        #lb will be 1
        l, r = 1, max(piles)
        def check(bph):
            needed_h = 0
            for banana in piles:
                needed_h += math.ceil(banana/bph)
            #true
            return needed_h<=h
        ans = r
        while l<=r:
            mid = (l+r)//2
            if check(mid):
                r = mid-1
                ans = mid
            else:
                l = mid+1
        return ans
