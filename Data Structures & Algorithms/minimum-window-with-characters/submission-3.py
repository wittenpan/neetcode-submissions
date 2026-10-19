class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = len(t)
        tCounts = Counter(t)
        if len(t)>len(s):
            return ""
        l = 0
        ans = (float('inf'),"")
        have = {}
        for r in range(len(s)):
            if have.get(s[r],0)<tCounts.get(s[r],0):
                need-=1
            have[s[r]] = have.get(s[r],0)+1
            while need==0:
                ans = min(ans, (r-l+1,s[l:r+1]))
                if have.get(s[l])<=tCounts.get(s[l],0):
                    need+=1
                have[s[l]]-=1
                l+=1
        return ans[1]

            
