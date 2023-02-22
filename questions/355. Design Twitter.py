class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set) #key = userId, values = list of userIds
        self.tweetMap = defaultdict(list) #key = userId, value = set of tweetId
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweetMap[userId].append([-self.time, tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:

        maxHeap = []
        res = []

        heapq.heapify(maxHeap)

        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:

            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(maxHeap, [count, tweetId, followeeId, index -1])

        while maxHeap and len(res) < 10:
            cnt, tweetId, followeeId, index = heapq.heappop(maxHeap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(maxHeap, [count, tweetId, followeeId, index -1])

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
