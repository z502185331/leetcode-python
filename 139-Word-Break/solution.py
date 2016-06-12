class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        
        if s is None or wordDict is None:
            return False
        
        if not wordDict:
            return not s
        
        return self.sol_dp(s, wordDict)
    
    
    '''
    A method to solve the problem by dp
    '''
    def sol_dp(self, s, dict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        maxLength = max([len(w) for w in dict])
        for i in xrange(1, len(s) + 1):
            for j in xrange(max(0, i - maxLength), i):
                if dp[j] and s[j : i] in dict:
                    dp[i] = True
        return dp[-1]