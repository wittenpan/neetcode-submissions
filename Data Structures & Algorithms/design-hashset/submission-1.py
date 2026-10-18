class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyHashSet:

    def __init__(self):
        self.hashTable = [None]*10000

    def add(self, key: int) -> None:
        if not self.contains(key):
            index = key%10000
            if self.hashTable[index] is None:
                self.hashTable[index] = Node(key)
            else:
                curr = self.hashTable[index]
                while curr.next:
                    curr = curr.next
                curr.next = Node(key)
        

    def remove(self, key: int) -> None:
        index = key%10000
        curr = self.hashTable[index]
        if curr and curr.val == key:
            self.hashTable[index] = curr.next
            return
        prev = None
        while curr:
            if curr.val == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def contains(self, key: int) -> bool:
        index = key%10000
        curr = self.hashTable[index]
        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)