class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        
        return self.sol_dp(nums)
    
    def sol_greedy(self, nums):
        cur = 0
        reach = 0
        
        for num in nums[: -1]:
            reach = max(reach, cur + nums[cur])
            if (reach <= cur):
                return False
            cur += 1
        
        return True;
    
    
    def sol_dp(self, nums):
        
        m = len(nums)
        dp = [False] * m
        dp[0] = True
        
        for i in xrange(1, m):
            for j in xrange(i):
                if dp[j] and i <= j + nums[j]:
                    dp[i] = True
                    break
            
        
        return dp[m - 1]
        
            
            