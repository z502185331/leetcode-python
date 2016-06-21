class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [0] * (n + 1)
        for i in xrange(1, n + 1):
            if not obstacleGrid[0][i - 1]:
                dp[i] = 1
            else:
                break
        
        for i in xrange(1, m):
            for j in xrange(1, n + 1):
                if obstacleGrid[i][j - 1]:
                    dp[j] = 0
                else:
                    dp[j] += dp[j - 1]
        return dp[-1]