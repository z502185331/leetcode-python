class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        if matrix is None or not matrix:
            return matrix
        
        m = len(matrix)
        n = len(matrix[0])
        
        # Use the first horizontal and vertical line to record 0
        is_h_z, is_v_z = False, False
        for i in range(m):
            if matrix[i][0] == 0:
                is_v_z = True
                break
        
        for i in range(n):
            if matrix[0][i] == 0:
                is_h_z = True
                break
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if is_h_z:
            for i in range(n):
                matrix[0][i] = 0
        
        if is_v_z:
            for i in range(m):
                matrix[i][0] = 0
        