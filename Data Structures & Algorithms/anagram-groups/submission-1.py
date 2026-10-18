class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getTuple(s):
            chars = [0]*26
            for c in s:
                chars[ord(c)-ord('a')]+=1
            return tuple(chars)
        anagram_dictionary = defaultdict(list)
        for s in strs:
            anagram_dictionary[getTuple(s)].append(s)
        return list(anagram_dictionary.values())