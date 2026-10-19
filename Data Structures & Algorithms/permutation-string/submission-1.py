class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1chars = [0]*26
        #preprocess s1 to s1chars arry, check in windows of s1 len in s2
        for c in s1:
            s1chars[ord(c)-ord('a')]+=1
        s2window = [0]*26
        for i in range(len(s1)):
            s2window[ord(s2[i])-ord('a')]+=1
        if s1chars==s2window:
            return True
        l = 0
        for i in range(len(s1),len(s2)):
            s2window[ord(s2[i])-ord('a')]+=1
            s2window[ord(s2[l])-ord('a')]-=1
            if s1chars==s2window:
                return True
            l+=1
        return False