class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        if n == 0:
            return []
        
        queens = []
        res = []
        self.dfs(queens, 0, res, n)
        return res
    
    def dfs(self, queens, index, res, n):
        if index == n:
            res.append(self.format(queens, n))
            return
        
        for i in xrange(n):
            
            queens.append(i)
            if self.isValid(queens):
                self.dfs(queens, index + 1, res, n)
            
            queens.pop()
    
    
    
    def isValid(self, queens):
        rowId = len(queens) - 1
        for i in xrange(rowId):
            
            diff = abs(queens[rowId] - queens[i])
            if diff == 0 or diff == rowId - i:
                return False
        
        return True
        
        
    def format(self, queens, n):
        res = []
        for queen in queens:
            s = ['.'] * n
            s[queen] = 'Q'
            res.append(''.join(s))
        return res