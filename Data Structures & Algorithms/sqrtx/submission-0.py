class Solution:
    def mySqrt(self, x: int) -> int:
        #root will be 
        l, r = 0, x
        ans = 0
        while l<=r:
            mid = (l+r)//2
            if mid**2>x:
                
                r = mid-1
            else:
                ans = mid
                l = mid+1
        return ans