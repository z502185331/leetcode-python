class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'
        
        # store the sign and remove the sign from n and d
        is_neg = (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0)
        n = abs(numerator)
        d = abs(denominator)
        
        res = ''
        res += str(n / d)   # save the integer
        r = n % d
        
        if r == 0:
            return '-' + res if is_neg else res
        else:
            res += '.'
            
        
        dict = {}
        while r:
            if r in dict:
                index = dict[r]    # get the index where the repeat start
                res = res[: index] + '(' + res[index :] + ')'
                break
            else:
                dict[r] = len(res)
                r *= 10
                res += str(r / d)
                r %= d
        
        return '-' + res if is_neg else res
                
        