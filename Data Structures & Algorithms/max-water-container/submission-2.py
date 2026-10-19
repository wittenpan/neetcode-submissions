class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #we can model the height between any two bars as min(l,r)*(r-l)
        #then with two pointers we move in.
        #only move in the one that increases it more, i.e. 
        ans = 0
        l, r = 0, len(heights)-1
        while l<r:
            ans = max(ans, min(heights[l],heights[r])*(r-l))
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return ans