class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        m = len(nums)
        nums = [1] + nums + [1] # avoid special cases
        dp = [[0] * (m + 2) for i in xrange(m + 2)]
        
        def helper(i, j):
            if dp[i][j] > 0:    # this has been calculated
                return dp[i][j]
            
            for x in xrange(i, j + 1):
                dp[i][j] = max(dp[i][j], helper(i, x - 1) + nums[i - 1] * nums[x] * nums[j + 1] + helper(x + 1, j))
            
            return dp[i][j]
        
        return helper(1, m)