# Solution for LeetCode Problem 355: Design Twitter
# Time Complexity:
# - `postTweet`: O(1), as adding a tweet to the list is constant time.
# - `getNewsFeed`: O(F + T * log(F)), where F is the number of followees for the user and T is the number of tweets processed (up to 10). Heap operations dominate the complexity.
# - `follow` and `unfollow`: O(1), as adding/removing a followee from a set is constant time.
# Space Complexity: O(U + T), where U is the number of unique users and T is the total number of tweets stored.

import heapq
from typing import List

class Twitter:
    """
    Implements the Twitter system with functionality to post tweets, follow/unfollow users,
    and retrieve the 10 most recent tweets from a user's news feed.
    """

    def __init__(self):
        """
        Initializes the Twitter object.
        - `time`: A counter used to assign timestamps to tweets in reverse chronological order.
        - `follow_dict`: Maps users to the set of followees they follow.
        - `tweets_dict`: Maps users to a list of their tweets, with each tweet represented as [timestamp, tweetId].
        """
        self.time = 0
        self.follow_dict = {}
        self.tweets_dict = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Posts a new tweet for a user.
        
        :param userId: ID of the user posting the tweet.
        :param tweetId: ID of the tweet being posted.
        """
        if userId not in self.tweets_dict:
            self.tweets_dict[userId] = []
        self.tweets_dict[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieves the 10 most recent tweets in a user's news feed, which includes their own tweets and tweets from their followees.
        
        :param userId: ID of the user requesting the news feed.
        :return: List of up to 10 tweet IDs, sorted in reverse chronological order.
        """
        res = []
        tweet_heap = []

        # Ensure the user follows themselves
        if userId not in self.follow_dict:
            self.follow_dict[userId] = set()
            self.follow_dict[userId].add(userId)

        # Add the most recent tweets of each followee to a min-heap
        for followee_id in self.follow_dict[userId]:
            if followee_id in self.tweets_dict:
                index = len(self.tweets_dict[followee_id]) - 1
                count, tweet_id = self.tweets_dict[followee_id][index]
                tweet_heap.append([count, followee_id, tweet_id, index - 1])

        heapq.heapify(tweet_heap)

        # Extract the top 10 tweets from the heap
        while tweet_heap and len(res) < 10:
            count, followee_id, tweet_id, index = heapq.heappop(tweet_heap)
            res.append(tweet_id)
            if index >= 0:
                count, tweet_id = self.tweets_dict[followee_id][index]
                heapq.heappush(tweet_heap, [count, followee_id, tweet_id, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Makes one user follow another.
        
        :param followerId: ID of the user who wants to follow.
        :param followeeId: ID of the user to be followed.
        """
        if followerId not in self.follow_dict:
            self.follow_dict[followerId] = set()
            self.follow_dict[followerId].add(followerId)  # Ensure the user follows themselves
        self.follow_dict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Makes one user unfollow another. A user cannot unfollow themselves.
        
        :param followerId: ID of the user who wants to unfollow.
        :param followeeId: ID of the user to be unfollowed.
        """
        if followerId in self.follow_dict:
            self.follow_dict[followerId].discard(followeeId)
