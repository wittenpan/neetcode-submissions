class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #optimal is choose the most freq chr
        seeing = {}
        l = 0
        ans = 0
        most_freq = 0
        for r in range(len(s)):
            #how to find most freq c?
            seeing[s[r]] = seeing.get(s[r],0)+1
            most_freq = max(most_freq, seeing[s[r]])
            while (r-l+1)-most_freq>k:
                seeing[s[l]]-=1
                l+=1
            ans = max(ans, r-l+1)
        return ans
