class Solution:
    def validPalindrome(self, s: str) -> bool:
        loop_string = s.lower()
        s = []
        for char in loop_string:
            if char.isalnum():
                s.append(char)
        deletionUsed = False
        l, r = 0, len(s)-1
        while l<r:
            if s[l]!=s[r]:
                deletionUsed = True
                break
            l+=1
            r-=1
        if not deletionUsed:
            return True
        else:
            rightl, rightr = l, r-1
            leftl, leftr = l+1, r
            failed = 0
            while rightl<rightr:
                if s[rightl]!=s[rightr]:
                    failed+=1
                    break
                rightl+=1
                rightr-=1
            while leftl<leftr:
                if s[leftl]!=s[leftr]:
                    failed+=1
                    break
                leftl+=1
                leftr-=1
            return failed!=2
            
