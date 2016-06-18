class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for i in xrange(n):
            for j in xrange(i + 1):
                dp[i + 1] += dp[j] * dp[i - j]
        
        return dp[n]
                
        