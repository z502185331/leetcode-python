# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        
        res = 0
        tmpBuf = [''] * 4
        
        while n > 0:
            cur = min(read4(tmpBuf), n)
            
            for i in xrange(cur):
                buf[res] = tmpBuf[i]
                res += 1
            
            if cur < 4:
                break
            n -= 4
        
        return res