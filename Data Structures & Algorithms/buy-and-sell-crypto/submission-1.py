class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #n^2 obvious but what are constraints
        #we want highest in future
        #if we can get a lower price we take it
        lowest = prices[0]
        ans = 0
        for i in range(1,len(prices)):
            ans = max(prices[i]-lowest,ans)
            if prices[i]<lowest:
                lowest = prices[i]
        return ans