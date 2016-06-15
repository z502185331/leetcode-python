class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        
        m = len(s)
        dp = [0] * (m + 1)
        dp[0] = dp[1] = 1
        
        if s[0] == '0':
            return 0
        
        for i in xrange(1, m):
            cur_num = int(s[i])
            cp_num = int(s[i - 1 : i + 1])
            
            # deal with exception
            if cur_num == 0 and (cp_num < 10 or cp_num > 26):
                return 0
            
            if cur_num != 0:
                dp[i + 1] += dp[i]
            
            if cp_num >= 10 and cp_num <= 26:
                dp[i + 1] += dp[i - 1]
        
        return dp[m]
            