class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if not n or not k:
            return 0
        
        count = [0] * (n + 1)
        count[0] = 1
        for i in xrange(n):
            if i < 2:
                count[i + 1] = k * count[i]
            elif i == 2:
                count[i + 1] = (count[i] - count[i - 2] * k) * k + count[i - 2] * k * (k - 1)
            else:
                count[i + 1] = (count[i] - count[i - 2] * (k - 1)) * k + count[i - 2] * (k - 1) * (k - 1)
        return count[n]