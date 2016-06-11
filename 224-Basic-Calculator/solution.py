class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        
        s = s.strip()
        
        m = len(s)
        stack_oper = []
        stack_num = []
        
        '''
        A method to calculate the current expression
        '''
        def cal_helper():
            oper = stack_oper.pop()
            num2 = stack_num.pop()
            num1 = stack_num.pop()
            ans = num1 + num2 if oper == '+' else num1 - num2
            stack_num.append(ans)
        
        i = 0
        while i < m:
            # when cur is a digit
            if s[i].isdigit():
                num = int(s[i])
                i += 1
                while i < m and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                stack_num.append(num)
                continue
                
            if s[i] == ' ':
                i += 1
                continue
            
            # when cur is a oper
            if s[i] == ')':
                while stack_oper[-1] != '(':
                    cal_helper()
                stack_oper.pop()
            
            elif s[i] == '(':
                stack_oper.append('(')
            else:
                while stack_oper and stack_oper[-1] != '(':
                    cal_helper()
                stack_oper.append(s[i])
            i +=1
        
        
        while stack_oper:
            cal_helper()
        
        return stack_num[-1] if stack_num else 0
                    