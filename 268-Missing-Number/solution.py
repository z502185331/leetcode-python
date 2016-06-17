class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        # for i in xrange(len(nums)):
        #     while i != nums[i]:
        #         if nums[i] == len(nums):
        for i in xrange(len(nums)):
            if i not in nums:
                return i
                
        return len(nums)
                    