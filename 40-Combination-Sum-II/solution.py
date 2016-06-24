class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if candidates is None or not candidates:
            return []
        
        res = []
        candidates.sort()
        
        def dfs(index, sum, path):
            if sum == target:
                if path not in res:
                    res.append(list(path))
                return
            
            for i in range(index, len(candidates)):
                if sum + candidates[i] > target:
                    continue
                
                path.append(candidates[i])
                dfs(i + 1, sum + candidates[i], path)
                path.pop()
        
        dfs(0, 0, [])
        return res