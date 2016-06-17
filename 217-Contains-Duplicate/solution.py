class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if not nums:
            return False
        
        nums.sort()
        for i in xrange(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        
        return False