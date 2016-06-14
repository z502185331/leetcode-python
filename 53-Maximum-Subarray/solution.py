class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        m = len(nums)
        local_sum = 0
        max_sum = -sys.maxint - 1
        
        for num in nums:
            local_sum = max(local_sum + num, num)
            max_sum = max(max_sum, local_sum)
        
        return max_sum
        