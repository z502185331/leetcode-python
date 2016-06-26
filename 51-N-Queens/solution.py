class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        if n == 0:
            return []
        
        self.rows = [False] * n
        self.columns = [False] * n
        self.ups = [False] * (2 * n - 1)
        self.downs = [False] * (2 * n - 1)
        
        queens = [-1] * n
        res = []
        self.dfs(queens, 0, res, n)
        return res
    
    def dfs(self, queens, index, res, n):
        if index == n:
            res.append(self.format(queens, n))
            return
        
        for i in xrange(n):
            if self.isOccupied(index, i, n):
                continue
            
            self.setOccupied(index, i, n)
            queens[index] = i
            self.dfs(queens, index + 1, res, n)
            self.removeOccupied(index, i, n)
        
    
    def isOccupied(self, i, j, n):
        return self.rows[i] or self.columns[j] or \
            self.ups[i + j] or self.downs[i - j + n - 1]
            
    def setOccupied(self, i, j, n):
        self.rows[i] = True
        self.columns[j] = True
        self.ups[i + j] = True 
        self.downs[i - j + n - 1] = True
    
    def removeOccupied(self, i, j, n):
        self.rows[i] = False
        self.columns[j] = False
        self.ups[i + j] = False
        self.downs[i - j + n - 1] = False
        
        
    def format(self, queens, n):
        res = []
        for queen in queens:
            s = ['.'] * n
            s[queen] = 'Q'
            res.append(''.join(s))
        return res