class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # test row and colume
        for i in xrange(9):
            s_row = set()
            s_col = set()
            for j in xrange(9):
                if board[i][j] != '.':
                    if board[i][j] in s_row:
                        return False
                    s_row.add(board[i][j])
                
                if board[j][i] != '.':
                    if board[j][i] in s_col:
                        return False
                    s_col.add(board[j][i])

                
        
        # test square
        for i in xrange(3):
            for j in xrange(3):
                s = set()
                for x in xrange(3):
                    for y in xrange(3):
                        cur = board[3 * i + x][3 * j + y]
                        if cur != '.':
                            if cur in s:
                                return False
                            s.add(cur)
        
        return True
        