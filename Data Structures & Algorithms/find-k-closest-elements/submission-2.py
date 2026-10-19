class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #can heap with nlogk, (dist, num)
        #given that its sorted in ascending order
        #bisect to find best starting pos, then return start:start+k
        n = len(arr)
        l, r = 0, n-k
        while l<r:
            mid = (l+r)//2
            if x-arr[mid]>arr[mid+k]-x:
                l = mid+1
            else:
                r = mid
        return arr[l:l+k]
