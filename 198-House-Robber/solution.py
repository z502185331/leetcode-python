class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        m = len(nums)
        dp = [0] * (m + 1)
        
        for i in xrange(m):
            dp[i + 1] = max(dp[i - 1] + nums[i], dp[i])
        
        return dp[m]