class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(k, n, 1, 0, [], res)
        return res
    
    def dfs(self, k, target, index, path_sum, path, res):
        if len(path) == k:
            if path_sum == target:
                if path not in res:
                    res.append(list(path))
                
            return
        
        for i in xrange(index, 10):
            if path_sum + i > target:   # all the number are positive
                break
            
            path.append(i)
            self.dfs(k, target, i + 1, path_sum + i, path, res)
            path.pop()
            