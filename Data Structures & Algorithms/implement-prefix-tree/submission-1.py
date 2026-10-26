class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char)-ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            index = ord(char)-ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return curr.endOfWord
            


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            index = ord(char)-ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return True
        