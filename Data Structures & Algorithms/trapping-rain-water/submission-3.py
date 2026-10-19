class Solution:
    def trap(self, height: List[int]) -> int:
        #for each position i, the water trapped there is the min(highest to the left 
        #, highest to the right) - height at that position
        n = len(height)
        ans = 0
        preMaxes = [0] * n
        postMaxes = [0] * n
        preMaxes[0] = height[0]
        postMaxes[-1] = height[-1]
        for i in range(1,n):
            preMaxes[i] = max(height[i],preMaxes[i-1])
        for i in range(n-2, -1, -1):
            postMaxes[i] = max(height[i],postMaxes[i+1])
        for i in range(n):
            ans+=min(preMaxes[i],postMaxes[i])-height[i]
        return ans
