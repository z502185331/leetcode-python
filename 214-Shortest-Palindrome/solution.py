class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if not s:
            return s
            
        m = len(s)
        j = 0
        for i in reversed(xrange(m)):
            if s[i] == s[j]:
                j += 1
        
        if j == m:
            return s
        
        suffix = s[j :]
        prefix = suffix[:: -1]
        mid = self.shortestPalindrome(s[: j])
        return prefix + mid + suffix
    
    # TLE
    def sol_dp(self, s):
        m = len(s)
        matrix = [[False] * m for _ in xrange(m)]
        maxLen = 0
        for i in reversed(xrange(m)):
            for j in xrange(i, m):
                if s[i] == s[j] and (j - i < 2 or matrix[i + 1][j - 1]):
                    matrix[i][j] = True
                    
                    # test the longest palindrome starting from 0
                    if i == 0:
                        maxLen = max(maxLen, j + 1)
        
        right = s[maxLen :] # the right side of s which is not in palindrome starting from 0
        return right[:: -1] + s