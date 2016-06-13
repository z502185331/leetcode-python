class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        isPos = n > 0
        
        def helper(x, n):
            if n == 1:
                return x
            
            half = helper(x, n / 2)
            if (n & 1) == 1:
                return half * half * x
            else:
                return half * half
                
        res = helper(x, abs(n))
        
        return res if isPos else 1 / res