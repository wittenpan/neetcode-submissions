from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #can bucket sort
        buckets = [[] for _ in range(len(nums)+1)]
        counts = Counter(nums)
        for key, val in counts.items():
            buckets[val].append(key)
        ans = []
        i = len(nums)
        while len(ans)<k:
            ans+=buckets[i]
            i-=1
        return ans