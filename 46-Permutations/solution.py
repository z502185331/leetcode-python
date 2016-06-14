class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if not nums:
            return []
            
        res = []
        def dfs(path):
            if len(path) == len(nums):
                res.append(list(path))
                return
            
            for i in xrange(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                dfs(path)
                path.pop()
            
        dfs([])
        return res