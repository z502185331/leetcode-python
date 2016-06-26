class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
            
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for i in xrange(m + 1)]
        for i in xrange(m + 1):
            dp[i][0] = i
        
        for i in xrange(n + 1):
            dp[0][i] = i
        
        for i in xrange(m):
            for j in xrange(n):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = \
                        min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1
        return dp[-1][-1]