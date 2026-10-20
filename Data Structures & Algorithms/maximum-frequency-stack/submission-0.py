class FreqStack:

    def __init__(self):
        self.maxct = 0
        self.freqs = defaultdict(list)
        self.cnt = {}

    def push(self, val: int) -> None:
        if val not in self.cnt:
            self.cnt[val] = 0
        self.cnt[val]+=1
        if self.cnt[val]>self.maxct:
            self.maxct = self.cnt[val]
            self.freqs[self.maxct] = []
        self.freqs[self.cnt[val]].append(val)
        

    def pop(self) -> int:
        res = self.freqs[self.maxct].pop()
        self.cnt[res]-=1
        if not self.freqs[self.maxct]:
            self.maxct-=1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()