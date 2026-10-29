class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        def dfs(i, M):
            if i==len(piles):
                return 0
            if (i, M) in memo:
                return memo[(i, M)]
            res = float('-inf')
            taken = 0
            for j in range(i, min(len(piles),i+(2*M))):
                taken+=piles[j]
                res = max(res, taken-dfs(j+1, max(M, j-i+1)))
            memo[(i,M)] = res
            return res
        return (sum(piles)+dfs(0, 1))//2