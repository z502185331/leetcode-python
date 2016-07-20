class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        cur = 0
        last_reach = 0
        max_reach = 0
        count = 0
        
        while cur < len(nums) and cur <= max_reach:
            if cur > last_reach:
                count += 1
                last_reach = max_reach
                
            max_reach = max(max_reach, nums[cur] + cur)
            cur += 1
        
        return count if max_reach >= len(nums) - 1 else 0