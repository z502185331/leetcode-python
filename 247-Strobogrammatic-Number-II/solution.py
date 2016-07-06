class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        if n == 0:
            return []
            
        res = []
        self.sources = ['0', '1', '6', '9', '8']
        
        path = ['0'] * n
        self.dfs(0, n, path, res)
        return res
        
    def dfs(self, index, n, path, res):
        if index > n / 2 - 1:
            
            if (n & 1) == 1:    # odd n should process mid num
                for num in ['0', '1', '8']:
                    path[index] = num
                    res.append(''.join(path))
            else:
                res.append(''.join(path))
            return
        
        for num in self.sources:
            if index == 0 and num == '0':   # first digit should not be zero except 0
                continue
            
            path[index] = num
            if num == '6':
                path[n - index - 1] = '9'
            elif num == '9':
                path[n - index - 1] = '6'
            else:
                path[n - index - 1] = num
            
            self.dfs(index + 1, n, path, res)
    