class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #monotonic stack question
        #keep (tmp, index) in stk. while temperatures[i]>stk[-1][0], we pop and assign the answer index
        #to i-index
        n = len(temperatures)
        ans = [0]*n
        stk = []
        for i, tmp in enumerate(temperatures):
            while stk and tmp>stk[-1][0]:
                _, index = stk.pop()
                ans[index] = i-index
            stk.append((tmp,i))
        return ans

