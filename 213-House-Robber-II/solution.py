class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
            
        m = len(nums)
        
        # 1. rob the first house
        dp1 = [0] * m
        dp1[1] = nums[0]
        for i in xrange(1, m - 1):
            dp1[i + 1] = max(dp1[i], dp1[i - 1] + nums[i])
        
        # 2. rob the last house
        dp2 = [0] * m
        dp2[1] = nums[1]
        for i in xrange(2, m):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])
        
        return max(dp1[-1], dp2[-1])
            