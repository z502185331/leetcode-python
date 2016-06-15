class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        
        s = s.strip()
        is_exp = False  
        is_dot = False 
        is_digit = False
        m = len(s)
        
        for i in xrange(m):
            if s[i].isdigit():
                is_digit = True
                
            elif s[i] == '.':
                if is_dot or is_exp :  # . can only appear once
                    return False
                else:
                    is_dot = True
                    
            elif s[i] == 'E' or s[i] == 'e':
                if is_exp or not is_digit or (i + 1 < m and s[i + 1] == '.'):
                    return False
                else:
                    is_digit = False
                    is_exp = True
                
            elif s[i] == '+' or s[i] == '-':
                if is_digit or (i > 0 and s[i - 1] == '.'): # + - must behind all the digit or behind E
                    return False
                    
            else:
                return False
                
        return is_digit