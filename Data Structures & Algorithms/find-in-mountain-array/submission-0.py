class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        #you can find pivot (the peak) and bs both sides. 
        l, r = 0, mountainArr.length()-1
        cache = {}
        peak = 0
        while l<=r:
            m = (l+r)//2
            if m in cache: midElement = cache[m]
            else: 
                midElement = mountainArr.get(m)
                cache[m] = midElement
            if l in cache: leftElement = cache[l]
            else: 
                leftElement = mountainArr.get(l)
                cache[l] = leftElement
            if r in cache: rightElement = cache[r]
            else: 
                rightElement = mountainArr.get(r)
                cache[r] = rightElement
            if m+1 in cache: midRight = cache[m+1]
            else: 
                midRight = mountainArr.get(m+1)
                cache[m+1] = midRight
            if midElement>midRight:
                peak = m
                r = m-1
            else:
                l = m+1
        if cache[peak]==target:
            return peak
        l, r = 0, peak-1
        while l<=r:
            m = (l+r)//2
            if m in cache: midElement = cache[m]
            else: 
                midElement = mountainArr.get(m)
                cache[m] = midElement
            if midElement==target:
                return m
            elif midElement<target:
                l = m+1
            else:
                r = m-1
        l, r = peak+1, mountainArr.length()-1
        while l<=r:
            m = (l+r)//2
            if m in cache: midElement = cache[m]
            else: 
                midElement = mountainArr.get(m)
                cache[m] = midElement
            if midElement==target:
                return m
            elif midElement>target:
                l = m+1
            else:
                r = m-1
        return -1