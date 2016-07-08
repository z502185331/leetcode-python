class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if not nums:
            return []
        
        nums.sort()
        m = len(nums)
        dp = [None] * m
        res = []
        
        for i in xrange(m):
            dp[i] = []
            max_subset = []
            for j in xrange(0, i):
                if nums[i] % nums[j] != 0:
                    continue
                
                factor1, factor2 = nums[j], nums[i] / nums[j]
                len1, len2 = len(dp[j]), len(dp[nums.index(factor2)]) if factor2 in nums and factor2 < nums[i] else 0
                
                # find the factor in the nums and has longer subset
                if len1 > len2 and len1 > len(max_subset):
                    max_subset = dp[j]
                elif len2 >= len1 and len2 > len(max_subset):
                    max_subset = dp[nums.index(factor2)]
            
            dp[i] += max_subset
            dp[i].append(nums[i])
            if len(dp[i]) > len(res):
                res = dp[i]
        
        return res
                