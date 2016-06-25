class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if not s:
            return 0
        
        m = len(s)
        maxL = 0
        maxStr = ''
        
        dp = [[False] * m for i in xrange(m)]
        for i in reversed(xrange(m)):
            for j in xrange(i, m):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i + 1 > maxL:
                        maxL = j - i + 1
                        maxStr = s[i : j + 1]
        return maxStr