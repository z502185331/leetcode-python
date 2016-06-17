class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        
        if not input:
            return 0
        
        m = len(input)
        res = []
        if input.isdigit():
            return [int(input)]
        
        for i in xrange(m):
            if input[i].isdigit():
                continue
            
            left_list = self.diffWaysToCompute(input[: i])
            right_list = self.diffWaysToCompute(input[i + 1 :])
            
            for left_num in left_list:
                for right_num in right_list:
                    cur = 0
                    if input[i] == '+':
                        cur = left_num + right_num
                    elif input[i] == '-':
                        cur = left_num - right_num
                    elif input[i] == '*':
                        cur = left_num * right_num
                    
                    res.append(cur)
        return res