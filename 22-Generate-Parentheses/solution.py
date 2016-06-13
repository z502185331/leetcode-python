class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        if n == 0:
            return []
        
        res = []
        def helper(left_count, right_count, path):
            if left_count == n and right_count == n:
                res.append(path)
                return
            
            if left_count < n:
                helper(left_count + 1, right_count, path + '(')
            
            if left_count > right_count:
                helper(left_count, right_count + 1, path + ')')
        
        helper(0, 0, '')
        return res