class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        res = []
        
        def dfs(index, path):
            if len(path) == k:
                if path not in res:
                    res.append(list(path))
                return
            
            for i in xrange(index, n + 1):
                path.append(i)
                dfs(i + 1, path)
                path.pop()
        
        dfs(1, [])
        
        return res
            