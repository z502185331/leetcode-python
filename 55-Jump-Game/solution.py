class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.sol_greedy(nums)
    
    def sol_greedy(self, nums):
        
        if not nums:
            return True
        
        cur = 0
        reach = nums[0]
        m = len(nums)
        
        while cur <= reach:
            if reach >= m - 1:
                return True
            
            if cur + nums[cur] > reach:
                reach = cur + nums[cur]
            
            if cur < reach:
                cur += 1
            else:
                break
        
        return cur == m - 1;
            
            