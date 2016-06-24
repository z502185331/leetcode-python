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
        reach = 0
        
        for num in nums[: -1]:
            reach = max(reach, cur + nums[cur])
            if (reach <= cur):
                return False
            cur += 1
        
        return True;
            
            