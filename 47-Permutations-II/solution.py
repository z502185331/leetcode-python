class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if not nums:
            return []
            
        res = []
        self.helper(res, [], nums)
        return res
        
    def helper(self, result, path,  nums):
        if not nums :
            result += [path]
        else :
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue;
                self.helper(result, path + [nums[i]], nums[:i] + nums[i + 1:])