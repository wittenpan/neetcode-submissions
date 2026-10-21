class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(nums2)<len(nums1):
            A, B = nums2, nums1
       
        total = (len(A)+len(B))
        half = total//2
        l, r = 0, len(A)-1
        while True:
            i = (l+r)//2
            B_partition = half-i-2
            Aleft = A[i] if i>=0 else float("-inf")
            Aright = A[i+1] if i+1<len(A) else float('inf')
            Bleft = B[B_partition] if B_partition>=0 else float("-inf")
            Bright = B[B_partition+1] if B_partition+1<len(B) else float("inf")
            #dont check aleft and aright and b because sorted order
            if Aleft<=Bright and Bleft<=Aright:
                if total%2:
                    return min(Aright, Bright)
                return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft>Bright:
                r = i-1
            else:
                l = i+1