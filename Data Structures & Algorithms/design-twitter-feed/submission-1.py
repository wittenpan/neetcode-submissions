
from collections import defaultdict, deque
import heapq

class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(deque)
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].popleft()
        self.time += 1
    def getNewsFeed(self, userId: int) -> List[int]:
        #keep only the 10 newest tweets
        top10 = []
        for followeeId in self.following[userId] | {userId}:
            posts = self.tweets.get(followeeId)
            if not posts:
                continue
            index = len(posts) - 1
            count, tweetId = posts[index]
            entry = (count, tweetId, followeeId, index - 1)
            #positive timestamps, oldest at top
            if len(top10) < 10:
                heapq.heappush(top10, entry)
            elif count > top10[0][0]:
                heapq.heapreplace(top10, entry)
        #convert to max heap using negative timestamps
        heap = [
            (-count, tweetId, followeeId, index)
            for count, tweetId, followeeId, index in top10
        ]
        heapq.heapify(heap)
        res = []
        #k-way merge
        while heap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)
            #push next older tweet from the same user
            if index >= 0:
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(
                    heap,
                    (-count, tweetId, followeeId, index - 1)
                )
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
