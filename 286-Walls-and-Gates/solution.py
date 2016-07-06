class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if rooms is None or not rooms or not rooms[0]:
            return
        
        self.INF = 1 << 31 - 1
        self.offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        m, n = len(rooms), len(rooms[0])
        
        for i in xrange(m):
            for j in xrange(n):
                if rooms[i][j] == 0:
                    self.bfs(rooms, i, j)
        
    
    def bfs(self, rooms, x, y):
        m, n = len(rooms), len(rooms[0])
        queue = [(x, y)]
        distance = 0
        
        while queue:
            size = len(queue)
            for i in xrange(size):
                cur_x, cur_y = queue.pop(0)
                
                # cur room has gates with fewer distances
                rooms[cur_x][cur_y] = distance
                
                for j in xrange(len(self.offsets)):
                    next_x = cur_x + self.offsets[j][0]
                    next_y = cur_y + self.offsets[j][1]
                    
                    if next_x >= 0 and next_x < m and \
                        next_y >= 0 and next_y < n and \
                            rooms[next_x][next_y] != -1 and \
                                rooms[next_x][next_y] != 0 and \
                                    rooms[next_x][next_y] > rooms[cur_x][cur_y] + 1:
                        
                        queue.append((next_x, next_y))
            distance += 1
                