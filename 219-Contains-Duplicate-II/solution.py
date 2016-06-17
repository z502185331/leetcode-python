class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        if not nums:
            return False
        
        l = []
        for i in xrange(len(nums)):
            if nums[i] in l:
                return True
            
            l.append(nums[i])
            if len(l) > k:
                l.pop(0)
        return False
        