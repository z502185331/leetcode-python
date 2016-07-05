class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(buildings)
        
        if not buildings:
            return []
        
        if m == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
            
        mid = m / 2
        left = self.getSkyline(buildings[: mid])
        right = self.getSkyline(buildings[mid :])
        
        m, n = len(left), len(right)
        cur = 0
        h1 = h2 = -1
        i, j = 0, 0
        res = []
        
        while i < m and j < n:
            if left[i][0] < right[j][0]:
                cur = left[i][0]
                h1 = left[i][1]
                i += 1
            elif left[i][0] > right[j][0]:
                cur = right[j][0]
                h2 = right[j][1]
                j += 1
            else:
                h1 = left[i][1]
                h2 = right[j][1]
                cur = left[i][0]
                i += 1
                j += 1
        
    
            new = [cur, max(h1, h2)]
            if not res or res[-1][1] != new[1]:
                res.append(new)
        
        while i < m:
            if not res or res[-1][1] != left[i][1]:
                res.append(left[i][:])
            i += 1
        
        while j < n:
            if not res or res[-1][1] != right[j][1]:
                res.append(right[j][:])
            j += 1
        
        return res
        