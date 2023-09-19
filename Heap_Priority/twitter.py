#!/usr/bin/python3
"""
This is the solution to LeetCode problem 355: 
Design a simplified version of Twitter where users 
can post tweets, follow/unfollow another user, and 
is able to see the 10 most recent tweets in the user's 
news feed.
"""
import heapq
from collections import defaultdict

class Twitter:

    def __init__(self) -> None:

        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> list[int]:

        res, minHeap = [], []

        self.followMap[userId].add(userId)

        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                index = len(self.tweetMap[followee]) - 1
                count, tweetId = self.tweetMap[followee][index]
                minHeap.append([count, tweetId, followee, index - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followee, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followee][index]
                heapq.heappush(minHeap, [count, tweetId, followee, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:

        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

# Driver code
if __name__ == '__main__':

    # Variable, object and function calll
    obj = Twitter()
    obj.postTweet(1, 5)
    print(obj.getNewsFeed(1))
    obj.follow(1, 2)
    obj.postTweet(2, 6)
    print(obj.getNewsFeed(1))
    obj.unfollow(1, 2)
    print(obj.getNewsFeed(1))
