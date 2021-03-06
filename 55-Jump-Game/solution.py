class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        
        return self.sol_greedy(nums)
    
    def sol_greedy(self, nums):
        cur = 0
        reach = 0
        
        for num in nums[: -1]:
            reach = max(reach, cur + nums[cur])
            if (reach <= cur):
                return False
            cur += 1
        
        return True;
    
    
    # TLE
    def sol_dp(self, nums):
        
        m = len(nums)
        dp = [False] * m
        dp[0] = True
        
        for i in xrange(m):
            if dp[i]:
                for j in xrange(i + 1, i + nums[i] + 1):
                    if j < m:
                        dp[j] = True
                    else:
                        break
            else:
                break
        
        return dp[m - 1]
        
            
            