class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.map[key])-1
        best = (0,"")
        search = self.map[key]
        while l<=r:
            m = (l+r)//2
            if search[m][1]<=timestamp:
                best = max(best, (search[m][1],search[m][0]))
                l = m+1
            else:
                r = m-1
        return best[1]
            
