class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # if n == 0:
        #     return 0
        
        # count = 0   # count how many bomb are on
        # for i in xrange(1, n + 1):
        #     local_cnt = 0
        #     for j in xrange(1, i + 1):
        #         if i % j == 0:
        #             local_cnt += 1
                
        #     if (local_cnt & 1) == 1:
        #         count += 1
        
        # return count
        return int(math.sqrt(n))
            