class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #kadanes algorithm but with a negative number as well 
        maxPro = float('-inf')
        curPro = 1
        currNegPro = 1
        for num in nums:
            tmp = curPro*num
            curPro = max(num*curPro, num*currNegPro, num)
            currNegPro = min(tmp, num*currNegPro, num)
            maxPro = max(curPro, maxPro)
        return maxPro


