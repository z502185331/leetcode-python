class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        l, r = 0, 0
        local_sum = 0
        m = len(nums)
        min_len = m + 1
        
        while r < m:
            local_sum += nums[r]
            r += 1
            
            while l < r and local_sum >= s:
                min_len = min(min_len, r - l)
                local_sum -= nums[l]
                l += 1
        
        return min_len if min_len != m + 1 else 0