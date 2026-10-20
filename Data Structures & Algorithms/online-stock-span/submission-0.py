class StockSpanner:

    def __init__(self):
        #self.day = 0
        self.stk = []
    def next(self, price: int) -> int:
        #we can monotonic stk
        copy = self.stk.copy()
        #self.day+=1
        ans = 1
        while copy and copy[-1]<=price:
            ans+=1
            copy.pop()
        self.stk.append(price)
        return ans



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)