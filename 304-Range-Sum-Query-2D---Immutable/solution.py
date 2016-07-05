class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            self.sumMatrix = [[0]]
            return
        
        m, n = len(matrix), len(matrix[0])
        self.sumMatrix = [[0] * (n + 1) for i in xrange(m + 1)]
        
        # Build the sum matrix, so that sumMatrix[i][j] 
        # means the sum of square from (0, 0) to (i, j)
        for i in xrange(m):
            for j in xrange(n):
                self.sumMatrix[i + 1][j + 1] = self.sumMatrix[i][j + 1] + self.sumMatrix[i + 1][j] - \
                        self.sumMatrix[i][j] + matrix[i][j]
                
        print self.sumMatrix

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sumMatrix[row2 + 1][col2 + 1] - self.sumMatrix[row1][col2 + 1] - \
                self.sumMatrix[row2 + 1][col1] + self.sumMatrix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)