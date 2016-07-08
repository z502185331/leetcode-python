class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.grid = [[' '] * n for _ in xrange(n)]
        self.offsets = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)], [(-1, -1), (1, 1)], [(1, -1), (-1, 1)]]
        self.chess = {1 : 'X', 2 : 'O'}

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.grid[row][col] = self.chess[player]
        
        if not self.checkWin(player, row, col):
            return 0
        else:
            return player
            
    
    def checkWin(self, player, row, col):
        """
        A method to check whether is win in current turn
        """
        n = len(self.grid)
        for direction in self.offsets:
            count = 1
            
            for offset in direction:
                i, j = row + offset[0], col + offset[1]
                
                while 0 <= i < n and 0 <= j < n and self.grid[i][j] == self.chess[player]:
                    count += 1
                    i, j = i + offset[0], j + offset[1]

            if count == n:
                return True
                
        return False
        

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)