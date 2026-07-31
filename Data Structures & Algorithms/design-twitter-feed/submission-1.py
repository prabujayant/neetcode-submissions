import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.time = 0  # Global timestamp
        self.tweets = defaultdict(list)    # userId -> list of (time, tweetId)
        self.follows = defaultdict(set)    # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        users = set(self.follows[userId])  # Get followees
        users.add(userId)                  # Include self

        for uid in users:
            for tweet in self.tweets[uid][-10:]:  # Last 10 tweets from each user
                heapq.heappush(feed, tweet)
                if len(feed) > 10:
                    heapq.heappop(feed)

        feed.sort(reverse=True)  # Sort by most recent
        return [tweetId for _, tweetId in feed]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
