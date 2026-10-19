class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
class MyHashMap:

    def __init__(self):
        self.hashMap = [None]*10000

    def put(self, key: int, value: int) -> None:
        index = key%10000
        if self.hashMap[index] is None:
            self.hashMap[index] = Node(key,value)
            return
        curr = self.hashMap[index]
        prev = None
        while curr:
            if curr.key == key:
                curr.val = value
                return
            prev = curr
            curr = curr.next
        prev.next = Node(key,value)
            

    def get(self, key: int) -> int:
        index = key%10000
        if self.hashMap[index] is None:
            return -1
        curr = self.hashMap[index]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1
    def remove(self, key: int) -> None:
        if self.get(key)==-1:
            return
        index = key%10000
        curr = self.hashMap[index]
        if curr.key == key:
            self.hashMap[index] = curr.next
            return
        prev = None
        while curr:
            if curr.key == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)