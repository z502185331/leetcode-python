class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        if not n or not k:
            return []
        
        res = []
        
        def dfs(index, path):
            if len(path) == k:
                res.append(list(path))
                return
            
            for i in range(index, n + 1):
                path.append(i)
                dfs(i + 1, path)
                path.pop()
        
        dfs(1, [])
        return res
            