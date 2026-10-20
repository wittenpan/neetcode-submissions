class StockSpanner:

    def __init__(self):
        #self.day = 0
        self.stk = []
        
    def next(self, price: int) -> int:
        #we can monotonic stk with price, span, and span covers prev popped days.
        span = 1
        while self.stk and self.stk[-1][0]<=price:
            _, sp = self.stk.pop()
            span+=sp
        self.stk.append((price,span))
        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)