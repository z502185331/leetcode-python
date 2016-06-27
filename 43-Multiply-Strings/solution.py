class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        if not num1 or not num2:
            return '0'
        
        res = ''
        for i in xrange(len(num2)):
            index = len(num2) - i - 1
            local = self.eval_multi(num1, num2[index], i)
            res = self.eval_add(res, local)
        
        i = 0
        while i < len(res) - 1: # neglect last digit
            if res[i] != '0':
                break
            
            i += 1
        
        return res[i :]
            
    
    '''
    A method to muitiply the num1, and num2, num2 only has one digit.
    '''
    def eval_multi(self, num1, num2, base):
        res = ''
        c = 0
        for i in reversed(xrange(len(num1))):
            local = int(num1[i]) * int(num2) + c
            res = str(local % 10) + res
            c = local / 10
        
        if c != 0:
            res = str(c) + res
        
        for i in xrange(base):  # add '0' to the tail
            res += '0'
        
        return res
        
    '''
    A method to add num1 and num2
    '''
    def eval_add(self, num1, num2):
        res = ''
        c = 0
        m, n = len(num1), len(num2)
        
        # reverse two number
        num1, num2 = num1[::-1], num2[::-1]
        
        i = 0
        while i < m or i < n:
            local = c
            if i < m:
                local += int(num1[i])
            
            if i < n:
                local += int(num2[i])
            
            res += str(local % 10)
            c = local / 10
            i += 1
        
        if c != 0:
            res += str(c)
        
        return res[::-1]
                