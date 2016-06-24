class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
        if len(num) < 3:
            return False
        
        m = len(num)
        
        def helper(num1, num2, index):
            if index + len(num1) + len(num2) == m:
                return True
            
            num3 = int(num1) + int(num2)
            if num[index + len(num1) + len(num2) :].startswith(str(num3)):
                return helper(num2, str(num3), index + len(num1))
            else:
                return False
        
        len_num1 = 1
        while len_num1 < m:
            if num[0] == '0' and len_num1 != 1:
                break
            
            len_num2 = 1
            while len_num2 < m - len_num1:
                if num[len_num1] == '0' and len_num2 != 1:
                    break
                
                if helper(num[: len_num1], num[len_num1 : len_num1 + len_num2], 0):
                    return True
                
                len_num2 += 1
            len_num1 += 1
            
        
        return False
        
        