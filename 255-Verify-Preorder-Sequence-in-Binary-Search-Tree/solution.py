class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if not preorder:
            return True
        
        m = len(preorder)
        stack = []
        min_val = -sys.maxint - 1
        
        for num in preorder:
            if num < min_val:
                return False
            
            while stack and stack[-1] < num:
                min_val = stack.pop()
            
            stack.append(num)
        
        return True