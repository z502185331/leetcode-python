class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        if matrix is None or not matrix:
            return matrix
            
        m = len(matrix)
        
        for i in range(m):
            for j in range(i + 1, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(m):
            matrix[i].reverse()