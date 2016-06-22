class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if nums is None:
            return []
        result = []
        self.dfs(result, sorted(nums), 0, [])
        return result
        
        
    def dfs(self, result, S, index, path):
        if path not in result:
            result.append(list(path))
        if index == len(S):
            return
        
        for i in range(index, len(S)):
            path.append(S[i])
            self.dfs(result, S, i + 1, path)
            path.pop()