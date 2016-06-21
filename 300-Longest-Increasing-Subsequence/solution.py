class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        m = len(nums)
        dp = [1] * m
        max_len = 1
        
        for i in xrange(1, m):
            for j in xrange(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                
            max_len = max(max_len, dp[i])
        
        return max_len
            