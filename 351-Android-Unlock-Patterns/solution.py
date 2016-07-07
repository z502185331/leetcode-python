class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        count = self.dfs(m, n, [], -9)
        return count
    
    def dfs(self, m, n, path, prev):
        count = 0
        if m <= len(path) < n: # the path itself is a valid pattern
            count += 1
            
        elif len(path) == n:
            return 1

        for i in xrange(1, 10):
            if i not in path:
                x, y = (i - 1) / 3, (i - 1) % 3
                px, py = (prev - 1) / 3, (prev - 1) % 3
                if (5 not in path and (abs(x - px) == 2 and abs(y - py) == 2)) or \
                        (((y == py and abs(x - px) == 2) or (x == px and abs(y - py) == 2)) and (i + prev) / 2 not in path):
                    
                    continue
                
                path.append(i)
                count += self.dfs(m, n, path, i)
                path.pop()
        return count
            
