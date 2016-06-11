class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        # start from bottom-left
        # If matrix[i][j] > target, check matrix[i - 1][j]
        # If matrix[i][j] < target, check matrix[i][j + 1]
        i, j = m - 1, 0
        
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
        
        return False
            