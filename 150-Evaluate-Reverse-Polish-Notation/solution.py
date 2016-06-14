class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
        
        stack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self.eval(token, num1, num2))
        return stack.pop()
    
    
    def eval(self, oper, num1, num2):
        if oper == '+':
            return num1 + num2
        elif oper == '-':
            return num1 - num2
        elif oper == '*':
            return num1 * num2
        else:
            return int(num1 / float(num2))