class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num == 0:
            return True
        
        
        l, r = 0, num
        while l < r:
            mid = l + (r - l) / 2
            tmp = mid * mid
            
            if tmp < num:
                l = mid + 1
            
            elif tmp > num:
                r = mid - 1
            
            else:
                return True
        
        return l * l == num