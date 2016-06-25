class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if not s:
            return ''
        
        m = len(s)
        matrix = [[False] * m for i in xrange(m)]
        max_str = ''
        
        for i in reversed(xrange(m)):
            for j in xrange(i, m):
                if s[i] == s[j] and (j - i <= 1 or matrix[i + 1][j - 1]):
                    matrix[i][j] = True
                    if len(max_str) < j - i + 1:
                        max_str = s[i : j + 1]
        
        return max_str