class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s.strip()
        if not s:
            return 0
        
        def priority(oper):
            if oper == '+' or oper == '-':
                return 1
            elif oper == '*' or oper == '/':
                return 2
        
        def eval(oper, num1, num2):
            if oper == '+':
                return num1 + num2
                
            elif oper == '-':
                return num1 - num2
            
            elif oper == '*':
                return num1 * num2
            
            else:
                return num1 / num2
        
        stack_oper = []
        stack_num = []
        
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = 10 * num + int(s[i])
                    i += 1

                stack_num.append(num)
                
            else:
                oper = s[i]
                if not stack_oper or priority(oper) > priority(stack_oper[-1]):
                    stack_oper.append(oper)
                
                else:
                    while stack_oper and priority(oper) <= priority(stack_oper[-1]):
                        local_oper = stack_oper.pop()
                        num2 = stack_num.pop()
                        num1 = stack_num.pop()
                        stack_num.append(eval(local_oper, num1, num2))
                    
                    stack_oper.append(oper)
                i += 1
                
        while stack_oper:
            local_oper = stack_oper.pop()
            num2 = stack_num.pop()
            num1 = stack_num.pop()
            stack_num.append(eval(local_oper, num1, num2))
        
        return stack_num.pop()
                
                
            