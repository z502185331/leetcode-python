class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        # dp = [[0] * (n + 1) for i in xrange(m + 1)]
        # dp[0][1] = 1
        # for i in xrange(m):
        #     for j in xrange(n):
        #         dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1]
        
        # return dp[m][n]
        
        dp = [1] * n
        
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[j] += dp[j - 1]
        
        return dp[-1]