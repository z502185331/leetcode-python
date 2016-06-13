class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        minV, maxV = nums[0], nums[0]
        res = nums[0]
        
        for i in range(1, len(nums)):
            tmp = minV
            minV = min(nums[i], maxV * nums[i], minV * nums[i])
            maxV = max(nums[i], maxV * nums[i], tmp * nums[i])
            res = max(maxV, res)
        return res