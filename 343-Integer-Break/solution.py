class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in xrange(2, n + 1):
            for j in xrange(1, i):
                dp[i] = max(dp[i], dp[j] * dp[i - j], j * dp[i - j], dp[j] * (i - j), j * (i - j))
        
        return dp[-1]