class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        
        if not dungeon or not dungeon[0]:
            return 1
        
        m, n = len(dungeon), len(dungeon[0])
        dp = [1] * n
        dp[-1] = max(1, 1 - dungeon[m - 1][n - 1])
        
        for i in reversed(xrange(n - 1)):
            dp[i] = max(1, dp[i + 1] - dungeon[m - 1][i])
        
        for i in reversed(xrange(m - 1)):
            dp[-1] = max(1, dp[-1] - dungeon[i][n - 1])
            for j in reversed(xrange(n - 1)):
                leftwards = max(1, dp[j + 1] - dungeon[i][j])
                downwards = max(1, dp[j] - dungeon[i][j])
                dp[j] = min(leftwards, downwards)
        
        return dp[0]