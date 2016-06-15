class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if not nums:
            return []
            
        res = []
        nums.sort()
        size = len(nums)
        
        def dfs(nums, path):
            if len(path) == size:
                res.append(path)
            
            for i in xrange(len(nums)):
                if i > 0 and nums[i - 1] == nums[i]:
                    continue
                
                dfs(nums[: i] + nums[i + 1 :], path + [nums[i]])
        
        dfs(nums, [])
        return res
        
    def helper(self, result, path,  nums):
        if not nums :
            result += [path]
        else :
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue;
                self.helper(result, path + [nums[i]], nums[:i] + nums[i + 1:])