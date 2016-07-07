class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        kills = [[0] * n for _ in xrange(m)]
        maxEnemies = 0
        
        # left to right
        for i in xrange(m):
            current = 0
            for j in xrange(n):
                current = self.process(grid, kills, i, j, current)
        
        # top to bottom
        for j in xrange(n):
            current = 0
            for i in xrange(m):
                current = self.process(grid, kills, i, j, current)
                
        # right to left
        for i in xrange(m):
            current = 0
            for j in reversed(xrange(n)):
                current = self.process(grid, kills, i, j, current)
        
        # bottom to top
        for j in xrange(n):
            current = 0
            for i in reversed(xrange(m)):
                current = self.process(grid, kills, i, j, current)
                maxEnemies = max(maxEnemies, kills[i][j])
        
        return maxEnemies
    
    
        
    
    def process(self, grid, kills, i, j, current):
        if grid[i][j] == 'W':   # clear all the enemies behind the wall
            current = 0
        elif grid[i][j] == 'E':
            current += 1
        elif grid[i][j] == '0':
            kills[i][j] += current
        return current
        
        
        
    
    # TLE
    def sol_n3(self, grid):
        m, n = len(grid), len(grid[0])
        kills = [[None] * n for _ in xrange(m)]
        
        maxEnemy = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 'W' or grid[i][j] == 'E':
                    continue
                
                horizontalEnemy, verticalEnemy = -1, -1
                
                # find the enemy number in a horizontal line
                y = j - 1
                while y >= 0:
                    if grid[i][y] == '0':
                        horizontalEnemy = kills[i][y][0]
                        break
                    if grid[i][y] == 'W':
                        break
                    y -= 1
                if horizontalEnemy == -1:
                    horizontalEnemy = self.countHorizEnemy(grid, i, j)
                
                # find the enemy number in a vertical line
                x = i - 1
                while x >= 0:
                    if grid[x][j] == '0':
                        verticalEnemy = kills[x][j][1]
                        break
                    if grid[x][j] == 'W':
                        break
                    x -= 1
                if verticalEnemy == -1:
                    verticalEnemy = self.countVertiEnemy(grid, i, j)
                
                maxEnemy = max(maxEnemy, horizontalEnemy + verticalEnemy)
                kills[i][j] = (horizontalEnemy, verticalEnemy)
        
        return maxEnemy

    
    def countVertiEnemy(self, grid, x, y):
        count = 0
        
        i = x
        while i >= 0 and grid[i][y] != 'W':
            if grid[i][y] == 'E':
                count += 1
            i -= 1
        
        i = x
        while i < len(grid) and grid[i][y] != 'W':
            if grid[i][y] == 'E':
                count += 1
            i += 1
        return count
        
        
    def countHorizEnemy(self, grid, x, y):
        count = 0
        
        i = y
        while i >= 0 and grid[x][i] != 'W':
            if grid[x][i] == 'E':
                count += 1
            i -= 1
        
        i = y
        while i < len(grid[0]) and grid[x][i] != 'W':
            if grid[x][i] == 'E':
                count += 1
            i += 1
        return count