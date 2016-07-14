class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 1
        
        m = len(nums)
        for i in xrange(m):
            if i + 1 == nums[i]:
                continue
            
            while i + 1 != nums[i] and nums[i] > 0 and nums[i] < m and nums[i] != nums[nums[i] - 1]:
                tmp = nums[i]
                nums[i] = nums[tmp - 1]
                nums[tmp - 1] = tmp
            
        for i in xrange(0, m):
            if i + 1 != nums[i]:
                return i + 1
        
        return m + 1