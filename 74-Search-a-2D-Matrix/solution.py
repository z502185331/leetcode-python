class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if matrix is None or not matrix:
            return 0
        
        count = 0
        # traverse all the matrix
        for l in matrix:
            if target >= l[0]:
                if target in l:
                    return True
        return False
