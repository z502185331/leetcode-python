class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        if matrix is None or not matrix or not matrix[0]:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[1] * n for i in xrange(m)] # dp[i][j] shows the longest increasing path at i, j
        isVisited = [[False] * n for i in xrange(m)]
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        
        def dfs(i, j):
            if dp[i][j] != 1:   # this pos has been processed
                return dp[i][j]
                
            isVisited[i][j] = True
            for o in offsets:   # scan the four direction
                new_i = i + o[0]
                new_j = j + o[1]
                if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and \
                        not isVisited[new_i][new_j] and matrix[new_i][new_j] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dfs(new_i, new_j) + 1)
                    isVisited[new_i][new_j] = False
            isVisited[i][j] = False
                    
            return dp[i][j]
        
        max_len = 1
        for i in xrange(m):
            for j in xrange(n):
                max_len = max(dfs(i, j), max_len)
        
        return max_len
                
            
        
        