class MinStack:

    def __init__(self):
        self.mins = []
        self.stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if self.mins:
            self.mins.append(min(self.mins[-1],val))
        else:
            self.mins.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.mins[-1]
