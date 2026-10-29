class Solution:
    def tribonacci(self, n: int) -> int:
        if n==1 or n==2:
            return 1
        if n==0: return 0
        #t0=0, t1=1, t2 = 1
        prevprevprev = 0
        prevprev = 1
        prev = 1
        curr = -1
        for i in range(2, n):
            curr= prevprevprev+prevprev+prev
            prevprevprev = prevprev
            prevprev = prev
            prev = curr
        return curr