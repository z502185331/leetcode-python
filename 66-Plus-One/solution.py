class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]
        
        carry = 1
        for i in reversed(xrange(len(digits))):
            cur = digits[i] + carry
            carry = cur / 10
            digits[i] = cur % 10
            
            if carry == 0:
                break
        
        if carry:
            digits.insert(0, carry)
        
        return digits