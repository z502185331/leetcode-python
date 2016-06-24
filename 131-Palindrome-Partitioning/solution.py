class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        if not s:
            return []
        
        m = len(s)
        matrix = [[False] * m for i in xrange(m)]
        
        # build the palindrome matrix, matrix[i][j] true if s[i: j] is palindrome
        for i in reversed(xrange(m)):
            for j in xrange(i, m):
                matrix[i][j] = (s[i] == s[j] and (j - i <= 1 or matrix[i + 1][j - 1]))
        
        res = []
        def dfs(index, path):
            if index == m:
                res.append(list(path))
                return
            
            for i in xrange(index, m):
                if not matrix[index][i]:
                    continue
                
                path.append(s[index : i + 1])
                dfs(i + 1, path)
                path.pop()
        
        dfs(0, [])
        return res
            
        