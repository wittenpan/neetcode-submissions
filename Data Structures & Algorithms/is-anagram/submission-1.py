class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = dict()
        t_letters = dict()
        for c in s:
            s_letters[c] = s_letters.get(c,0)+1
        for c in t:
            t_letters[c] = t_letters.get(c,0)+1
        for c, v in s_letters.items():
            if c not in t_letters or v!=t_letters.get(c):
                return False
        for c, v in t_letters.items():
            if c not in s_letters or v!=s_letters.get(c):
                return False
        return True