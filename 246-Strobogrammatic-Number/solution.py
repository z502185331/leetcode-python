class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
        if not num:
            return True
        
        m = len(num)
        for i in xrange(m / 2 + 1):
            j = m - i - 1
            l, r = num[i], num[j]
            
            if l == r and l in ['0', '1', '8']:
                continue
            
            if (l == '6' and r == '9') or (l == '9' and r == '6'):
                continue
            
            return False
        
        return True