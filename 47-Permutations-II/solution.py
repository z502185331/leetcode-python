class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if not nums:
            return []
            
        res = []
        def dfs(path, index_path):
            if len(path) == len(nums):
                if path not in res:
                    res.append(list(path))
                return
            
            for i in xrange(len(nums)):
                if i in index_path:
                    continue
                path.append(nums[i])
                index_path.append(i)
                dfs(path, index_path)
                path.pop()
                index_path.pop()
            
        dfs([], [])
        return res