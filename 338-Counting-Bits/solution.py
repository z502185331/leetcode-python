class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        res = [0]
        
        i = 1
        step = 1
        
        while i < num + 1:
            for j in xrange(step):
                res.append(res[j] + 1)
                i += 1
                
                if i == num + 1:
                    break
                
            step <<= 1
            
        return res
            