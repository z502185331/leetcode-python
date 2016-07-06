class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        
        if not m or not n:
            return []
        
        parents = [-1] * (m * n + 1)
        res = []
        count = 0
        
        for position in positions:
            x, y = position[0], position[1]
            offset = x * n + y
            parents[offset] = offset
            count += 1
            
            if x - 1 >= 0 and parents[offset - n] != -1 and self.union(parents, offset, offset - n):
                count -= 1
            
            if y + 1 < n and parents[offset + 1] != -1 and self.union(parents, offset, offset + 1):
                count -= 1
            
            if x + 1 < m and parents[offset + n] != -1 and self.union(parents, offset, offset + n):
                count -= 1
            
            if y - 1 >= 0 and parents[offset - 1] != -1 and self.union(parents, offset, offset - 1):
                count -= 1
            
            res.append(count)
        return res
    
    
    
    
    
    def union(self, parents, offset1, offset2):
        root1 = self.find(parents, offset1)
        root2 = self.find(parents, offset2)
        
        if root1 == root2:  # they are connected
            return False
        
        parents[root1] = root2
        return True
    
    
    
    def find(self, parents, offset):
        while offset != parents[offset]:
            parents[offset] = parents[parents[offset]]
            offset = parents[offset]
        
        return offset