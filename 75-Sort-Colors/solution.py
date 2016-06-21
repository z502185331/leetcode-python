class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if not nums:
            return
        
        m = len(nums)
        l, r = 0, m - 1 # l is the index to put 0, r is the index to put 2
        i = 0
        
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
                
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
                
            else:
                i += 1
                
        for i in xrange(l, r + 1):
            nums[i] = 1
        
        