class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #is this not find the nearest min height to the left and right
        minToLeft = [-1]* len(heights)
        minToRight = [len(heights)]* len(heights)
        #monotonic stack for both left and right
        stk = []
        for i, num in enumerate(heights):
            while stk and num<stk[-1][0]:
                height, index = stk.pop()
                minToRight[index] = i
            stk.append((num,i))
        stk = []
        for i in range(len(heights)-1,-1,-1):
            while stk and heights[i]<stk[-1][0]:
                height, index = stk.pop()
                minToLeft[index] = i
            stk.append((heights[i],i))
        ans = 0
        for i in range(len(heights)):
            width = minToRight[i]-minToLeft[i]-1
            ans = max(ans, width*heights[i])
        return ans