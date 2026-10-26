class TrieNode:
    def __init__(self):
        self.children = [None] *26
        self.endOfWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word):
        curr = self.root
        for c in word:
            index = ord(c)-ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.endOfWord = True
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        #like word break 2, we want to put into trie and while curr in trie... we continue
        #once we meet not in trie we increment counter
        #we might want dp
        #dp[i] = min of i:len(s)
        #if we reach a None and not curr.endOfWord, we just return j-i
        #once we reach end of word, we break and dfs again from that spot
        trie = Trie()
        for word in dictionary:
            trie.addWord(word)
        memo = {}
        def dfs(i):
            if i==len(s):
                return 0
            if i in memo:
                return memo[i]
            #baseline treat i as not part as any root
            res = 1+dfs(i+1)
            curr = trie.root
            for j in range(i, len(s)):
                index = ord(s[j])-ord('a')
                if curr.children[index] is None:
                    break
                curr = curr.children[index]
                if curr.endOfWord:
                    res = min(res, dfs(j+1))
            memo[i] = res
            return res
        return dfs(0)