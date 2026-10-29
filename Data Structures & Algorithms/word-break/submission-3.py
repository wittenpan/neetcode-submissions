class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i==len(s):
                return True
            res = False
            for word in wordDict:
                if s[i:i+len(word)]==word:
                    res|=dfs(i+len(word))
            memo[i] = res
            return res
        return dfs(0)