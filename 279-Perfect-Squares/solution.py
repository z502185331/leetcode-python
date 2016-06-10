import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        while n % 4 == 0:
            n /= 4
        
        if n % 8 == 7:
            return 4
        
        i = 0
        while i * i <= n:
            j = int(math.sqrt(n - i * i))
            if i * i + j * j == n:
                return (not not i) + (not not j)
            i += 1
        
        return 3