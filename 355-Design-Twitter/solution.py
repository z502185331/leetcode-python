class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follow_dict = {}
        self.tweet_list = []

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweet_list.insert(0, (tweetId, userId))
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        
        # get the userId who the user follows includes herself
        followed_list = self.follow_dict.get(userId, [userId])
        
        tweets = []
        i = 0
        
        while i < len(self.tweet_list) and len(tweets) < 10:
            if self.tweet_list[i][1] in followed_list:
                tweets.append(self.tweet_list[i][0])
            
            i += 1
        
        return tweets
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        # get the userId who the user follows includes herself
        self.follow_dict[followerId] = self.follow_dict.get(followerId, [followerId])
        
        if followeeId not in self.follow_dict[followerId]:
            self.follow_dict[followerId].append(followeeId)
        
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        # user cannot unfollow himself
        if followerId == followeeId:
            return
        
        # get the userId who the user follows includes herself
        self.follow_dict[followerId] = self.follow_dict.get(followerId, [followerId])
        
        if followeeId in self.follow_dict[followerId]:
            self.follow_dict[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)