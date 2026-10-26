class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            i = ord(char)-ord('a')
            if curr.children[i] is None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(root, i):
            if i==len(word) and root.endOfWord:
                return True
            elif i==len(word):
                return False
            ans = False
            index = ord(word[i])-ord('a')
            if word[i]==".":
                for j in range(26):
                    if root.children[j] and dfs(root.children[j],i+1):
                        ans = True
                        break
            elif root.children[index]:
                ans = dfs(root.children[index],i+1)
            return ans
        return dfs(self.root,0)
