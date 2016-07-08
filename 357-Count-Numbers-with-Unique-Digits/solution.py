class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 10:
            return None
        
        dp = [1] +  [9] * n
        
        for i in xrange(2, n + 1):
            
            for x in xrange(9, 9 - i + 1, -1):
                dp[i] *= x
        
        return sum(dp)