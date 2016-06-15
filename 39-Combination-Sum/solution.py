class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if not candidates:
            return []
        
        res = []
        m = len(candidates)
        
        def dfs(index, sum, path):
            if sum == target:
                if path not in res:
                    res.append(list(path))
                return
            
            if index == m:
                return
            
            for i in xrange(index, m):
                if sum + candidates[i] > target:
                    continue
                
                path.append(candidates[i])
                dfs(i, sum + candidates[i], path)
                path.pop()
        
        dfs(0, 0, [])
        return res