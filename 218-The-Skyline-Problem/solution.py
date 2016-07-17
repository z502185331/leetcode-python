import heapq
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        
        endpoints = []
        for l, r, _ in buildings:
            endpoints.append(l)
            endpoints.append(r)
        endpoints.sort()
        
        res = []
        heap = []   # max heap
        i = 0
        
        for x in endpoints:
            while heap and heap[0][1] <= x: # pop all the previous line
                heapq.heappop(heap)
                
            while i < len(buildings) and buildings[i][0] == x:  # push all lines starting from x
                heapq.heappush(heap, (-buildings[i][2], buildings[i][1]))     # push the right height and endpoint to heap
                i += 1
            
            height = 0 if not heap else -heap[0][0]
            
            if not res or res[-1][1] != height:
                res.append([x, height])
        
        return res
            
        
    def sol_mergeSort(self, buildings):
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
        